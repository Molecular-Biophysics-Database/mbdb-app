import React, { useState } from "react";
import PropTypes from "prop-types";
import { Formik } from "formik";
import {
  Accordion,
  Button,
  Divider,
  Form,
  Icon,
  Menu,
  Message,
  Segment,
} from "mbdb-semantic-ui-react";
// Not from "@js/mbdb/forms": its index pulls in react-searchkit, whose d3
// dependency (ESM) Jest cannot load.
import { MbdbDepositRecordSerializer } from "@js/mbdb/forms/serializer";

const serializer = new MbdbDepositRecordSerializer();

const ERRORS_EXAMPLE = `[
  {
    "field": "metadata.general_parameters.entities_of_interest.0.name",
    "messages": ["Missing data for required field."]
  }
]`;

// Formik state of one mount. Every change of scenario, reset, or applied
// server errors remounts the form (new `key`), because the deposit form also
// shows server errors as Formik `initialErrors` of a reinitialized form.
const mountScenario = (scenario, key) => ({
  key,
  initialValues: scenario.initialValues || {},
  initialErrors: scenario.initialErrors || {},
});

// `text` lives in StoryFrame: applying errors remounts the form and this panel.
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

export const StoryFrame = ({ story }) => {
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
  const remount = (initialValues, initialErrors) =>
    setMount({ key: mount.key + 1, initialValues, initialErrors });
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
        initialValues={mount.initialValues}
        initialErrors={mount.initialErrors}
        onSubmit={() => {}}
      >
        {({ values, handleSubmit }) => (
          <>
            <Form onSubmit={handleSubmit}>
              <Content />
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
                  onApply={(errors) => remount(values, errors)}
                  onClear={() => remount(values, {})}
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
    scenarios: PropTypes.arrayOf(
      PropTypes.shape({
        name: PropTypes.string.isRequired,
        initialValues: PropTypes.object,
        initialErrors: PropTypes.object,
        render: PropTypes.elementType.isRequired,
      })
    ).isRequired,
  }).isRequired,
};
