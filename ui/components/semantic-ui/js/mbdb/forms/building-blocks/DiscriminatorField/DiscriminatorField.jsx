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
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";
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
  const { values, errors, initialErrors, initialValues, setFieldValue } =
    useFormikContext();
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

  // C1 fallback: server errors arrive as initialErrors and Formik clears
  // `errors` on the first edit; read the initial ones while the object is
  // untouched. (Local; re-point to errors.js useFieldErrors once it lands.)
  const srcHas = (source) => {
    const atField = getIn(source, `${objectPath}.${field}`);
    if (atField !== undefined && atField !== null && atField !== "")
      return true;
    const atObject = getIn(source, objectPath);
    return (
      (typeof atObject === "string" && atObject !== "") ||
      (atObject !== null &&
        typeof atObject === "object" &&
        typeof atObject.message === "string")
    );
  };
  const errorSource = srcHas(errors)
    ? errors
    : obj === getIn(initialValues, objectPath)
    ? initialErrors
    : {};
  // Errors of the discriminator itself plus a string error at the object
  // path (NOT errors of the sub-form's fields; those render elsewhere).
  const objError = getIn(errorSource, objectPath);
  const errorMessages = [
    ...messagesOf(
      typeof objError === "string" ||
        (objError && typeof objError.message === "string")
        ? objError
        : undefined
    ),
    ...messagesOf(getIn(errorSource, `${objectPath}.${field}`)),
  ];

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
    if (newValue === undefined) {
      // Unset works on the object, not the field: an existing object with
      // data (even without `field`) must confirm, an absent one is a no-op.
      if (obj === undefined) return;
      if (hasDataAny(obj)) setPending(undefined);
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

  // Arrow keys move focus between the option buttons (same small handler
  // as ButtonGroupField; kept separate because the confirm-gated onSelect
  // cannot go through ButtonGroupField's direct setFieldValue binding).
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
  helpText: PropTypes.string,
  required: PropTypes.bool,
};
