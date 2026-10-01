import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { isManualChemical } from "./chemical";
import { ChemicalPicker } from "./ChemicalPicker";
import { ManualChemical } from "./ManualChemical";

// Basic information of a chemical: the PubChem-backed vocabulary dropdown,
// or the manual form when the stored value is a manual entry (has data but
// no id). The mode is derived from the VALUE on every render, not kept in
// state: the picker's "Enter manually" option and the manual form's "Search
// PubChem instead" both just write the value and the mode follows by
// itself, one write in each event handler.
export const BasicInformation = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const value = getIn(values, fieldPath);
  return isManualChemical(value) ? (
    <ManualChemical fieldPath={fieldPath} />
  ) : (
    <ChemicalPicker fieldPath={fieldPath} />
  );
};

BasicInformation.propTypes = {
  // `${itemPath}.basic_information`
  fieldPath: PropTypes.string.isRequired,
};
