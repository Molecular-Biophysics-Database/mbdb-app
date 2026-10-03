import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Divider, Form } from "mbdb-semantic-ui-react";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import {
  NumberField,
  TextField,
} from "@js/mbdb/forms/building-blocks/TextField";
import { PolymerFields } from "@js/mbdb/forms/entities/Polymer";
import { ChemicalFields } from "@js/mbdb/forms/entities/Chemical";
import { COMPONENT_TYPES } from "./constants";

// Copy number is a double in the model (a ratio such as 0.5 is valid); -1
// means "unknown" and is shown as such in the table only, the input keeps -1.
export const ComponentFields = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const type = getIn(values, `${fieldPath}.type`);
  return (
    <>
      <DiscriminatorField
        objectPath={fieldPath}
        field="type"
        options={COMPONENT_TYPES}
        variant="buttons"
        // Polymer and Chemical both have additional_specifications, so a type
        // change keeps it (plan 4R, Y1)
        keep={["name", "copy_number", "additional_specifications"]}
      />
      <Form.Group widths="equal">
        <TextField fieldPath={`${fieldPath}.name`} />
        <NumberField fieldPath={`${fieldPath}.copy_number`} min={-1} />
      </Form.Group>
      <Divider />
      {type === "Polymer" && <PolymerFields fieldPath={fieldPath} />}
      {type === "Chemical" && <ChemicalFields fieldPath={fieldPath} />}
    </>
  );
};

ComponentFields.propTypes = {
  // the component item path
  fieldPath: PropTypes.string.isRequired,
};
