import React, { useState } from "react";
import PropTypes from "prop-types";
import { Formik } from "formik";
import {
  Accordion,
  Button,
  DisclosureDefaultProvider,
  Divider,
  Form,
  Icon,
  Menu,
  Message,
  ReviewModeProvider,
  Segment,
} from "mbdb-semantic-ui-react";
import { MbdbDepositRecordSerializer } from "@js/mbdb/forms/serializer";
import { EntityDetails } from "@js/mbdb/forms/sections/EntitiesOfInterest/EntityDetails";
import { ENTITY_PATH } from "./fixtures";

const serializer = new MbdbDepositRecordSerializer();

const ERRORS_EXAMPLE = `[
  {
    "field": "metadata.general_parameters.entities_of_interest.0.name",
    "messages": ["Missing data for required field."]
  }
]`;

// Scenario switches and resets remount the form (new `key`). Applying server
// errors does NOT remount: the deposit form reinitializes a Formik that stays
// mounted (enableReinitialize), so blocks that must react to new errors while
// staying mounted (open a row with errors, keep a badge) can be checked here.
const mountScenario = (scenario, key) => ({
  key,
  initialValues: scenario.initialValues || {},
  initialErrors: scenario.initialErrors || {},
});

// `text` lives in StoryFrame: applying errors reinitializes the form's
// initial errors (no remount), and this panel keeps its state.
const ServerErrorsPanel = ({ text, setText, onApply, onClear }) => {
  const [parseError, setParseError] = useState(null);

  const apply = () => {
    try {
      const errors = JSON.parse(text);
      setParseError(null);
      onApply(serializer.deserializeErrors(errors));
    } catch (e) {
      setParseError(e.message);
    }
  };

  return (
    <Form error={!!parseError}>
      <Form.TextArea
        rows={6}
        value={text}
        onChange={(e, { value }) => setText(value)}
      />
      <Message error content={parseError} />
      <Button type="button" primary size="small" onClick={apply}>
        Apply errors
      </Button>
      <Button type="button" size="small" onClick={onClear}>
        Clear
      </Button>
    </Form>
  );
};

ServerErrorsPanel.propTypes = {
  text: PropTypes.string.isRequired,
  setText: PropTypes.func.isRequired,
  onApply: PropTypes.func.isRequired,
  onClear: PropTypes.func.isRequired,
};

export const StoryFrame = ({
  story,
  disclosure,
  epoch = 0,
  review = false,
}) => {
  const { scenarios } = story;
  const [scenarioIndex, setScenarioIndex] = useState(0);
  const [mount, setMount] = useState(() => mountScenario(scenarios[0], 0));
  const [open, setOpen] = useState({ values: true, errors: false });
  const [errorsText, setErrorsText] = useState(ERRORS_EXAMPLE);

  const scenario = scenarios[scenarioIndex];
  const Content = scenario.render;

  const selectScenario = (index) => {
    setScenarioIndex(index);
    setMount(mountScenario(scenarios[index], mount.key + 1));
  };
  const reinit = (initialValues, initialErrors) =>
    setMount((m) => ({ ...m, initialValues, initialErrors }));
  const toggle = (panel) => setOpen({ ...open, [panel]: !open[panel] });

  return (
    <>
      <Menu secondary pointing>
        {scenarios.map(({ name }, index) => (
          <Menu.Item
            key={name}
            name={name}
            active={index === scenarioIndex}
            onClick={() => selectScenario(index)}
          />
        ))}
      </Menu>

      <Formik
        key={mount.key}
        enableReinitialize
        initialValues={mount.initialValues}
        initialErrors={mount.initialErrors}
        onSubmit={() => {}}
      >
        {({ values, handleSubmit }) => (
          <>
            <Form onSubmit={handleSubmit}>
              {/* The one-shot Expand/Collapse all default, applied to the
                  blocks' INITIAL state. `key={epoch}` remounts only the story
                  content when the default changes, so the blocks re-read it;
                  Formik stays mounted and the values are kept. Review mode
                  (ReviewModeProvider) also opens everything and keys the
                  content by the mode; a story that declares `review: "entity"`
                  shows the entity's read-only details instead. */}
              <DisclosureDefaultProvider value={disclosure}>
                <ReviewModeProvider review={review}>
                  <React.Fragment
                    key={`${epoch}-${review ? "review" : "edit"}`}
                  >
                    {review && story.review === "entity" ? (
                      <EntityDetails fieldPath={ENTITY_PATH} />
                    ) : (
                      <Content />
                    )}
                  </React.Fragment>
                </ReviewModeProvider>
              </DisclosureDefaultProvider>
            </Form>

            <Divider />
            <Accordion fluid styled>
              <Accordion.Title
                active={open.values}
                onClick={() => toggle("values")}
              >
                <Icon name="dropdown" />
                Form values
              </Accordion.Title>
              <Accordion.Content active={open.values}>
                <Button
                  type="button"
                  size="small"
                  floated="right"
                  onClick={() => selectScenario(scenarioIndex)}
                >
                  Reset
                </Button>
                <Segment basic>
                  <pre>{JSON.stringify(values, null, 2)}</pre>
                </Segment>
              </Accordion.Content>

              <Accordion.Title
                active={open.errors}
                onClick={() => toggle("errors")}
              >
                <Icon name="dropdown" />
                Server errors (inject)
              </Accordion.Title>
              <Accordion.Content active={open.errors}>
                <ServerErrorsPanel
                  text={errorsText}
                  setText={setErrorsText}
                  onApply={(errors) => reinit(values, errors)}
                  onClear={() => reinit(values, {})}
                />
              </Accordion.Content>
            </Accordion>
          </>
        )}
      </Formik>
    </>
  );
};

StoryFrame.propTypes = {
  story: PropTypes.shape({
    title: PropTypes.string,
    // a story that declares `review: "entity"` shows the entity's details in
    // review mode instead of its form (design ReviewMode.md)
    review: PropTypes.string,
    scenarios: PropTypes.arrayOf(
      PropTypes.shape({
        name: PropTypes.string.isRequired,
        initialValues: PropTypes.object,
        initialErrors: PropTypes.object,
        render: PropTypes.elementType.isRequired,
      })
    ).isRequired,
  }).isRequired,
  // the playground's one-shot Expand all / Collapse all default; absent in
  // tests and anywhere `StoryFrame` is used without the buttons
  disclosure: PropTypes.oneOf(["open", "closed"]),
  // bumped by the buttons to remount the story content and re-read `disclosure`
  epoch: PropTypes.number,
  // review mode (design ReviewMode.md): all open, no edit affordances, and the
  // stories that declare `review: "entity"` show the entity's details
  review: PropTypes.bool,
};
