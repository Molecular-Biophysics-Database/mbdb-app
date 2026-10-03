import React from "react";
import PropTypes from "prop-types";
import { StringArrayField } from "mbdb-react-invenio-forms";
import { BasicInformation } from "@js/mbdb/forms/shared/BasicInformation";

// The content of a chemical's entity modal, after Type and Name: the
// PubChem-backed picker and the free-text specifications. Reused as a
// component's field set (ComponentChemical), so it assumes nothing about
// where it sits — every path is built from `fieldPath`.
export const ChemicalFields = ({ fieldPath }) => (
  <>
    <BasicInformation fieldPath={`${fieldPath}.basic_information`} />
    <StringArrayField fieldPath={`${fieldPath}.additional_specifications`} />
  </>
);

ChemicalFields.propTypes = {
  // the entity item path (or a component item path)
  fieldPath: PropTypes.string.isRequired,
};
