import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Form, Icon } from "mbdb-semantic-ui-react";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { NumberField } from "@js/mbdb/forms/building-blocks/TextField";
import { HOMOGENEITY_METHODS } from "./constants";

// Shown under the Homogeneity row of QualityControls when "Yes" is selected.
export const HomogeneityFields = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const {
    expected_number_of_species: expected,
    number_of_species_observed: observed,
  } = getIn(values, fieldPath) ?? {};
  return (
    <>
      <SelectField
        fieldPath={`${fieldPath}.method`}
        options={HOMOGENEITY_METHODS}
      />
      <Form.Group widths="equal">
        <NumberField
          fieldPath={`${fieldPath}.expected_number_of_species`}
          integer
          min={1}
        />
        <NumberField
          fieldPath={`${fieldPath}.number_of_species_observed`}
          integer
          min={1}
        />
      </Form.Group>
      {expected !== undefined &&
        observed !== undefined &&
        observed > expected && (
          <p className="mbdb-muted-text">
            <Icon name="info circle" /> More species observed than expected.
          </p>
        )}
    </>
  );
};

HomogeneityFields.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
