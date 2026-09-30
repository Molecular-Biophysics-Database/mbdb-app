import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  TextField as RifTextField,
  SelectField as RifSelectField,
  ArrayField as RifArrayField,
  TextAreaField as RifTextAreaField,
} from "react-invenio-forms";
import { StringArrayField as OARepoStringArrayField } from "@js/oarepo_ui/forms";
import { FieldHelp, HelpLabel, useHelpMode } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

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

const fieldShape = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  helpText: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
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
  helpText,
  required,
  onChange,
  ...uiProps
}) => {
  const { values, setFieldValue } = useFormikContext();
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <RifTextField
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
        {...uiProps}
        // RIF spreads uiProps after `field`/onChange, so these override;
        // a caller's own onChange (e.g. NumberField) wins over the default
        onChange={
          onChange ??
          ((e, onChangeData) =>
            setFieldValue(
              fieldPath,
              eventValue(e, onChangeData) === ""
                ? undefined
                : eventValue(e, onChangeData)
            ))
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
  helpText,
  required,
  onChange,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <RifSelectField
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
          (({ data: selectData, formikProps }) =>
            formikProps.form.setFieldValue(
              fieldPath,
              selectData.value === "" ? undefined : selectData.value
            ))
        }
        {...uiProps}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
SelectField.propTypes = fieldShape;

export const ArrayField = ({
  fieldPath,
  label,
  helpText,
  required,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  // RIF renders helpText inside the Form.Field directly under the label,
  // above the rows — where the design wants it. In "invenio" mode pass it
  // there (F2: not below the Add button); in "popup" mode the icon lives
  // in HelpLabel and nothing renders below. This is the one wrapper that
  // reads the mode itself.
  const mode = useHelpMode();
  return (
    <RifArrayField
      fieldPath={fieldPath}
      // RIF renders label through its FieldLabel (inside a real <label>)
      label={<HelpLabel label={data.label} help={data.helpText} />}
      required={data.required}
      helpText={mode === "invenio" ? data.helpText : undefined}
      {...uiProps}
    />
  );
};
ArrayField.propTypes = fieldShape;

// RIF TextAreaField renders no helptext itself (RIF passes uiProps to
// Form.TextArea, whose `label` lands in the field's FormField). The
// wrapper only appends FieldHelp and fixes the onChange/value handling
// (RIF passes form.handleChange and a raw getIn value otherwise).
// Note: unlike RIF TextField/SelectField, RIF TextAreaField has no
// helpText exclusion, so helpText must NOT be forwarded at all — it
// would land on the DOM <textarea>.
export const TextAreaField = ({
  fieldPath,
  label,
  helpText,
  required,
  onChange,
  ...uiProps
}) => {
  const { values, setFieldValue } = useFormikContext();
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <RifTextAreaField
        fieldPath={fieldPath}
        // like RifTextField: semantic Form.TextArea drops the <label>
        // element for node labels, so wrap HelpLabel ourselves
        label={
          <label htmlFor={fieldPath}>
            <HelpLabel label={data.label} help={data.helpText} />
          </label>
        }
        required={data.required}
        {...uiProps}
        onChange={
          onChange ??
          ((e, onChangeData) =>
            setFieldValue(
              fieldPath,
              eventValue(e, onChangeData) === ""
                ? undefined
                : eventValue(e, onChangeData)
            ))
        }
        value={getIn(values, fieldPath) ?? ""}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
TextAreaField.propTypes = fieldShape;

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
  helpText,
  required,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <OARepoStringArrayField
        fieldPath={fieldPath}
        label={<HelpLabel label={data.label} help={data.helpText} />}
        required={data.required}
        helpText={null}
        {...uiProps}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
StringArrayField.propTypes = fieldShape;
