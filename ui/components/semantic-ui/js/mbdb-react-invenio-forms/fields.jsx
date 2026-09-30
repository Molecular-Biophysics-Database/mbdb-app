import React from "react";
import PropTypes from "prop-types";
import {
  TextField as RifTextField,
  SelectField as RifSelectField,
  ArrayField as RifArrayField,
  TextAreaField as RifTextAreaField,
} from "react-invenio-forms";
import { FieldHelp } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

// mbdb wrappers around react-invenio-forms fields: they fill label /
// helpText / required from the model (explicit props win) and render
// helpText through FieldHelp, so this is the only place where the look
// of help texts can change. The RIF components render helpText as their
// own <label className="helptext">; the wrappers pass undefined to
// suppress it and render FieldHelp after the field instead.

const fieldShape = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  helpText: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  required: PropTypes.bool,
};

export const TextField = ({
  fieldPath,
  label,
  helpText,
  required,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <RifTextField
        fieldPath={fieldPath}
        label={data.label}
        required={data.required}
        helpText={undefined}
        {...uiProps}
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
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <RifSelectField
        fieldPath={fieldPath}
        label={data.label}
        required={data.required}
        helpText={undefined}
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
  return (
    <>
      <RifArrayField
        fieldPath={fieldPath}
        label={data.label}
        required={data.required}
        helpText={undefined}
        {...uiProps}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
ArrayField.propTypes = fieldShape;

// RIF TextAreaField renders no helptext itself (label goes through
// Form.TextArea sugar), so only FieldHelp is appended.
export const TextAreaField = ({
  fieldPath,
  label,
  helpText,
  required,
  ...uiProps
}) => {
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  return (
    <>
      <RifTextAreaField
        fieldPath={fieldPath}
        label={data.label}
        required={data.required}
        {...uiProps}
      />
      <FieldHelp help={data.helpText} />
    </>
  );
};
TextAreaField.propTypes = fieldShape;
