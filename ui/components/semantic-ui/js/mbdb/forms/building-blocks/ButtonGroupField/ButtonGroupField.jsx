import React from "react";
import PropTypes from "prop-types";
import { Button } from "mbdb-semantic-ui-react";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import { useRowHelpPlacement } from "@js/mbdb/forms/building-blocks/FieldRow";
import { toOption } from "@js/mbdb/forms/building-blocks/options";
import { onRovingKeyDown } from "@js/mbdb/forms/building-blocks/rovingFocus";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";

// A single choice among 2–5 short options shown as a Button.Group, so all
// options are visible; more than 5 options fall back to a SelectField.
// Clicking the active button clears the value, but only when the field is
// optional. Values may be strings or booleans.
export const ButtonGroupField = ({
  fieldPath,
  options,
  label,
  help,
  required,
}) => {
  const f = useFieldBinding(fieldPath, { label, help, required });
  // In a Form.Group row every field puts its help under its control, so the row
  // lines up (FieldRow); outside a row the buttons keep it under the label,
  // where a help under the buttons would read like the next field's (guide §8).
  const rowPlacement = useRowHelpPlacement();
  const opts = options.map((o) => {
    const { value, text } = toOption(o);
    return { value, text: String(text) }; // boolean values need string labels
  });
  const current = f.value;

  if (opts.length > 5) {
    return (
      <SelectField
        fieldPath={fieldPath}
        options={opts.map(({ value, text }) => ({
          key: String(value),
          value,
          text,
        }))}
        label={f.label}
        help={f.help}
        required={f.required}
      />
    );
  }

  return (
    <FieldShell
      inputId={fieldPath}
      label={f.label}
      help={f.help}
      required={f.required}
      hasError={f.hasError}
      messages={f.messages}
      helpPlacement={rowPlacement ?? "label"}
    >
      <Button.Group
        id={fieldPath}
        // role="group", not "radiogroup": the buttons toggle (aria-pressed),
        // they are not radios. The design doc asks for the mix.
        role="group"
        aria-label={typeof f.label === "string" ? f.label : fieldPath}
        onKeyDown={onRovingKeyDown}
      >
        {opts.map(({ value, text }) => {
          const isActive = current === value;
          return (
            // Semantic Button renders aria-pressed itself from its
            // toggle/active pair; an aria-pressed prop would be dropped.
            <Button
              key={String(value)}
              type="button"
              toggle
              primary={isActive}
              active={isActive}
              onClick={() => {
                // the binding's writer: undefined unsets (a now-empty parent
                // object is dropped, not left as {}, guide §7); required
                // fields keep the value instead
                if (isActive) {
                  if (!f.required) f.setValue(undefined);
                } else {
                  f.setValue(value);
                }
              }}
            >
              {text}
            </Button>
          );
        })}
      </Button.Group>
    </FieldShell>
  );
};

ButtonGroupField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(
    PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.shape({
        value: PropTypes.oneOfType([PropTypes.string, PropTypes.bool])
          .isRequired,
        text: PropTypes.node.isRequired,
      }),
    ])
  ).isRequired,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
};
