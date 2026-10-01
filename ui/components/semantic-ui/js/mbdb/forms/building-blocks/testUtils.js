import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { Formik } from "formik";
import { HelpModeProvider } from "mbdb-semantic-ui-react";

// Shared test harness for the building-block tests. One jest.mock for
// "@js/oarepo_ui/forms" (oarepoFake) and one renderInForm/unmountForm pair,
// so a change to the mock contract is a single edit instead of one per file.

// --- oarepo_ui/forms fake ------------------------------------------------

// Turns a ui_model path leaf ("some_field") into a readable label
// ("Some field"); the default getFieldData label when no override is set.
const leafLabel = (path) => {
  const leaf = String(path).split(".").pop();
  const words = leaf.replace(/_/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
};

// Per-path overrides, { [fieldPath]: {label, helpText, required} }. A test
// sets this (usually in beforeEach, resetting to {}) to inject model labels
// or help; paths with no entry fall back to the readable-leaf label and
// helpText null.
let fakeUiModel = {};

export const setFakeUiModel = (uiModel) => {
  fakeUiModel = uiModel ?? {};
};

// The default getFieldData: per-path override wins, else the leaf label with
// helpText null. fieldRepresentation is ignored (the blocks use only "text").
const defaultGetFieldData = ({ fieldPath }) => {
  const override = fakeUiModel[fieldPath] ?? {};
  return {
    label: override.label ?? leafLabel(fieldPath),
    helpText: override.helpText ?? null,
    required: override.required,
  };
};

// Provider stand-ins. They only render their children: the fake getFieldData
// reads setFakeUiModel's module map, not context, so no real provider is
// needed. Exported so tests that render providers explicitly keep working.
export const FormConfigProvider = ({ children }) => children;
export const FieldDataProvider = ({ children }) => children;
FormConfigProvider.propTypes = {
  children: PropTypes.node,
  value: PropTypes.any,
};
FieldDataProvider.propTypes = { children: PropTypes.node };

// The fake "@js/oarepo_ui/forms" module. Wire it up with ONE line in a test:
//   jest.mock("@js/oarepo_ui/forms", () =>
//     jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
//   );
// (jest.mock factories must be self-contained; requireActual inside is legal.)
export const oarepoFake = {
  FormConfigProvider,
  FieldDataProvider,
  useFieldData: () => ({ getFieldData: defaultGetFieldData }),
};

// --- render helper --------------------------------------------------------

// Render `ui` inside a real Formik (enableReinitialize, like the deposit
// form) into a fresh container appended to document.body. helpMode wraps the
// tree in HelpModeProvider. Returns the container; pass it to unmountForm.
export const renderInForm = (
  ui,
  { initialValues = {}, initialErrors = {}, helpMode } = {}
) => {
  const container = document.createElement("div");
  document.body.appendChild(container);
  const tree = (
    <Formik
      initialValues={initialValues}
      initialErrors={initialErrors}
      enableReinitialize
      onSubmit={() => {}}
    >
      {helpMode ? (
        <HelpModeProvider mode={helpMode}>{ui}</HelpModeProvider>
      ) : (
        ui
      )}
    </Formik>
  );
  act(() => {
    ReactDOM.render(tree, container);
  });
  return container;
};

// Unmount and remove a container returned by renderInForm. Also removes any
// modal/dimmer portals Semantic mounted on document.body.
export const unmountForm = (container) => {
  if (!container) return;
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
  document
    .querySelectorAll(".ui.modals, .ui.dimmer")
    .forEach((el) => el.remove());
};
