import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { ArrayField as RifArrayField } from "react-invenio-forms";
import { StringArrayField as OARepoStringArrayField } from "@js/oarepo_ui/forms";
import {
  Dropdown,
  Form,
  Input,
  TextArea,
  FieldHelp,
  HelpLabel,
  useHelpMode,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { ErrorMessages } from "@js/mbdb/forms/building-blocks/ErrorMessages";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";

// mbdb wrappers around react-invenio-forms fields: they fill label /
// helpText / required from the model (explicit props win) and render
// helpText through the two help slots (HelpLabel in the label, FieldHelp
// under the field), so this is the only place where the look of help
// texts can change. FieldHelp decides per global help mode: in "invenio"
// mode it renders the helptext label below the field, in "popup" mode it
// renders nothing (the "?" icon sits in the label instead). The RIF
// components' own helpText rendering is suppressed. The wrappers also
// force a controlled input value and map the empty string to `undefined`,
// so cleared fields are removed from the form data instead of persisting "".
//
// Prop order (guide §8: wrappers spread the caller's props first and set
// their own last): `{...uiProps}` comes FIRST and the wrapper's `label`,
// `required`, `helpText`, `onChange`, `value` come AFTER it, so a caller's
// stray `helpText` (the old prop name) cannot undo the suppression.

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
// (RIF stores it through ensureSelectedValuesInOptions). Without this the
// dropdown would show the placeholder and silently mislead the user about
// stored data we never touch ourselves.
const optionsWithCurrentValue = (options, value) => {
  if (
    value !== undefined &&
    value !== "" &&
    !options.some((option) => option.value === value)
  )
    return [...options, { key: value, value, text: String(value) }];
  return options;
};

// 1R-pass-3 / D8 (AliasPackages P4-F1): every wrapper renders ONE root
// element — the field's `Form.Field` — with label, control, ErrorMessages and
// FieldHelp inside it. A fragment (control + FieldHelp) would let Form.Group
// columns put the help text into its own column.

// The label slot, shared by all four wrappers: a real <label> holding the
// HelpLabel (model label + optional ? icon inside).
const FieldLabel = ({ fieldPath, label, help }) =>
  label ? (
    <label htmlFor={fieldPath}>
      <HelpLabel label={label} help={help} />
    </label>
  ) : null;
FieldLabel.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.node,
  help: PropTypes.node,
};

// Text wrapper, rebuilt on plain Form.Field + Input (no RIF). RIF's TextField
// merges help and field on the same returns-a-fragment level as a sibling
// before D8. Errors come from useFieldErrors (the errors.js semantics), so
// they clear once the value is edited — RIF's own error label is not used.
// onChange: "" unsets (C15 pruning); a caller's own onChange (NumberField)
// replaces the default write entirely.
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
  const { values, setFieldValue } = useFormikContext();
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const { hasError: hookHasError, messages } = useFieldErrors(fieldPath);
  // `error` overrides the hook state: a boolean marks the field red; a string
  // is shown as the message (used by callers whose server errors sit on a
  // neighbouring parent, e.g. i18n dicts on `title` vs `title.en`).
  const hasError = error !== undefined ? !!error : hookHasError;
  const errorText = typeof error === "string" ? error : undefined;
  return (
    <Form.Field
      error={hasError || undefined}
      required={data.required}
      width={width}
    >
      <FieldLabel
        fieldPath={fieldPath}
        label={data.label}
        help={data.helpText}
      />
      <Input
        {...uiProps}
        id={fieldPath}
        name={fieldPath}
        fluid={uiProps.fluid ?? true}
        error={hasError || undefined}
        value={getIn(values, fieldPath) ?? ""}
        onChange={
          onChange ??
          ((e, onChangeData) => {
            const v = eventValue(e, onChangeData);
            if (v === "") unsetFieldValue(values, setFieldValue, fieldPath);
            else setFieldValue(fieldPath, v);
          })
        }
      />
      <ErrorMessages
        messages={errorText ? [errorText, ...messages] : messages}
      />
      <FieldHelp help={data.helpText} />
    </Form.Field>
  );
};
TextField.propTypes = {
  ...fieldShape,
  width: PropTypes.number,
  error: PropTypes.oneOfType([PropTypes.bool, PropTypes.string]),
};

// Select wrapper, rebuilt on plain Form.Field + Dropdown. Errors come from
// useFieldErrors, the clear icon writes `unset` through the pruning helper,
// and a stored value outside `options` stays visible (RIF's
// ensureSelectedValuesInOptions is recreated here so old data never
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
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const { values, setFieldValue } = useFormikContext();
  const { hasError, messages } = useFieldErrors(fieldPath);
  const value = getIn(values, fieldPath);
  const options = optionsWithCurrentValue(uiProps.options ?? [], value);
  return (
    <Form.Field
      error={hasError || undefined}
      required={data.required}
      width={width}
    >
      <FieldLabel
        fieldPath={fieldPath}
        label={data.label}
        help={data.helpText}
      />
      <Dropdown
        {...uiProps}
        id={fieldPath}
        fluid
        search
        selection
        selectOnBlur={false}
        clearable={clearable !== undefined ? clearable : !data.required}
        error={hasError || undefined}
        options={options}
        value={value ?? ""}
        onChange={
          onChange ??
          ((e, { value: next }) => {
            if (next === "" || next === undefined)
              unsetFieldValue(values, setFieldValue, fieldPath);
            else setFieldValue(fieldPath, next);
          })
        }
      />
      <ErrorMessages messages={messages} />
      <FieldHelp help={data.helpText} />
    </Form.Field>
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
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // RIF renders helpText inside the Form.Field directly under the label,
  // above the rows — where the design wants it. In "invenio" mode pass it
  // there (F2: not below the Add button); in "popup" mode the icon lives
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

// Textarea wrapper, rebuilt on plain Form.Field + TextArea (no RIF). RIF's
// TextAreaField always renders its ErrorLabel, which shows
// `get(errors) || get(initialErrors)` forever with no "value changed" check,
// and never marks the field red. This rebuilds reads errors through the
// errors.js helper (useFieldErrors): the message clears once the value at
// fieldPath is edited, and Form.Field gets `error`. onBlur chains Formik's
// handleBlur (marks touched) and then the caller's onBlur. The wrapper keeps
// the controlled value and maps "" to unset.
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
  const { values, setFieldValue, handleBlur } = useFormikContext();
  // The hook keeps helpText because that is the model's key (getFieldData);
  // the wrapper's public prop is `help`.
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const { hasError, messages } = useFieldErrors(fieldPath);
  // className goes on the Form.Field: Semantic's TextArea would land it on
  // the <textarea> itself, breaking descendant class styling (e.g.
  // `.mbdb-monospace textarea`) and the "one root element" structure (D8).
  const { className, ...restUiProps } = uiProps;
  return (
    <Form.Field
      error={hasError || undefined}
      required={data.required}
      className={className}
    >
      {data.label && (
        <label htmlFor={fieldPath}>
          <HelpLabel label={data.label} help={data.helpText} />
        </label>
      )}
      <TextArea
        {...restUiProps}
        id={fieldPath}
        name={fieldPath}
        value={getIn(values, fieldPath) ?? ""}
        onChange={(e, d) => {
          // a caller's own onChange takes over the write entirely
          if (onChange) {
            onChange(e, d);
            return;
          }
          const v = d?.value ?? e.target.value;
          if (v === "") unsetFieldValue(values, setFieldValue, fieldPath);
          else setFieldValue(fieldPath, v);
        }}
        onBlur={(e, d) => {
          handleBlur(e);
          onBlur?.(e, d);
        }}
      />
      <ErrorMessages messages={messages} />
      {children}
      <FieldHelp help={data.helpText} />
    </Form.Field>
  );
};
TextAreaField.propTypes = {
  ...fieldShape,
  onBlur: PropTypes.func,
  // rendered inside the same Form.Field, between the error messages and the
  // help (e.g. the block's link buttons); never a sibling column
  children: PropTypes.node,
};

// Wrapper around oarepo's StringArrayField (the wrapper StringListField
// review question F1 asked about). oarepo's component resolves the label
// through its own useFieldData and renders its own help as a helptext
// label between the rows and the Add button; helpText={null} suppresses
// it there (oarepo's mergeFieldData keeps null overrides). The mbdb
// wrapper resolves label/help/required from the model the same way as the
// other wrappers, puts HelpLabel into the label prop (FieldLabel renders
// nodes), and appends FieldHelp after the field.
export const StringArrayField = ({
  fieldPath,
  label,
  help,
  required,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  // oarepo's component shows item-level errors but never falls back to
  // initialErrors for a string error at the list path itself (its own error
  // read is Formik errors-only), so the list-level message is rendered here
  // from the shared merge, next to the items — same place as the siblings.
  const { hasError } = useFieldErrors(fieldPath);
  const ownMessages = useOwnErrorMessages(fieldPath);
  return (
    // One root for the whole block (D8): oarepo's component renders its own
    // inner field structure; FieldHelp still reads the mode and sits inside
    // the same column, never a sibling of the control.
    <Form.Field
      required={data.required}
      error={hasError || undefined}
      className="mbdb-field-wrapper"
    >
      <OARepoStringArrayField
        {...uiProps}
        fieldPath={fieldPath}
        label={<HelpLabel label={data.label} help={data.helpText} />}
        required={data.required}
        helpText={null}
      />
      <ErrorMessages messages={ownMessages} />
      <FieldHelp help={data.helpText} />
    </Form.Field>
  );
};
StringArrayField.propTypes = fieldShape;
