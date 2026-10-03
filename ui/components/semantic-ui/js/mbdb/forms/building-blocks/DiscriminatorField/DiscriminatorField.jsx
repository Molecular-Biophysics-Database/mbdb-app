import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import pick from "lodash/pick";
import { Button, Confirm, Dropdown } from "mbdb-semantic-ui-react";
import {
  isEmptyValue,
  useFieldErrors,
  useOwnErrorMessages,
} from "@js/mbdb/forms/building-blocks/errors";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import { toOption } from "@js/mbdb/forms/building-blocks/options";
import { onRovingKeyDown } from "@js/mbdb/forms/building-blocks/rovingFocus";
import { useUnsetField } from "@js/mbdb/forms/building-blocks/unset";

// A choice that decides which fields follow; changing it replaces the object
// and keeps only `keep` keys (design/building-blocks/DiscriminatorField.md).
export const DiscriminatorField = ({
  objectPath,
  field,
  options,
  variant,
  keep = ["id"],
  seed,
  allowUnset = false,
  unsetLabel = "Not specified",
  label,
  help,
  required,
}) => {
  const { values, setFieldValue } = useFormikContext();
  const unset = useUnsetField();
  // The hook keeps helpText because that is the model's key (getFieldData);
  // the block's public prop is `help`.
  const data = useModelFieldData(`${objectPath}.${field}`, {
    label,
    helpText: help,
    required,
  });
  const text = data.label;

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

  // `keep` preserves fields rendered above the discriminator (a sub-type change
  // keeps `name`, a component keeps `name`/`copy_number`). The confirm must not
  // promise to delete them: any keep beyond `id` uses the type-specific copy,
  // a static string (design/building-blocks/DiscriminatorField.md, "confirm
  // copy with keep").
  const keepsBeyondId = keep.some((key) => key !== "id");

  const apply = (newValue) => {
    if (newValue === undefined) unset(objectPath);
    else
      setFieldValue(objectPath, {
        ...pick(obj ?? {}, keep),
        [field]: newValue,
        // seed last: a fixed value the new type's model requires (design,
        // "Addition: seed"). Applied after `keep` and the new value, so it is
        // never overwritten by a keep key with the same name.
        ...(seed?.(newValue) ?? {}),
      });
  };

  const requestChange = (newValue) => {
    if (newValue === undefined) {
      // Unset works on the object, not the field: only data besides the
      // discriminator and the `keep` keys is lost, so use the same test as a
      // change (guide: "No" → "Not specified" keeps only the answer, so it
      // must not ask). An absent object is a no-op.
      if (obj === undefined) return;
      if (hasOtherData(obj)) setPending(undefined);
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

  return (
    <FieldShell
      // inputId points at the field path so OARepo error scrolling finds
      // it; the control itself is a Semantic Dropdown, not labelable. An
      // empty-string label renders no label at all (the pre-shell `text &&`
      // gate).
      inputId={`${objectPath}.${field}`}
      label={text || undefined}
      help={data.helpText}
      required={data.required}
      hasError={errorMessages.length > 0}
      messages={errorMessages}
      // a button row is composite: its help belongs under the label, not below
      // the buttons where it reads like the next field's help. A dropdown is a
      // single control, so its help stays under the control (guide §8).
      helpPlacement={mode === "buttons" ? "label" : "control"}
    >
      {mode === "buttons" ? (
        <Button.Group
          role="group"
          aria-label={typeof text === "string" ? text : field}
          onKeyDown={onRovingKeyDown}
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
          options={normalized.map((o) =>
            toOption({ value: o.value, text: o.label })
          )}
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
            : `Change ${text ?? field} to "${labelOf(pending)}"?`
        }
        content={
          keepsBeyondId
            ? "The type-specific data will be removed."
            : current === undefined || pending === undefined
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
    </FieldShell>
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
  seed: PropTypes.func,
  allowUnset: PropTypes.bool,
  unsetLabel: PropTypes.string,
  label: PropTypes.string,
  help: PropTypes.string,
  required: PropTypes.bool,
};
