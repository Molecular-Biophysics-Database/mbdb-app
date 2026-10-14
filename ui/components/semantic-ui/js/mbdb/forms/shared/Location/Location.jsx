import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { NumberField } from "@js/mbdb/forms/building-blocks/TextField";
import { MapLink } from "./MapLink";

// Sampling coordinates: three number fields on one row, plus a link to check
// them on a map. The FieldGroup takes title, help and required from the model
// through fieldPath. step="any" on all three so decimals are not rounded
// (the old form had step=1). The altitude label override "(m)" is NOT passed:
// it belongs in the model label (guide §6), which currently says "Altitude".
export const Location = ({ fieldPath }) => (
  <FieldGroup fieldPath={fieldPath}>
    <Form.Group widths="equal">
      <NumberField
        fieldPath={`${fieldPath}.latitude`}
        min={-90}
        max={90}
        step="any"
      />
      <NumberField
        fieldPath={`${fieldPath}.longitude`}
        min={-180}
        max={180}
        step="any"
      />
      <NumberField
        fieldPath={`${fieldPath}.altitude`}
        min={-6378100}
        step="any"
      />
    </Form.Group>
    <MapLink fieldPath={fieldPath} />
  </FieldGroup>
);

Location.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
