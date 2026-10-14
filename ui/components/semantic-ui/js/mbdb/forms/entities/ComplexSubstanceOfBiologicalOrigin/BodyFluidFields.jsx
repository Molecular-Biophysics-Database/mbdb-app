import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";

// The fields specific to a biological substance derived from a body fluid: the
// fluid vocabulary and the donor's health status, on one row. `body-fluids` is
// the hyphenated name the server knows. Every path is built
// from `fieldPath` (the entity item path).
export const BodyFluidFields = ({ fieldPath }) => (
  <Form.Group widths="equal">
    <MbdbVocabularyField
      vocabularyName="body-fluids"
      fieldPath={`${fieldPath}.fluid`}
    />
    <TextField fieldPath={`${fieldPath}.health_status`} />
  </Form.Group>
);

BodyFluidFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
