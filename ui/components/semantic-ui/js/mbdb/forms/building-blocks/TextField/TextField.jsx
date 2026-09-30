import React from "react";
import PropTypes from "prop-types";
import { useFormikContext } from "formik";
import { Button } from "mbdb-semantic-ui-react";
import {
  TextField as MbdbTextField,
  TextAreaField as MbdbTextAreaField,
} from "mbdb-react-invenio-forms";

// Plain text input. Labels/help/required come from the model via the
// mbdb-react-invenio-forms wrapper; any extra prop (e.g. `width={8}`,
// `placeholder`) flows through to the underlying Semantic Form.Input.
export const TextField = (props) => <MbdbTextField {...props} />;

TextField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.node,
  helpText: PropTypes.node,
  required: PropTypes.bool,
  width: PropTypes.number,
};

// Number input that stores a real number. RIF spread order puts uiProps
// after Formik's `field`, so this onChange overrides field.onChange and
// writes parsed values. NaN input keeps the raw string so the server can
// report it (and typing "-", "1e3" is not blocked); "" clears the value.
export const NumberField = ({
  fieldPath,
  integer,
  min,
  max,
  step = "any",
  ...uiProps
}) => {
  const { setFieldValue } = useFormikContext();
  return (
    <MbdbTextField
      fieldPath={fieldPath}
      type="number"
      min={min}
      max={max}
      step={step}
      onChange={(e, { value }) => {
        if (value === "") {
          setFieldValue(fieldPath, undefined);
        } else {
          const n = integer ? parseInt(value, 10) : parseFloat(value);
          setFieldValue(fieldPath, Number.isNaN(n) ? value : n);
        }
      }}
      {...uiProps}
    />
  );
};

NumberField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  integer: PropTypes.bool,
  min: PropTypes.number,
  max: PropTypes.number,
  step: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
  label: PropTypes.node,
  helpText: PropTypes.node,
  required: PropTypes.bool,
  width: PropTypes.number,
};

// Long text (sequences). `monospace` needs one CSS rule (see
// custom-components.less): .mbdb-monospace textarea uses a monospace font.
// `links` renders small basic link buttons under the field.
export const TextAreaField = ({
  fieldPath,
  links,
  monospace,
  className,
  ...uiProps
}) => (
  <>
    <MbdbTextAreaField
      fieldPath={fieldPath}
      className={
        [monospace && "mbdb-monospace", className].filter(Boolean).join(" ") ||
        undefined
      }
      {...uiProps}
    />
    {links &&
      links.map(({ label, href }) => (
        <Button
          key={href}
          basic
          size="mini"
          as="a"
          href={href}
          target="_blank"
          rel="noreferrer"
          type="button"
        >
          {label}
        </Button>
      ))}
  </>
);

TextAreaField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.node,
  helpText: PropTypes.node,
  required: PropTypes.bool,
  autoHeight: PropTypes.bool,
  monospace: PropTypes.bool,
  links: PropTypes.arrayOf(
    PropTypes.shape({
      label: PropTypes.string.isRequired,
      href: PropTypes.string.isRequired,
    })
  ),
  className: PropTypes.string,
};
