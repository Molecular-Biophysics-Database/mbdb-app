import React from "react";
import PropTypes from "prop-types";
import { ArrayField as RifArrayField } from "react-invenio-forms";
import { StringArrayField as OARepoStringArrayField } from "@js/oarepo_ui/forms";
import {
  Dropdown,
  Input,
  TextArea,
  HelpLabel,
  useHelpMode,
} from "mbdb-semantic-ui-react";
import {
  useFieldBinding,
  useModelFieldData,
} from "@js/mbdb/forms/building-blocks/fieldData";
import { useOwnErrorMessages } from "@js/mbdb/forms/building-blocks/errors";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import { toOption } from "@js/mbdb/forms/building-blocks/options";

// mbdb wrappers around react-invenio-forms fields: they fill label /
// helpText / required from the model via useFieldBinding (explicit props
// win) and render the one FieldShell frame, whose two help slots are the
// only place where the look of help texts can change. FieldHelp decides
// per global help mode: in "invenio" mode it renders the helptext label
// below the field, in "popup" mode it renders nothing (the "?" icon sits
// in the label instead). The wrapped components' own helpText rendering is
// suppressed. The wrappers also force a controlled input value and map the
// empty string to unset, so cleared fields are removed from the form data
// instead of persisting "" ("" / null / undefined → absent key, guide §7).
//
// Prop order (guide §8: wrappers spread the caller's props first and set
// their own last): `{...uiProps}` comes FIRST and the wrapper's `label`,
// `required`, `helpText`, `onChange`, `value` come AFTER it, so a caller's
// stray `helpText` (the old prop name) cannot undo the suppression.
//
// Every wrapper renders ONE root element — the shell's `Form.Field` — with
// label, control, ErrorMessages and FieldHelp inside it. A fragment would let
// Form.Group columns put the help text into a column of its own.

const fieldShape = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  help: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  required: PropTypes.bool,
  // own onChange (e.g. NumberField) wins over the wrapper's default
  onChange: PropTypes.func,
};

// Semantic Input onChange carries the value as `data.value`; a Form.Input
// without an intermediary control (e.g. clear) reports `e.target.value`.
const eventValue = (e, data) => data?.value ?? e.target.value;

// A stored value that is not in `options` stays visible as an extra option
// (RIF stores it through ensureSelectedValuesInOptions); the block-level
// SelectField then flags it with its "Unknown value" label too. Options
// coming in as plain strings are normalized FIRST, so the current value is
// not appended a second time as a phantom `{key,value,text}` clone.
const optionsWithCurrentValue = (options, value) => {
  const normalized = options.map(toOption);
  const valueIsKnown =
    value !== undefined &&
    value !== "" &&
    normalized.some((option) => option.value === value);
  if (!valueIsKnown && value !== undefined && value !== "")
    return [...normalized, { key: value, value, text: String(value) }];
  return normalized;
};

// Text wrapper, rebuilt on FieldShell + plain Semantic Input. Errors come
// from the binding (useFieldErrors semantics), so they clear once the
// value is edited — RIF's own error label is not used. onChange: "" unsets
// (the pruning setter); a caller's own onChange (NumberField) replaces the
// default write entirely.
export const TextField = ({
  fieldPath,
  label,
  help,
  required,
  onChange,
  error,
  width,
  ...uiProps
}) => {
  const f = useFieldBinding(fieldPath, { label, help, required });
  // `error` overrides the hook state: a boolean marks the field red; a string
  // is shown as the message (used by callers whose server errors sit on a
  // neighbouring parent, e.g. i18n dicts on `title` vs `title.en`).
  const hasError = error !== undefined ? !!error : f.hasError;
  const messages =
    typeof error === "string" ? [error, ...f.messages] : f.messages;
  return (
    <FieldShell
      inputId={fieldPath}
      label={f.label}
      help={f.help}
      required={f.required}
      hasError={hasError}
      messages={messages}
      width={width}
    >
      <Input
        {...uiProps}
        id={fieldPath}
        name={fieldPath}
        fluid={uiProps.fluid ?? true}
        error={hasError || undefined}
        value={f.value ?? ""}
        onBlur={f.onBlur}
        onChange={onChange ?? ((e, d) => f.setValue(eventValue(e, d)))}
      />
    </FieldShell>
  );
};
TextField.propTypes = {
  ...fieldShape,
  width: PropTypes.number,
  error: PropTypes.oneOfType([PropTypes.bool, PropTypes.string]),
};

// Select wrapper, rebuilt on FieldShell + plain Semantic Dropdown. The
// clear icon unsets, and a stored value outside `options` stays visible
// (RIF's ensureSelectedValuesInOptions is recreated here so old data never
// disappears into the placeholder). Optional selects are clearable by
// default; a required one is not.
export const SelectField = ({
  fieldPath,
  label,
  help,
  required,
  onChange,
  width,
  clearable,
  ...uiProps
}) => {
  const f = useFieldBinding(fieldPath, { label, help, required });
  const options = optionsWithCurrentValue(uiProps.options ?? [], f.value);
  return (
    <FieldShell
      inputId={fieldPath}
      label={f.label}
      help={f.help}
      required={f.required}
      hasError={f.hasError}
      messages={f.messages}
      width={width}
    >
      <Dropdown
        {...uiProps}
        id={fieldPath}
        fluid
        search
        selection
        selectOnBlur={false}
        clearable={clearable !== undefined ? clearable : !f.required}
        error={f.hasError || undefined}
        options={options}
        value={f.value ?? ""}
        onBlur={f.onBlur}
        onChange={onChange ?? ((e, { value: next }) => f.setValue(next))}
      />
    </FieldShell>
  );
};
SelectField.propTypes = {
  ...fieldShape,
  width: PropTypes.number,
  clearable: PropTypes.bool,
};

export const ArrayField = ({
  fieldPath,
  label,
  help,
  required,
  ...uiProps
}) => {
  // Not the shell: RIF's ArrayField renders the whole block (label, rows,
  // Add button) and takes helpText as a prop — this wrapper only feeds the
  // resolved model data in, so it keeps calling useModelFieldData directly.
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // RIF renders helpText inside the Form.Field directly under the label,
  // above the rows — where the design wants it. In "invenio" mode pass it
  // there (not below the Add button); in "popup" mode the icon lives
  // in HelpLabel and nothing renders below. This is the one wrapper that
  // reads the mode itself.
  const mode = useHelpMode();
  return (
    <RifArrayField
      {...uiProps}
      fieldPath={fieldPath}
      // RIF renders label through its FieldLabel (inside a real <label>)
      label={<HelpLabel label={data.label} help={data.helpText} />}
      required={data.required}
      helpText={mode === "invenio" ? data.helpText : undefined}
    />
  );
};
ArrayField.propTypes = fieldShape;

// Textarea wrapper, rebuilt on FieldShell + plain Semantic TextArea (no
// RIF). RIF's TextAreaField always renders its ErrorLabel, which shows
// `get(errors) || get(initialErrors)` forever with no "value changed"
// check, and never marks the field red. The binding's errors (errors.js
// helper) clear once the value at fieldPath is edited. onBlur chains
// Formik's handleBlur (marks touched) and then the caller's onBlur. The
// wrapper keeps the controlled value and maps "" to unset.
export const TextAreaField = ({
  fieldPath,
  label,
  help,
  required,
  onChange,
  onBlur,
  // drop the old prop name: it would otherwise flow through uiProps onto the
  // DOM <textarea>; help goes through `help` → HelpLabel/FieldHelp only
  helpText, // eslint-disable-line no-unused-vars
  autoHeight: _autoHeight, // eslint-disable-line no-unused-vars -- consumed by the block (rows computed there); drop so it never reaches the DOM
  children,
  ...uiProps
}) => {
  const f = useFieldBinding(fieldPath, { label, help, required });
  // className goes on the shell's Form.Field: Semantic's TextArea would land
  // it on the <textarea> itself, breaking descendant class styling (e.g.
  // `.mbdb-monospace textarea`) and the "one root element" structure.
  const { className, ...restUiProps } = uiProps;
  return (
    <FieldShell
      inputId={fieldPath}
      label={f.label}
      help={f.help}
      required={f.required}
      hasError={f.hasError}
      messages={f.messages}
      className={className}
    >
      <TextArea
        {...restUiProps}
        id={fieldPath}
        name={fieldPath}
        value={f.value ?? ""}
        onChange={(e, d) => {
          // a caller's own onChange takes over the write entirely
          if (onChange) {
            onChange(e, d);
            return;
          }
          f.setValue(d?.value ?? e.target.value);
        }}
        onBlur={(e, d) => {
          f.onBlur(e);
          onBlur?.(e, d);
        }}
      />
      {children}
    </FieldShell>
  );
};
TextAreaField.propTypes = {
  ...fieldShape,
  onBlur: PropTypes.func,
  // rendered inside the shell, between the control and the error messages
  // (e.g. the block's link buttons); never a sibling column
  children: PropTypes.node,
};

// Wrapper around oarepo's StringArrayField. oarepo's component resolves the
// label through its own useFieldData and renders its own help as a helptext
// label between the rows and the Add button; helpText={null} suppresses
// it there (oarepo's mergeFieldData keeps null overrides). The mbdb
// wrapper puts the resolved label/help into the shell's label slot
// (oarepo labels from its own field data, which must not see the caller's
// label/help), and renders the list-level message plus the help through
// the shell like every other field.
export const StringArrayField = ({
  fieldPath,
  label,
  help,
  required,
  ...uiProps
}) => {
  const f = useFieldBinding(fieldPath, { label, help, required });
  // oarepo's component shows item-level errors but never falls back to
  // initialErrors for a string error at the list path itself (its own error
  // read is Formik errors-only), so the list-level message is rendered here
  // from the shared merge, after the items — same place as the siblings.
  const ownMessages = useOwnErrorMessages(fieldPath);
  return (
    // One root for the whole block: oarepo's component renders its own
    // inner field structure; the shell's FieldHelp still reads the mode and
    // sits inside the same column, never a sibling of the control.
    <FieldShell
      label={f.label}
      help={f.help}
      required={f.required}
      messages={ownMessages}
      className="mbdb-field-wrapper"
      // the list plus its Add button is composite: help goes under the label,
      // not under the button where Invenio's negative margin hides it
      helpPlacement="label"
      // do not tint the whole list when one row has an error — the rows are
      // ways of normal inputs; the list-level message goes through
      // ErrorMessages, never by making the wrapper `.field.error`
      markError={false}
    >
      <OARepoStringArrayField
        {...uiProps}
        fieldPath={fieldPath}
        // the shell's own label is the only visible one; `null` overrules
        // the model label in oarepo's merge (undefined would leave theirs
        // in place, duplicating the shell's label)
        label={null}
        required={null}
        helpText={null}
      />
    </FieldShell>
  );
};
StringArrayField.propTypes = fieldShape;
