import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import pick from "lodash/pick";
import { Button, Confirm, FieldHelp, Form } from "mbdb-semantic-ui-react";
import { isEmptyValue } from "../errors";
import { useModelFieldData } from "../fieldData";

// A choice that decides which fields follow; changing it replaces the object
// and keeps only `keep` keys (design/building-blocks/DiscriminatorField.md).
export const DiscriminatorField = ({
  objectPath,
  field,
  options,
  variant,
  keep = ["id"],
  allowUnset = false,
  unsetLabel = "Not specified",
  label,
  helpText,
  required,
}) => {
  const { values, setFieldValue } = useFormikContext();
  const data = useModelFieldData(`${objectPath}.${field}`, {
    label,
    helpText,
    required,
  });
  const text = data.label;
  const help = data.helpText;

  const [pending, setPending] = useState(null); // value to apply after confirm
  const obj = getIn(values, objectPath);
  const current = obj?.[field];

  // data besides the discriminator and the kept keys would be lost on change
  const hasOtherData = (candidate) =>
    Object.entries(candidate ?? {}).some(
      ([key, value]) =>
        key !== field && !keep.includes(key) && !isEmptyValue(value)
    );
  const hasDataAny = (candidate) =>
    Object.entries(candidate ?? {}).some(([, value]) => !isEmptyValue(value));

  const apply = (newValue) => {
    if (newValue === undefined) setFieldValue(objectPath, undefined);
    else
      setFieldValue(objectPath, {
        ...pick(obj ?? {}, keep),
        [field]: newValue,
      });
  };

  const requestChange = (newValue) => {
    if (newValue === current) return;
    if (newValue === undefined ? hasDataAny(obj) : hasOtherData(obj))
      setPending(newValue);
    else apply(newValue);
  };

  const normalized = options.map((option) =>
    typeof option === "string"
      ? { value: option, label: option }
      : { value: option.value, label: option.label ?? option.value }
  );
  const mode = variant ?? (normalized.length <= 4 ? "buttons" : "dropdown");

  return (
    <Form.Field required={data.required}>
      {text && <label>{text}</label>}
      {help && <FieldHelp help={help} />}
      {mode === "buttons" ? (
        <Button.Group>
          {allowUnset && (
            <Button
              type="button"
              primary={current === undefined}
              onClick={() => requestChange(undefined)}
            >
              {unsetLabel}
            </Button>
          )}
          {normalized.map((option) => (
            <Button
              key={option.value}
              type="button"
              primary={current === option.value}
              onClick={() => requestChange(option.value)}
            >
              {option.label}
            </Button>
          ))}
        </Button.Group>
      ) : (
        <Form.Dropdown
          selection
          clearable={allowUnset}
          options={normalized.map((option) => ({
            key: option.value,
            value: option.value,
            text: option.label,
          }))}
          value={current ?? ""}
          onChange={(e, { value: next }) =>
            requestChange(next === "" ? undefined : next)
          }
          aria-label={text ?? field}
        />
      )}
      <Confirm
        open={pending !== null}
        header={
          pending === undefined
            ? `${unsetLabel}: remove ${text ?? field}?`
            : `Change ${text ?? field} to "${pending}"?`
        }
        content={
          current === undefined || pending === undefined
            ? "The entered data will be removed."
            : `The data entered for "${current}" will be removed.`
        }
        confirmButton={pending === undefined ? "Remove" : "Change"}
        onCancel={() => setPending(null)}
        onConfirm={() => {
          apply(pending);
          setPending(null);
        }}
      />
    </Form.Field>
  );
};

DiscriminatorField.propTypes = {
  objectPath: PropTypes.string.isRequired,
  field: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(
    PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.shape({
        value: PropTypes.string.isRequired,
        label: PropTypes.string,
      }),
    ])
  ).isRequired,
  variant: PropTypes.oneOf(["buttons", "dropdown"]),
  keep: PropTypes.arrayOf(PropTypes.string),
  allowUnset: PropTypes.bool,
  unsetLabel: PropTypes.string,
  label: PropTypes.string,
  helpText: PropTypes.string,
  required: PropTypes.bool,
};
