import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  Dropdown,
  Form,
  Input,
  Label,
  FieldHelp,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "../fieldData";

// A measured quantity as one control: number input with the unit dropdown
// attached on its right. Writes `{ value, unit }` at fieldPath. The
// defaultUnit is shown pre-selected but written only together with a
// value, so an empty optional quantity stays absent; clearing the value
// removes the object (unless the user explicitly picked a non-default
// unit, which is kept as user intent).
export const ValueUnitField = ({
  fieldPath,
  units,
  defaultUnit,
  label,
  helpText,
  required,
  ...uiProps
}) => {
  const { values, errors, setFieldValue } = useFormikContext();
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  const current = getIn(values, fieldPath) || {};
  const valueError = getIn(errors, `${fieldPath}.value`);
  const unitError = getIn(errors, `${fieldPath}.unit`);

  const setValue = (raw) => {
    if (raw === "") {
      if (current.unit === undefined || current.unit === defaultUnit) {
        setFieldValue(fieldPath, undefined);
      } else {
        setFieldValue(fieldPath, { unit: current.unit });
      }
      return;
    }
    const n = parseFloat(raw);
    setFieldValue(fieldPath, {
      value: Number.isNaN(n) ? raw : n,
      unit: current.unit !== undefined ? current.unit : defaultUnit,
    });
  };

  const setUnit = (unit) => {
    if (current.value !== undefined) {
      setFieldValue(fieldPath, { ...current, unit });
    } else if (unit === defaultUnit) {
      setFieldValue(fieldPath, undefined);
    } else {
      setFieldValue(fieldPath, { unit });
    }
  };

  return (
    <Form.Field required={data.required} error={!!(valueError || unitError)}>
      <label>{data.label}</label>
      <Input
        fluid
        type="number"
        step="any"
        value={current.value !== undefined ? current.value : ""}
        onChange={(e, { value }) => setValue(value)}
        label={
          <Dropdown
            selectOnBlur={false}
            options={units.map((u) => ({ key: u, value: u, text: u }))}
            value={current.unit !== undefined ? current.unit : defaultUnit}
            onChange={(e, { value }) => setUnit(value)}
          />
        }
        labelPosition="right"
        {...uiProps}
      />
      {valueError && (
        <Label basic color="red" pointing>
          {valueError}
        </Label>
      )}
      {unitError && (
        <Label basic color="red" pointing>
          {unitError}
        </Label>
      )}
      <FieldHelp help={data.helpText} />
    </Form.Field>
  );
};

ValueUnitField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  units: PropTypes.arrayOf(PropTypes.string).isRequired,
  defaultUnit: PropTypes.string,
  label: PropTypes.node,
  helpText: PropTypes.node,
  required: PropTypes.bool,
};
