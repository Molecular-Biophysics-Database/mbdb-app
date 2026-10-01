import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { Label } from "mbdb-semantic-ui-react";
import { SelectField as MbdbSelectField } from "mbdb-react-invenio-forms";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";

const toOption = (option) =>
  typeof option === "string"
    ? { key: option, value: option, text: option }
    : option;

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
  const { values } = useFormikContext();
  const data = useModelFieldData(fieldPath, {
    label,
    helpText: help,
    required,
  });
  const opts = options.map(toOption);
  const isClearable = clearable !== undefined ? clearable : !data.required;
  const value = getIn(values, fieldPath);
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
        label={data.label}
        help={data.helpText}
        required={data.required}
        {...uiProps}
      />
      {unknown && (
        // Still below the wrapper's FieldHelp (accepted deviation, see
        // SelectField-review F5), so it does not `point` at the dropdown.
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
