import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { PURITY_METHODS, PURITY_PERCENTAGES } from "./constants";

// Shown under the Purity row of QualityControls when "Yes" is selected.
// Labels/help/required come from the model (the variant-aware lookup picks
// the Yes variant once `assessed` is Yes).
export const PurityFields = ({ fieldPath }) => (
  <Form.Group widths="equal">
    <SelectField fieldPath={`${fieldPath}.method`} options={PURITY_METHODS} />
    <ButtonGroupField
      fieldPath={`${fieldPath}.purity_percentage`}
      options={PURITY_PERCENTAGES}
    />
  </Form.Group>
);

PurityFields.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
