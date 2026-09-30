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

// Unique message strings under an error node: strings plus OARepo
// { message, severity } objects (never rendered raw). Local clone of
// errors.js errorMessages; for the C1-aware source below.
const messagesOf = (node, out = []) => {
  if (node === undefined || node === null || node === "") return out;
  if (typeof node === "string") {
    if (!out.includes(node)) out.push(node);
  } else if (Array.isArray(node)) {
    node.forEach((child) => messagesOf(child, out));
  } else if (typeof node === "object") {
    if (typeof node.message === "string") {
      if (!out.includes(node.message)) out.push(node.message);
    } else {
      Object.values(node).forEach((child) => messagesOf(child, out));
    }
  }
  return out;
};

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
  helpText,
  required,
  ...uiProps
}) => {
  const { values, errors, initialErrors, initialValues, setFieldValue } =
    useFormikContext();
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  const current = getIn(values, fieldPath) || {};
  // Unit chosen while the quantity is empty; written on the next value.
  const [pickedUnit, setPickedUnit] = useState(undefined);
  const unit = pickedUnit ?? current.unit ?? defaultUnit;

  // C1 fallback: server errors arrive as initialErrors and Formik clears
  // `errors` on the first edit; read the initial ones while the value is
  // untouched. (Local; re-point to errors.js useFieldErrors once it lands.)
  const pick = (source) => {
    const node = getIn(source, fieldPath);
    return node === undefined || node === null || node === ""
      ? undefined
      : node;
  };
  const errorNode =
    pick(errors) ??
    (getIn(values, fieldPath) === getIn(initialValues, fieldPath)
      ? pick(initialErrors)
      : undefined);
  // The object path itself can hold the message (required quantity
  // missing); the children hold value/unit validation messages.
  const objectMessages =
    typeof errorNode === "string"
      ? [errorNode]
      : errorNode && typeof errorNode.message === "string"
      ? [errorNode.message]
      : [];
  const valueMessages = messagesOf(errorNode && errorNode.value);
  const unitMessages = messagesOf(errorNode && errorNode.unit);
  const hasError =
    objectMessages.length + valueMessages.length + unitMessages.length > 0;

  const setValue = (raw) => {
    if (raw === "") {
      setFieldValue(fieldPath, undefined);
      setPickedUnit(undefined);
      return;
    }
    const n = parseFloat(raw);
    setFieldValue(fieldPath, {
      value: Number.isNaN(n) ? raw : n,
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
      {[...objectMessages, ...valueMessages, ...unitMessages].map((message) => (
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
  helpText: PropTypes.node,
  required: PropTypes.bool,
};
