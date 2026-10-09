import React, { Suspense, lazy, useEffect, useMemo, useState } from "react";
import PropTypes from "prop-types";
import {
  Button,
  Container,
  DEFAULT_HELP_MODE,
  Grid,
  Header,
  HELP_MODES,
  HelpModeProvider,
  Icon,
  Loader,
  Menu,
  Message,
  Progress,
  Segment,
} from "mbdb-semantic-ui-react";
import { FieldDataProvider, FormConfigProvider } from "@js/oarepo_ui/forms";
import { REGISTRY, STEPS } from "./registry";
import { StoryFrame } from "./StoryFrame";

// One lazy pane per built entry, created once so each story chunk loads only once.
const ENTRIES = REGISTRY.map((entry) => ({
  ...entry,
  title: entry.title || entry.key,
  Pane:
    entry.load &&
    lazy(() =>
      entry.load().then(({ default: story }) => ({
        default: (props) => <StoryFrame story={story} {...props} />,
      }))
    ),
}));

const PROGRESS_ENTRIES = ENTRIES.filter(
  ({ step }) => STEPS.find((s) => s.step === step).inProgress !== false
);

const keyFromHash = () => {
  const key = decodeURIComponent(window.location.hash.slice(1));
  return ENTRIES.some((entry) => entry.key === key) ? key : ENTRIES[0].key;
};

const EntryHeader = ({ entry }) => (
  <Header as="h2" dividing>
    {entry.title}
    <Header.Subheader>
      Step {entry.step} · conversion_docs/poc/{entry.design}
    </Header.Subheader>
  </Header>
);

EntryHeader.propTypes = {
  entry: PropTypes.object.isRequired,
};

export const PlaygroundApp = ({ uiModel }) => {
  const [activeKey, setActiveKey] = useState(keyFromHash);
  // Global help display for every story; remembered across reloads.
  const [helpMode, setHelpMode] = useState(() => {
    const m = localStorage.getItem("mbdb.playground.helpMode");
    return HELP_MODES.includes(m) ? m : DEFAULT_HELP_MODE;
  });
  // One-shot default for the collapsible parts of the current story ("open" /
  // "closed"; undefined = the blocks' own default). `epoch` remounts the story
  // content so the blocks re-read it, while Formik (and its values) stays put.
  const [disclosure, setDisclosure] = useState(undefined);
  const [epoch, setEpoch] = useState(0);
  const expandAll = () => {
    setDisclosure("open");
    setEpoch((n) => n + 1);
  };
  const collapseAll = () => {
    setDisclosure("closed");
    setEpoch((n) => n + 1);
  };
  // review mode (design ReviewMode.md): a toggle next to Expand/Collapse all
  const [review, setReview] = useState(false);

  const selectHelpMode = (mode) => {
    setHelpMode(mode);
    localStorage.setItem("mbdb.playground.helpMode", mode);
  };

  useEffect(() => {
    const onHashChange = () => setActiveKey(keyFromHash());
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  const formConfig = useMemo(
    () => ({ config: { ui_model: uiModel } }),
    [uiModel]
  );

  const active = ENTRIES.find((entry) => entry.key === activeKey);
  const built = PROGRESS_ENTRIES.filter((entry) => entry.load).length;

  return (
    <FormConfigProvider value={formConfig}>
      <FieldDataProvider>
        <HelpModeProvider mode={helpMode}>
          <Container fluid className="rel-p-2">
            <Grid>
              <Grid.Row>
                <Grid.Column width={10}>
                  <Header as="h1">
                    MBDB playground
                    <Header.Subheader>
                      Entities of interest PoC
                    </Header.Subheader>
                  </Header>
                </Grid.Column>
                <Grid.Column width={6}>
                  <Progress
                    value={built}
                    total={PROGRESS_ENTRIES.length}
                    label={`${built} / ${PROGRESS_ENTRIES.length} components built`}
                    size="small"
                    success={built === PROGRESS_ENTRIES.length}
                  />
                  <Button.Group>
                    <Button
                      type="button"
                      content="Help text"
                      active={helpMode === "invenio"}
                      onClick={() => selectHelpMode("invenio")}
                    />
                    <Button
                      type="button"
                      content="Help popups"
                      active={helpMode === "popup"}
                      onClick={() => selectHelpMode("popup")}
                    />
                  </Button.Group>
                  <Button.Group>
                    <Button
                      type="button"
                      content="Expand all"
                      onClick={expandAll}
                    />
                    <Button
                      type="button"
                      content="Collapse all"
                      onClick={collapseAll}
                    />
                  </Button.Group>
                  <Button.Group>
                    <Button
                      type="button"
                      toggle
                      active={review}
                      content={review ? "Review: on" : "Review"}
                      onClick={() => setReview((v) => !v)}
                    />
                  </Button.Group>
                </Grid.Column>
              </Grid.Row>
              <Grid.Row>
                <Grid.Column width={4}>
                  <Menu vertical fluid>
                    {STEPS.map(({ step, title }) => (
                      <Menu.Item key={step}>
                        <Menu.Header>
                          {step} · {title}
                        </Menu.Header>
                        <Menu.Menu>
                          {ENTRIES.filter((entry) => entry.step === step).map(
                            (entry) => (
                              // A hash link: navigation goes through the
                              // hashchange listener, and planned (greyed out)
                              // entries stay clickable.
                              <Menu.Item
                                key={entry.key}
                                as="a"
                                href={`#${entry.key}`}
                                active={entry.key === activeKey}
                                disabled={
                                  !entry.load && entry.key !== activeKey
                                }
                              >
                                <Icon
                                  name={entry.load ? "check" : "circle outline"}
                                  color={entry.load ? "green" : undefined}
                                />
                                {entry.title}
                              </Menu.Item>
                            )
                          )}
                        </Menu.Menu>
                      </Menu.Item>
                    ))}
                  </Menu>
                </Grid.Column>
                <Grid.Column width={12}>
                  <Segment>
                    <EntryHeader entry={active} />
                    {active.Pane ? (
                      <Suspense fallback={<Loader active inline="centered" />}>
                        <active.Pane
                          key={active.key}
                          disclosure={disclosure}
                          epoch={epoch}
                          review={review}
                        />
                      </Suspense>
                    ) : (
                      <Message
                        info
                        header="Not built yet"
                        content={`Design: conversion_docs/poc/${active.design}`}
                      />
                    )}
                  </Segment>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          </Container>
        </HelpModeProvider>
      </FieldDataProvider>
    </FormConfigProvider>
  );
};

PlaygroundApp.propTypes = {
  uiModel: PropTypes.object.isRequired,
};
