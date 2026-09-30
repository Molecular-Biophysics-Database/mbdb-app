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
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";

const toOption = (option) =>
  typeof option === "object" && option !== null
    ? option
    : { value: option, text: String(option) };

// Unique message strings under path: strings plus OARepo
// { message, severity } objects (never rendered raw).
// Local clone of errors.js errorMessages applied to the C1 error source;
// point at errors.js/useFieldErrors once that helper exists.
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

// A single choice among 2–5 short options shown as a Button.Group, so all
// options are visible; more than 5 options fall back to a SelectField.
// Clicking the active button clears the value, but only when the field is
// optional. Values may be strings or booleans.
export const ButtonGroupField = ({
  fieldPath,
  options,
  label,
  helpText,
  required,
}) => {
  const { values, errors, initialErrors, initialValues, setFieldValue } =
    useFormikContext();
  const data = useModelFieldData(fieldPath, { label, helpText, required });
  const opts = options.map(toOption);
  const current = getIn(values, fieldPath);

  // C1 fallback: server errors arrive as initialErrors; Formik clears
  // `errors` on the first edit. Read initialErrors while the value is
  // untouched. (Local; re-point to errors.js useFieldErrors once it lands.)
  const errorNode =
    getIn(errors, fieldPath) !== undefined && getIn(errors, fieldPath) !== null
      ? getIn(errors, fieldPath)
      : current === getIn(initialValues, fieldPath)
      ? getIn(initialErrors, fieldPath)
      : undefined;
  const messages = messagesOf(errorNode);

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
        helpText={data.helpText}
        required={data.required}
      />
    );
  }

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
    <Form.Field required={data.required} error={messages.length > 0}>
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
  helpText: PropTypes.node,
  required: PropTypes.bool,
};
