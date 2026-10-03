import React, { useState } from "react";
import PropTypes from "prop-types";
import { useFormikContext } from "formik";
import { Dropdown, Input } from "mbdb-semantic-ui-react";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import {
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { parseNumberInput } from "@js/mbdb/forms/building-blocks/number";

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
  // The object-path write stays with Formik directly (the binding's writer
  // unsets on "", which is exactly the clear case; the value write carries
  // `{ value, unit }`, never a scalar).
  const { setFieldValue } = useFormikContext();
  const f = useFieldBinding(fieldPath, { label, help, required });
  const current = f.value || {};
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

  const setValue = (raw) => {
    if (raw === "") {
      // remove the whole object (and now-empty parents) and drop the
      // locally picked unit with it
      f.setValue("");
      setPickedUnit(undefined);
      return;
    }
    setFieldValue(fieldPath, {
      value: parseNumberInput(raw),
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
    <FieldShell
      inputId={fieldPath}
      label={f.label}
      help={f.help}
      required={f.required}
      messages={messages}
    >
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
    </FieldShell>
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
