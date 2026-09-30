import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { Button, Form, Label, FieldHelp } from "mbdb-semantic-ui-react";
import { useModelFieldData } from "../fieldData";

const toOption = (option) =>
  typeof option === "object" && option !== null
    ? option
    : { value: option, text: String(option) };

// A single choice among 2–5 short options shown as a Button.Group, so all
// options are visible. Clicking the active button clears the value, but
// only when the field is optional. Values may be strings or booleans.
export const ButtonGroupField = ({
  fieldPath,
  options,
  label,
  helpText,
  required,
}) => {
  const { values, errors, setFieldValue } = useFormikContext();
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  const opts = options.map(toOption);
  const current = getIn(values, fieldPath);
  const error = getIn(errors, fieldPath);

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
    <Form.Field required={data.required} error={!!error}>
      <label>{data.label}</label>
      <Button.Group
        role="radiogroup"
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
                  if (!data.required) setFieldValue(fieldPath, undefined);
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
      {error && (
        <Label basic color="red" pointing>
          {error}
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
  helpText: PropTypes.node,
  required: PropTypes.bool,
};
