import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  TextField as RifTextField,
  SelectField as RifSelectField,
  ArrayField as RifArrayField,
} from "react-invenio-forms";
import { StringArrayField as OARepoStringArrayField } from "@js/oarepo_ui/forms";
import {
  Form,
  TextArea,
  FieldHelp,
  HelpLabel,
  useHelpMode,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useFieldErrors } from "@js/mbdb/forms/building-blocks/errors";
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

export const TextField = ({
  fieldPath,
  label,
  help,
  required,
  onChange,
  ...uiProps
}) => {
  const { values, setFieldValue } = useFormikContext();
  // The hook keeps helpText because that is the model's key (getFieldData);
  // the wrapper's public prop is `help`.
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  return (
    <>
      <RifTextField
        {...uiProps}
        fieldPath={fieldPath}
        // semantic-ui passing label shorthand through Form.Input drops the
        // <label> element for node values, so wrap HelpLabel ourselves
        label={
          <label htmlFor={fieldPath}>
            <HelpLabel label={data.label} help={data.helpText} />
          </label>
        }
        required={data.required}
        helpText={undefined}
        // RIF spreads uiProps after `field`/onChange, so these override;
        // a caller's own onChange (e.g. NumberField) wins over the default
        onChange={
          onChange ??
          ((e, onChangeData) => {
            const v = eventValue(e, onChangeData);
            if (v === "") unsetFieldValue(values, setFieldValue, fieldPath);
            else setFieldValue(fieldPath, v);
          })
        }
        value={getIn(values, fieldPath) ?? ""}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
TextField.propTypes = fieldShape;

export const SelectField = ({
  fieldPath,
  label,
  help,
  required,
  onChange,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  return (
    <>
      <RifSelectField
        {...uiProps}
        fieldPath={fieldPath}
        // RIF puts the label inside its semantic Label shorthand ({children:
        // label}), whose createHTMLLabel renders a real <label> element
        label={<HelpLabel label={data.label} help={data.helpText} />}
        required={data.required}
        helpText={undefined}
        // RIF pitfall: a custom onChange must set the value itself; the
        // clear icon passes "" which would persist an empty string.
        onChange={
          onChange ??
          (({ data: selectData, formikProps }) => {
            if (selectData.value === "")
              unsetFieldValue(
                formikProps.form.values,
                formikProps.form.setFieldValue,
                fieldPath
              );
            else formikProps.form.setFieldValue(fieldPath, selectData.value);
          })
        }
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
SelectField.propTypes = fieldShape;

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
  return (
    <Form.Field error={hasError || undefined} required={data.required}>
      {data.label && (
        <label htmlFor={fieldPath}>
          <HelpLabel label={data.label} help={data.helpText} />
        </label>
      )}
      <TextArea
        {...uiProps}
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
      <FieldHelp help={data.helpText} />
    </Form.Field>
  );
};
TextAreaField.propTypes = { ...fieldShape, onBlur: PropTypes.func };

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
  return (
    <>
      <OARepoStringArrayField
        {...uiProps}
        fieldPath={fieldPath}
        label={<HelpLabel label={data.label} help={data.helpText} />}
        required={data.required}
        helpText={null}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
StringArrayField.propTypes = fieldShape;
