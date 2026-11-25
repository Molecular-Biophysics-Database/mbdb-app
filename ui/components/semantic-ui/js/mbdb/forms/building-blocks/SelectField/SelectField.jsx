import React from "react";
import PropTypes from "prop-types";
import { Label } from "mbdb-semantic-ui-react";
import { SelectField as MbdbSelectField } from "mbdb-react-invenio-forms";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { toOption } from "@js/mbdb/forms/building-blocks/options";

// Dropdown with a fixed option list. String options are expanded to
// Semantic option objects. Optional fields are clearable, required ones
// are not (overridable with `clearable`). A stored value that is not in
// `options` stays visible (RIF ensureSelectedValuesInOptions) and is
// marked with a red "Unknown value" label instead of being deleted.
export const SelectField = ({
  fieldPath,
  options,
  clearable,
  label,
  help,
  required,
  ...uiProps
}) => {
  // Only the model data is needed here — but the binding IS the one model-
  // data hook now (the help → helpText mapping lives there alone).
  const f = useFieldBinding(fieldPath, { label, help, required });
  const opts = options.map(toOption);
  const isClearable = clearable !== undefined ? clearable : !f.required;
  const value = f.value;
  const unknown =
    value !== undefined &&
    value !== "" &&
    opts.length > 0 &&
    !opts.some((o) => o.value === value);

  return (
    <>
      <MbdbSelectField
        fieldPath={fieldPath}
        options={opts}
        clearable={isClearable}
        label={f.label}
        help={f.help}
        required={f.required}
        {...uiProps}
      />
      {unknown && (
        // Still below the wrapper's FieldHelp (accepted deviation), so it
        // does not `point` at the dropdown.
        <Label basic color="red">
          Unknown value
        </Label>
      )}
    </>
  );
};

SelectField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(
    PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.shape({
        key: PropTypes.string,
        value: PropTypes.string,
        text: PropTypes.node,
      }),
    ])
  ).isRequired,
  clearable: PropTypes.bool,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
};
