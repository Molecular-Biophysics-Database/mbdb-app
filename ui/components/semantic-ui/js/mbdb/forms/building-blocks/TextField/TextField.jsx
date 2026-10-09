import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { parseNumberInput } from "@js/mbdb/forms/building-blocks/number";
import { ExternalLink } from "@js/mbdb/forms/building-blocks/ExternalLink";
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
// clears; anything else unparseable (a caller that changed `type`, jsdom)
// becomes undefined via parseNumberInput, so the store never holds NaN.
// The wrapper's controlled `value` keeps showing what the user typed.
export const NumberField = ({
  fieldPath,
  integer,
  min,
  max,
  step,
  ...uiProps
}) => {
  const f = useFieldBinding(fieldPath);
  return (
    <MbdbTextField
      fieldPath={fieldPath}
      {...uiProps}
      type="number"
      min={min}
      max={max}
      step={step ?? (integer ? 1 : "any")}
      onChange={(e, { value }) => {
        // "" and unparseable input both clear (parseNumberInput →
        // undefined IS the clear marker): setValue unsets and prunes
        f.setValue(value === "" ? undefined : parseNumberInput(value));
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

// SUIR 2.1.5 TextArea has no autoHeight: the prop lands on the DOM and does
// nothing. Growth is emulated by sizing `rows` to the content: one line per
// ~80 characters plus one per line break, at least `min` (3 by default), capped at 12.
// Pure and exported so other places with a textarea (TableArrayField's
// textarea cells) can size rows the same way.
export const autoRows = (text, { min = 3 } = {}) => {
  const s = String(text ?? "");
  return Math.min(
    12,
    Math.max(min, Math.ceil(s.length / 80) + s.split("\n").length - 1)
  );
};

// Long text (sequences). `monospace` needs one CSS rule (see
// custom-components.less): .mbdb-monospace textarea uses a monospace font.
// `links` renders small basic link buttons under the field.
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
  const sizedRows = autoHeight ? autoRows(text) : rows;
  return (
    // links go INSIDE the wrapper's Form.Field via its children slot — as
    // siblings they would become their own column inside Form.Group rows
    <MbdbTextAreaField
      fieldPath={fieldPath}
      className={
        [monospace && "mbdb-monospace", className].filter(Boolean).join(" ") ||
        undefined
      }
      {...uiProps}
      rows={sizedRows}
    >
      {links &&
        links.map(({ label, href }) => (
          <ExternalLink key={href} href={href}>
            {label}
          </ExternalLink>
        ))}
    </MbdbTextAreaField>
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
