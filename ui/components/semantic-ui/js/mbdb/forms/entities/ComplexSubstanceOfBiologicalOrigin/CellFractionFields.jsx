import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";

// The fields specific to a biological substance derived from a sub-cellular
// fraction: the fraction vocabulary and the donor's health status, then the
// optional organ / tissue / cell type. `organ` is optional here and required
// in Solid tissue sample — the model lookup gives each variant its own
// flag, so it is not overridden. `cell-fractions` is the hyphenated server
// name.
export const CellFractionFields = ({ fieldPath }) => (
  <>
    <Form.Group widths="equal">
      <MbdbVocabularyField
        vocabularyName="cell-fractions"
        fieldPath={`${fieldPath}.fraction`}
      />
      <TextField fieldPath={`${fieldPath}.health_status`} />
    </Form.Group>
    <Form.Group widths="equal">
      <TextField fieldPath={`${fieldPath}.organ`} />
      <TextField fieldPath={`${fieldPath}.tissue`} />
      <TextField fieldPath={`${fieldPath}.cell_type`} />
    </Form.Group>
  </>
);

CellFractionFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
