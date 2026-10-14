import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { OrcidField } from "./OrcidField";
import { Affiliations } from "./Affiliations";

// The group spec of a person (model type Person), read by the details views
// (guide §8). Affiliations are vocabulary references, so they declare their
// vocabulary for the details view.
export const PERSON_GROUPS = [
  {
    title: "Person",
    fields: [
      "given_name",
      "family_name",
      "identifiers",
      { field: "affiliations", vocabulary: "affiliations" },
    ],
  },
];

// The fields of one person (model type Person): the ORCID lookup first (its
// Prefill fills the names below), then Given name and Family name side by side
// (both required) and the ROR Affiliations behind a plus button. Labels, help
// and required come from the model (the depositors subtree is in the ui_model).
// `mbdb-person` keeps the form compact (custom-components.less).
export const PersonForm = ({ fieldPath }) => (
  <div className="mbdb-person">
    <OrcidField fieldPath={fieldPath} />
    <Form.Group widths="equal">
      <TextField fieldPath={`${fieldPath}.given_name`} />
      <TextField fieldPath={`${fieldPath}.family_name`} />
    </Form.Group>
    <Affiliations fieldPath={`${fieldPath}.affiliations`} />
  </div>
);

PersonForm.propTypes = {
  // the person OBJECT path
  fieldPath: PropTypes.string.isRequired,
};
