import React, { useState } from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  Dropdown,
  Form,
  Input,
  Label,
  FieldHelp,
  HelpLabel,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";

// A measured quantity as one control: number input with the unit dropdown
// attached on its right. Writes `{ value, unit }` at fieldPath. The
// defaultUnit is shown pre-selected but written only together with a
// value, so an empty optional quantity stays absent. A unit picked before
// any value lives in local state only — never as a partial `{ unit }` —
// and clearing the value removes the whole object and resets the pick.
export const ValueUnitField = ({
  fieldPath,
  units,
  defaultUnit,
  label,
  help,
  required,
  ...uiProps
}) => {
  const { values, setFieldValue } = useFormikContext();
  // The hook keeps helpText because that is the model's key (getFieldData);
  // the block's public prop is `help`.
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const current = getIn(values, fieldPath) || {};
  // Unit chosen while the quantity is empty; written on the next value.
  const [pickedUnit, setPickedUnit] = useState(undefined);
  const unit = pickedUnit ?? current.unit ?? defaultUnit;

  // The object path itself can hold a message (required quantity missing);
  // value/unit hold the child validation messages.
  const objectMessages = useOwnErrorMessages(fieldPath);
  const valueMessages = useFieldErrors(`${fieldPath}.value`).messages;
  const unitMessages = useFieldErrors(`${fieldPath}.unit`).messages;
  const messages = [
    ...new Set([...objectMessages, ...valueMessages, ...unitMessages]),
  ];
  const hasError = messages.length > 0;

  const setValue = (raw) => {
    if (raw === "") {
      unsetFieldValue(values, setFieldValue, fieldPath);
      setPickedUnit(undefined);
      return;
    }
    const n = Number(raw);
    setFieldValue(fieldPath, {
      value: Number.isNaN(n) ? undefined : n,
      unit,
    });
  };

  const setUnit = (nextUnit) => {
    if (current.value !== undefined) {
      setFieldValue(fieldPath, { ...current, unit: nextUnit });
    }
    setPickedUnit(nextUnit);
  };

  return (
    <Form.Field required={data.required} error={hasError}>
      <label htmlFor={fieldPath}>
        <HelpLabel label={data.label} help={data.helpText} />
      </label>
      <Input
        {...uiProps}
        fluid
        id={fieldPath}
        type="number"
        step="any"
        value={current.value !== undefined ? current.value : ""}
        onChange={(e, { value }) => setValue(value)}
        label={
          <Dropdown
            aria-label="Unit"
            selectOnBlur={false}
            options={units.map((u) => ({ key: u, value: u, text: u }))}
            value={unit}
            onChange={(e, { value }) => setUnit(value)}
          />
        }
        labelPosition="right"
      />
      {messages.map((message) => (
        <Label key={message} basic color="red" pointing>
          {message}
        </Label>
      ))}
      <FieldHelp help={data.helpText} />
    </Form.Field>
  );
};

ValueUnitField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  units: PropTypes.arrayOf(PropTypes.string).isRequired,
  defaultUnit: PropTypes.string,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
};
