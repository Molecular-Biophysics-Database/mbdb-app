import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import fs from "fs";
import path from "path";
import { Formik, FormikProvider, Field, getIn, useFormikContext } from "formik";
import { HelpModeProvider } from "mbdb-semantic-ui-react";
import { useFieldErrors } from "./errors";

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

// --- structured ui_model (the real model fixture) ---------------

// The deposit ui_model, trimmed to the entities_of_interest path, generated
// from /playground by __fixtures__/generate-ui-model.mjs. Read lazily so suites
// that do not need it never parse the file.
export const realUiModel = () =>
  JSON.parse(
    fs.readFileSync(
      path.join(__dirname, "__fixtures__", "ui_model.json"),
      "utf8"
    )
  );

// The ui_model mockOarepoForms() feeds useFormConfig; undefined keeps the flat
// setFakeUiModel path.
let structuredUiModel;
export const setStructuredUiModel = (uiModel) => {
  structuredUiModel = uiModel ?? undefined;
};

// A StringArrayField stand-in: oarepo's own needs a context the mbdb wrapper
// does not pass in tests. Renders the current list so a test can read it.
const StringArrayFieldStandIn = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const items = getIn(values, fieldPath) ?? [];
  return (
    <div data-testid="specs" data-path={fieldPath}>
      {items.join(", ")}
    </div>
  );
};
StringArrayFieldStandIn.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};

// Ready-made "@js/oarepo_ui/forms" mock for the block tests: the
// shared fake plus the StringArrayField stand-in and useFormConfig reading the
// structured ui_model. Use it as:
//   jest.mock("@js/oarepo_ui/forms", () =>
//     jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").mockOarepoForms()
//   );
// and call setStructuredUiModel(realUiModel()) where the real shape is needed.
export const mockOarepoForms = () => ({
  ...oarepoFake,
  StringArrayField: StringArrayFieldStandIn,
  useFormConfig: () => ({ config: { ui_model: structuredUiModel } }),
});

// A client-only uuid for the row-key mocks (jsdom has no WebCrypto). Its
// shape is `uuid-N`; the sequence resets per test file.
//   jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
//     jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").mockRandomUUID()
//   );
let uuidSeq = 0;
export const mockRandomUUID = () => ({
  randomUUID: () => `uuid-${++uuidSeq}`,
});

// A synchronous vocabulary title/item cache, mirroring the real
// vocabularyTitles module. Seed it with
// setFakeVocabulary({ "organisms/taxid:1": { title: "…", customFields: … } });
// rememberItem writes into it (like the real cache), so a fake pick can seed
// the item a later read resolves.
let fakeVocabulary = {};
export const setFakeVocabulary = (items) => {
  fakeVocabulary = items ?? {};
};
export const mockVocabularyTitles = () => ({
  useVocabularyItem: (type, id) => fakeVocabulary[`${type}/${id}`] ?? {},
  useVocabularyTitle: (type, id) => fakeVocabulary[`${type}/${id}`]?.title,
  rememberItem: (type, id, item) => {
    if (!type || !id) return;
    fakeVocabulary[`${type}/${id}`] = {
      ...(fakeVocabulary[`${type}/${id}`] ?? {}),
      ...item,
    };
  },
  rememberTitle: () => {},
});

// A pick suggestion per vocabulary name, in the real
// serializeVocabularySuggestions shape ({ id, title_l10n, custom_fields }),
// for the mockVocabularyField() pick button.
let vocabularyPicks = {};
export const setFakeVocabularyPicks = (picks) => {
  vocabularyPicks = picks ?? {};
};

// A fake for MbdbVocabularyField, mirroring what a block needs
// from the real wrapper: the fieldPath, the value it shows, the label slot, the
// merged field error, a pick that writes { id } and calls onPicked (the real
// onValueChange — seed the item cache with setFakeVocabulary()), and the
// manual-addition trigger. Use it as:
//   jest.mock("…/MbdbVocabularyField", () =>
//     jest.requireActual("…/testUtils").mockVocabularyField()
//   );
const FakeMbdbVocabularyField = ({
  fieldPath,
  vocabularyName,
  label,
  onPicked,
  onAddition,
}) => {
  const { values, setFieldValue } = useFormikContext();
  const { messages } = useFieldErrors(fieldPath);
  const v = getIn(values, fieldPath);
  const shown = v?.id ?? v?.title?.en ?? "";
  const pick = vocabularyPicks[vocabularyName];
  return (
    <div data-testid="picker" data-path={fieldPath} data-value={shown}>
      <span data-testid="picker-value">{shown}</span>
      <span data-testid="picker-label">{label}</span>
      {messages.length > 0 && (
        <span data-testid="picker-error">{messages.join(" ")}</span>
      )}
      {pick && (
        <button
          type="button"
          data-testid="pick"
          onClick={() => {
            setFieldValue(fieldPath, { id: pick.id });
            onPicked?.(pick);
          }}
        />
      )}
      {onAddition && (
        <button
          type="button"
          data-testid="enter-manually"
          onClick={() => onAddition("my custom lipid mix")}
        />
      )}
    </div>
  );
};
FakeMbdbVocabularyField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  vocabularyName: PropTypes.string,
  onPicked: PropTypes.func,
  onAddition: PropTypes.func,
  label: PropTypes.node,
};
export const mockVocabularyField = () => ({
  MbdbVocabularyField: FakeMbdbVocabularyField,
});

// --- render helper --------------------------------------------------------

// Render `ui` inside a real Formik (enableReinitialize, like the deposit
// form) into a fresh container appended to document.body. helpMode wraps the
// tree in HelpModeProvider. Returns the container; pass it to unmountForm.
//
// Options:
// - withUnrelatedField: also renders, after `ui`, a formik Field named
//   "unrelatedTestField" (data-testid="unrelated-field") for the
//   errors-stay-after-an-unrelated-edit pattern (editUnrelatedField). Opt-in,
//   so existing querySelector("input") tests are not affected.
// - onSetFieldValue(fn): wraps `ui` so fn is called on every formik
//   setFieldValue (a spy for "no write on …" tests).
export const renderInForm = (
  ui,
  {
    initialValues = {},
    initialErrors = {},
    uiModel,
    helpMode,
    withUnrelatedField = false,
    onSetFieldValue,
  } = {}
) => {
  if (uiModel !== undefined) setFakeUiModel(uiModel);
  if (onSetFieldValue !== undefined)
    ui = <SetFieldValueSpy fn={onSetFieldValue}>{ui}</SetFieldValueSpy>;
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
        <HelpModeProvider mode={helpMode}>
          {ui}
          {withUnrelatedField && (
            <Field name="unrelatedTestField" data-testid="unrelated-field" />
          )}
        </HelpModeProvider>
      ) : (
        <>
          {ui}
          {withUnrelatedField && (
            <Field name="unrelatedTestField" data-testid="unrelated-field" />
          )}
        </>
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

// --- renderInForm options -----------------------------------

// Wraps `ui` so callers can spy on Formik's setFieldValue: it reads the real
// formik context and re-provides it through FormikProvider with a
// setFieldValue that reports to `fn` and then delegates.
const SetFieldValueSpy = ({ fn, children }) => {
  const formik = useFormikContext();
  const wrapped = {
    ...formik,
    setFieldValue: (...a) => {
      fn(...a);
      return formik.setFieldValue(...a);
    },
  };
  return <FormikProvider value={wrapped}>{children}</FormikProvider>;
};
SetFieldValueSpy.propTypes = {
  fn: PropTypes.func.isRequired,
  children: PropTypes.node,
};

// --- model YAML enum reading ------------------------------------

// Walks up from this file's real path (Jest may load it through the assets
// symlink) to the repository's models/ folder.
export const modelYamlPath = () => {
  let dir = fs.realpathSync(__dirname);
  while (dir !== path.dirname(dir)) {
    const p = path.join(
      dir,
      "models",
      "general_parameters-definitions-rdm.yaml"
    );
    if (fs.existsSync(p)) return p;
    dir = path.dirname(dir);
  }
  throw new Error(`model YAML not found above ${__dirname}`);
};

// The lines of a top-level `Type:` block in the model YAML (until the next
// line that starts at column 0).
const typeBlock = (typeName) => {
  const lines = fs.readFileSync(modelYamlPath(), "utf8").split("\n");
  const start = lines.findIndex((l) => l === `${typeName}:`);
  if (start === -1)
    throw new Error(`type not found in model YAML: ${typeName}`);
  let end = lines.length;
  for (let i = start + 1; i < lines.length; i += 1) {
    if (lines[i] !== "" && !/^\s/.test(lines[i])) {
      end = i;
      break;
    }
  }
  return lines.slice(start + 1, end);
};

// Enum of a top-level type (`yamlEnum("LENGTH_UNITS")`) or of a property of a
// top-level type (`yamlEnum("Size", "type")`). Text parsing of the model's
// fixed layout: `<Type>:` at column 0, properties at 4 spaces, `enum:` then
// `- value` lines. Strips surrounding quotes; throws when nothing is found.
export const yamlEnum = (typeName, property) => {
  let block = typeBlock(typeName);
  if (property !== undefined) {
    const propIdx = block.findIndex((l) => l === `    ${property}:`);
    if (propIdx === -1)
      throw new Error(`property not found on ${typeName}: ${property}`);
    // The property block ends at the next line at the property indent (4 sp).
    let propEnd = block.length;
    for (let i = propIdx + 1; i < block.length; i += 1) {
      const l = block[i];
      if (l !== "" && /^ {4}\S/.test(l)) {
        propEnd = i;
        break;
      }
    }
    block = block.slice(propIdx + 1, propEnd);
  }
  const enumIdx = block.findIndex((l) => /^\s+enum:\s*$/.test(l));
  if (enumIdx === -1)
    throw new Error(
      `enum not found on ${typeName}${property ? "." + property : ""}`
    );
  const values = [];
  for (let i = enumIdx + 1; i < block.length; i += 1) {
    const m = /^\s+-\s+(.*)$/.exec(block[i]);
    if (!m) break; // first non-`- …` line ends the enum list
    values.push(m[1].trim().replace(/^["']|["']$/g, ""));
  }
  if (values.length === 0)
    throw new Error(
      `empty enum on ${typeName}${property ? "." + property : ""}`
    );
  return values;
};

// True when `typeName` declares a top-level property `name` (a `    name:`
// line). The property sibling of yamlEnum, for group paths that carry no enum.
export const yamlProperty = (typeName, name) =>
  typeBlock(typeName).some((l) => l === `    ${name}:`);

// --- value probe ------------------------------------------------

// Renders the formik value at `path` as JSON so tests assert stored data, not
// DOM. Renders `null` when the value is absent (undefined), so `readProbe`
// parses `null` there.
export const ValueProbe = ({ path }) => {
  const { values } = useFormikContext();
  return (
    <pre data-testid="value-probe">
      {JSON.stringify(getIn(values, path) ?? null)}
    </pre>
  );
};
ValueProbe.propTypes = { path: PropTypes.string.isRequired };

// JSON.parse of ValueProbe's <pre>; `null` when the value (or probe) is absent.
export const readProbe = (container) => {
  const pre = container.querySelector('[data-testid="value-probe"]');
  return pre ? JSON.parse(pre.textContent) : null;
};

// --- event helpers -------------------------------------------

// Simulate an input `change` to `value`. Sets the DOM value first so Semantic
// wrapped inputs (which read event.target.value, not the Simulate payload)
// see the new value, then fires the change with the payload so plain
// React-controlled inputs work too. Flushes one macrotask before and after:
// the flush BEFORE lets a pending render land so the input event sees a
// current DOM; the flush AFTER lets Formik's setFieldValue → validation promise
// resolve. Both are needed because formik's state/validation settle in promise
// ticks, not synchronously with the simulated event.
export const typeInto = async (element, value) => {
  element.value = value;
  await act(async () => {
    await new Promise((r) => setTimeout(r, 0));
    Simulate.change(element, { target: { value } });
    await new Promise((r) => setTimeout(r, 0));
  });
};

// Simulate a click, with the same two-tick flush as typeInto: React's render
// from any prior event lands first, then formik's post-click update settles.
export const clickOn = async (element) => {
  await act(async () => {
    await new Promise((r) => setTimeout(r, 0));
    Simulate.click(element);
    await new Promise((r) => setTimeout(r, 0));
  });
};

// Pick an option from a Semantic dropdown block. SelectField passes
// id={fieldPath} to the dropdown and Semantic renders its menu inside that
// same element, so an item click works without opening the dropdown first.
export const pickDropdown = async (fieldPath, optionText) => {
  const dd = document.getElementById(fieldPath);
  if (!dd) throw new Error(`dropdown not found: ${fieldPath}`);
  const item = [...dd.querySelectorAll(".menu .item")].find(
    (el) => el.textContent.trim() === optionText
  );
  if (!item) throw new Error(`option not found: ${optionText} in ${fieldPath}`);
  await clickOn(item);
};

// Types "x" into the unrelated field rendered by the withUnrelatedField option.
// The timer after the change is needed because Formik's validation —
// which resets `errors` to {} — resolves in a promise AFTER the change. By the
// time this returns, that reset has settled, so a surviving message is the
// merged-initialErrors fallback, not a stale `errors` node.
export const editUnrelatedField = async (container) => {
  const field = container.querySelector('[data-testid="unrelated-field"]');
  if (!field) throw new Error("no unrelatedTestField; pass withUnrelatedField");
  await typeInto(field, "x");
};
