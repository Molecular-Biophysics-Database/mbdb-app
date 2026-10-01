import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";
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
  help: PropTypes.node,
  required: PropTypes.bool,
  width: PropTypes.number,
};

// Number input that stores a real number and removes the key when
// cleared. `type="number"` reports unparseable input as "", which also
// clears; the isNaN guard is for callers that change `type` (jsdom).
// The wrapper's controlled `value` keeps showing what the user typed.
export const NumberField = ({
  fieldPath,
  integer,
  min,
  max,
  step,
  ...uiProps
}) => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <MbdbTextField
      fieldPath={fieldPath}
      {...uiProps}
      type="number"
      min={min}
      max={max}
      step={step ?? (integer ? 1 : "any")}
      onChange={(e, { value }) => {
        if (value === "") {
          unsetFieldValue(values, setFieldValue, fieldPath);
          return;
        }
        const n = Number(value);
        setFieldValue(fieldPath, Number.isNaN(n) ? undefined : n);
      }}
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
  help: PropTypes.node,
  required: PropTypes.bool,
  width: PropTypes.number,
};

// Long text (sequences). `monospace` needs one CSS rule (see
// custom-components.less): .mbdb-monospace textarea uses a monospace font.
// `links` renders small basic link buttons under the field.
// SUIR 2.1.5 TextArea has no autoHeight: it is emulated by sizing `rows`
// to the content (max 12); autoHeight is NOT passed down to the DOM.
export const TextAreaField = ({
  fieldPath,
  links,
  monospace,
  autoHeight,
  rows,
  className,
  ...uiProps
}) => {
  const { values } = useFormikContext();
  const text = String(getIn(values, fieldPath) ?? "");
  const sizedRows = autoHeight
    ? Math.min(
        12,
        Math.max(3, Math.ceil(text.length / 80) + text.split("\n").length - 1)
      )
    : rows;
  return (
    <>
      <MbdbTextAreaField
        fieldPath={fieldPath}
        className={
          [monospace && "mbdb-monospace", className]
            .filter(Boolean)
            .join(" ") || undefined
        }
        {...uiProps}
        rows={sizedRows}
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
};

TextAreaField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
  autoHeight: PropTypes.bool,
  rows: PropTypes.number,
  monospace: PropTypes.bool,
  links: PropTypes.arrayOf(
    PropTypes.shape({
      label: PropTypes.string.isRequired,
      href: PropTypes.string.isRequired,
    })
  ),
  className: PropTypes.string,
};
