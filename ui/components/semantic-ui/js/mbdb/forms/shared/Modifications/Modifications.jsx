import React from "react";
import PropTypes from "prop-types";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { ModificationTable } from "./ModificationTable";

// The polymer's `modifications` object: two lists, one table each
// (design Modifications).
export const Modifications = ({ fieldPath }) => (
  <FieldGroup fieldPath={fieldPath}>
    <ModificationTable fieldPath={`${fieldPath}.biological_postprocessing`} />
    <ModificationTable fieldPath={`${fieldPath}.chemical`} />
  </FieldGroup>
);

Modifications.propTypes = {
  // the Polymer_modifications OBJECT path (`${itemPath}.modifications`)
  fieldPath: PropTypes.string.isRequired,
};
