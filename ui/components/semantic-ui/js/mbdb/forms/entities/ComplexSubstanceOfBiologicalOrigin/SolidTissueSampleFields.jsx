import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";

// The fields specific to a biological substance taken from a solid tissue.
// `organ` is required here (optional in Cell fraction) — D7 gives this variant
// its own flag. `homogenized` is a boolean: the buttons write true/false, never
// the strings "Yes"/"No", and "not answered" stays visible until one is picked.
export const SolidTissueSampleFields = ({ fieldPath }) => (
  <Form.Group widths="equal">
    <TextField fieldPath={`${fieldPath}.organ`} />
    <TextField fieldPath={`${fieldPath}.health_status`} />
    <ButtonGroupField
      fieldPath={`${fieldPath}.homogenized`}
      options={[
        { value: true, text: "Yes" },
        { value: false, text: "No" },
      ]}
    />
  </Form.Group>
);

SolidTissueSampleFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
