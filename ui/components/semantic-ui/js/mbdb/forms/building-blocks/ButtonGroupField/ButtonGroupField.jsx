import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import {
  Button,
  Form,
  Label,
  FieldHelp,
  HelpLabel,
} from "mbdb-semantic-ui-react";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import { useFieldErrors } from "@js/mbdb/forms/building-blocks/errors";
import { toOption } from "@js/mbdb/forms/building-blocks/options";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";
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
  const { values, setFieldValue } = useFormikContext();
  // The hook keeps helpText because that is the model's key (getFieldData);
  // the block's public prop is `help`.
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const opts = options.map((o) => {
    const { value, text } = toOption(o);
    return { value, text: String(text) }; // boolean values need string labels
  });
  const current = getIn(values, fieldPath);

  const { messages, hasError } = useFieldErrors(fieldPath);

  if (opts.length > 5) {
    return (
      <SelectField
        fieldPath={fieldPath}
        options={opts.map(({ value, text }) => ({
          key: String(value),
          value,
          text,
        }))}
        label={data.label}
        help={data.helpText}
        required={data.required}
      />
    );
  }

  // arrow-key roving focus — same as DiscriminatorField (share if a third
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
    <Form.Field required={data.required} error={hasError}>
      <label htmlFor={fieldPath}>
        <HelpLabel label={data.label} help={data.helpText} />
      </label>
      <Button.Group
        id={fieldPath}
        // role="group", not "radiogroup": the buttons toggle (aria-pressed),
        // they are not radios. Design doc asks for the mix; flagged for
        // a design update (ButtonGroupField-review F6).
        role="group"
        aria-label={typeof data.label === "string" ? data.label : fieldPath}
        onKeyDown={onKeyDown}
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
                if (isActive) {
                  // unset (not setFieldValue(path, undefined)) so a now-empty
                  // parent object is dropped, not left as {} (guide §7).
                  if (!data.required)
                    unsetFieldValue(values, setFieldValue, fieldPath);
                } else {
                  setFieldValue(fieldPath, value);
                }
              }}
            >
              {text}
            </Button>
          );
        })}
      </Button.Group>
      {messages.length > 0 && (
        <Label basic color="red" pointing>
          {messages.join(" ")}
        </Label>
      )}
      <FieldHelp help={data.helpText} />
    </Form.Field>
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
