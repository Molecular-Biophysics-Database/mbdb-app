import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import pick from "lodash/pick";
import {
  Button,
  Confirm,
  Dropdown,
  FieldHelp,
  Form,
  HelpLabel,
  Label,
} from "mbdb-semantic-ui-react";
import {
  hasData,
  isEmptyValue,
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

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
  help,
  required,
}) => {
  const { values, setFieldValue } = useFormikContext();
  // The hook keeps helpText because that is the model's key (getFieldData);
  // the block's public prop is `help`.
  const data = useModelFieldData(`${objectPath}.${field}`, {
    label,
    helpText: help,
    required,
  });
  const text = data.label;
  const helpText = data.helpText;

  const [pending, setPending] = useState(null); // value to apply after confirm
  const obj = getIn(values, objectPath);
  const current = obj?.[field];

  // Errors of the discriminator itself plus a string error at the object
  // path (NOT errors of the sub-form's fields; those render elsewhere).
  const objectMessages = useOwnErrorMessages(objectPath);
  const fieldMessages = useFieldErrors(`${objectPath}.${field}`).messages;
  const errorMessages = [...new Set([...objectMessages, ...fieldMessages])];

  // data besides the discriminator and the kept keys would be lost on change
  const hasOtherData = (candidate) =>
    Object.entries(candidate ?? {}).some(
      ([key, value]) =>
        key !== field && !keep.includes(key) && !isEmptyValue(value)
    );

  const apply = (newValue) => {
    if (newValue === undefined) setFieldValue(objectPath, undefined);
    else
      setFieldValue(objectPath, {
        ...pick(obj ?? {}, keep),
        [field]: newValue,
      });
  };

  const requestChange = (newValue) => {
    if (newValue === undefined) {
      // Unset works on the object, not the field: an existing object with
      // data (even without `field`) must confirm, an absent one is a no-op.
      if (obj === undefined) return;
      if (hasData(obj)) setPending(undefined);
      else apply(undefined);
      return;
    }
    if (newValue === current) return;
    if (hasOtherData(obj)) setPending(newValue);
    else apply(newValue);
  };

  const normalized = options.map((option) =>
    typeof option === "string"
      ? { value: option, label: option }
      : { value: option.value, label: option.label ?? option.value }
  );
  const labelOf = (value) =>
    normalized.find((option) => option.value === value)?.label ?? value;
  const mode = variant ?? (normalized.length <= 4 ? "buttons" : "dropdown");

  // arrow-key roving focus — same as ButtonGroupField (share if a third
  // user appears)
  const onKeyDown = (e) => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    const buttons = [...e.currentTarget.querySelectorAll("button")];
    const index = buttons.indexOf(document.activeElement);
    if (index === -1) return;
    e.preventDefault();
    const next =
      e.key === "ArrowRight"
        ? (index + 1) % buttons.length
        : (index - 1 + buttons.length) % buttons.length;
    buttons[next].focus();
  };

  return (
    <Form.Field required={data.required} error={errorMessages.length > 0}>
      {text && (
        // htmlFor points at the field path so OARepo error scrolling finds
        // it; the control itself is a Semantic Dropdown, not labelable.
        <label htmlFor={`${objectPath}.${field}`}>
          <HelpLabel label={text} help={help} />
        </label>
      )}
      {help && <FieldHelp help={help} />}
      {mode === "buttons" ? (
        <Button.Group
          role="group"
          aria-label={typeof text === "string" ? text : field}
          onKeyDown={onKeyDown}
        >
          {allowUnset && (
            <Button
              type="button"
              toggle
              primary={obj === undefined}
              active={obj === undefined}
              onClick={() => requestChange(undefined)}
            >
              {unsetLabel}
            </Button>
          )}
          {normalized.map((option) => (
            <Button
              key={option.value}
              type="button"
              toggle
              primary={current === option.value}
              active={current === option.value}
              onClick={() => requestChange(option.value)}
            >
              {option.label}
            </Button>
          ))}
        </Button.Group>
      ) : (
        <Dropdown
          fluid
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
      {errorMessages.map((message) => (
        <Label key={message} basic color="red" pointing>
          {message}
        </Label>
      ))}
      <Confirm
        open={pending !== null}
        header={
          pending === undefined
            ? `${unsetLabel}: remove ${text ?? field}?`
            : `Change ${text ?? field} to "${labelOf(pending)}"?`
        }
        content={
          current === undefined || pending === undefined
            ? "The entered data will be removed."
            : `The data entered for "${labelOf(current)}" will be removed.`
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
  help: PropTypes.string,
  required: PropTypes.bool,
};
