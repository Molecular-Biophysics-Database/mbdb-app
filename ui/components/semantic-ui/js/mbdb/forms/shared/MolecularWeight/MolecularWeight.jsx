import React from "react";
import PropTypes from "prop-types";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";

// Copied from the YAML enum MOLECULAR_WEIGHT_UNITS
// (models/general_parameters-definitions-rdm.yaml); a test compares this
// list with the same YAML values.
export const MOLECULAR_WEIGHT_UNITS = ["g/mol", "Da", "kDa", "MDa"];

// The molecular weight as one value+unit control. Label, help and required
// come from the model through fieldPath. There is no client-side min: the
// server checks minimum: -1 ("-1 if unknown").
export const MolecularWeight = ({ fieldPath, defaultUnit = "kDa" }) => (
  <ValueUnitField
    fieldPath={fieldPath}
    units={MOLECULAR_WEIGHT_UNITS}
    defaultUnit={defaultUnit}
  />
);

MolecularWeight.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  defaultUnit: PropTypes.oneOf(MOLECULAR_WEIGHT_UNITS),
};
