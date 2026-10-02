import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { Form, Button } from "mbdb-semantic-ui-react";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { NumberField } from "@js/mbdb/forms/building-blocks/TextField";
import { hasData } from "@js/mbdb/forms/building-blocks/errors";
import { useUnsetField } from "@js/mbdb/forms/building-blocks/unset";
import { SIZE_TYPES, LENGTH_UNITS } from "./constants";

// The size of a lipid assembly: a small statistics group with a single unit
// shared by all numbers. Title and help come from the model through
// fieldPath; each row's label too (the field blocks resolve their own).
export const Size = ({ fieldPath }) => {
  const { values } = useFormikContext();
  // required only once size is present: the model marks type/unit/mean
  // required unconditionally because it describes the inside of `size`;
  // `size` itself is optional, so the markers appear after the first entry
  const filled = hasData(getIn(values, fieldPath));
  const unset = useUnsetField();
  return (
    <FieldGroup
      fieldPath={fieldPath}
      actions={
        // A required field can't be cleared on its own, so the group header
        // gets one action that removes the whole optional object (no
        // confirm: it is a few numbers). Keeps required={filled} safe to use.
        filled ? (
          <Button
            basic
            size="mini"
            type="button"
            floated="right"
            onClick={() => unset(fieldPath)}
          >
            Clear size
          </Button>
        ) : undefined
      }
    >
      <Form.Group widths="equal">
        <ButtonGroupField
          fieldPath={`${fieldPath}.type`}
          options={SIZE_TYPES}
          required={filled}
        />
        <SelectField
          fieldPath={`${fieldPath}.unit`}
          options={LENGTH_UNITS}
          required={filled}
        />
      </Form.Group>
      <NumberField
        fieldPath={`${fieldPath}.mean`}
        min={0}
        step="any"
        required={filled}
      />
      <Form.Group widths="equal">
        <NumberField fieldPath={`${fieldPath}.median`} min={0} step="any" />
        <NumberField fieldPath={`${fieldPath}.lower`} min={0} step="any" />
        <NumberField fieldPath={`${fieldPath}.upper`} min={0} step="any" />
      </Form.Group>
    </FieldGroup>
  );
};

Size.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
