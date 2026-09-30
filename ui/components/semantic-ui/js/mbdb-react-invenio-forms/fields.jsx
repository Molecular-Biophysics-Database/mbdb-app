import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  TextField as RifTextField,
  SelectField as RifSelectField,
  ArrayField as RifArrayField,
  TextAreaField as RifTextAreaField,
} from "react-invenio-forms";
import { FieldHelp, FIELD_HELP_MODE } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// mbdb wrappers around react-invenio-forms fields: they fill label /
// helpText / required from the model (explicit props win) and render
// helpText through FieldHelp, so this is the only place where the look
// of help texts can change. The RIF components render helpText as their
// own <label className="helptext">; in "invenio" mode the wrappers pass
// undefined to suppress it and render FieldHelp after the field instead;
// in "popup" mode the help icon goes into the label and nothing renders
// below. The wrappers also force a controlled input value and map the
// empty string to `undefined`, so cleared fields are removed from the
// form data instead of persisting "".

const fieldShape = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  helpText: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  required: PropTypes.bool,
  // own onChange (e.g. NumberField) wins over the wrapper's default
  onChange: PropTypes.func,
};

// Invenio mode: help under the field via FieldHelp.
// Popup mode: help icon inside the label node (FieldHelp renders nothing
// below; note: the popup trigger in FieldHelp.jsx needs tabIndex + focus).
const helpLabel = (data) =>
  FIELD_HELP_MODE === "popup" && data.helpText ? (
    <>
      {data.label} <FieldHelp help={data.helpText} mode="popup" />
    </>
  ) : (
    data.label
  );

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
        label={helpLabel(data)}
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
      {FIELD_HELP_MODE !== "popup" && <FieldHelp help={data.helpText} />}
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
        label={helpLabel(data)}
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
      {FIELD_HELP_MODE !== "popup" && <FieldHelp help={data.helpText} />}
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
  // above the rows. In "invenio" mode pass it there (F2: not below the
  // Add button); in "popup" mode compose the icon into the label instead.
  return (
    <RifArrayField
      fieldPath={fieldPath}
      label={helpLabel(data)}
      required={data.required}
      helpText={FIELD_HELP_MODE === "popup" ? undefined : data.helpText}
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
        label={helpLabel(data)}
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
      {FIELD_HELP_MODE !== "popup" && <FieldHelp help={data.helpText} />}
    </>
  );
};
TextAreaField.propTypes = fieldShape;
