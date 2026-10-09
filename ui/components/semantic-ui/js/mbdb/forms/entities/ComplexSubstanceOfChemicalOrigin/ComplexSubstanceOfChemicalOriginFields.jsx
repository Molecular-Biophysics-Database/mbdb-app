import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Label } from "mbdb-semantic-ui-react";
import { LipidAssemblyDetails } from "@js/mbdb/forms/shared/LipidAssemblyDetails";
import { ComplexSubstanceCommonFields } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";

// The model has a single class value, "Lipid assembly", so the class is echoed
// as read-only text instead of a one-option choice (design
// ComplexSubstanceOfChemicalOrigin). "Class" is the model label (guide §6),
// kept literal here because there is no control to label.
const ClassText = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const value = getIn(values, `${fieldPath}.class`);
  return value ? (
    <p>{`Class: ${value}`}</p>
  ) : (
    // old data or a bug; the server error at `class` explains what is missing.
    // A warning (the design's "warning Label"), like the other hints: the
    // server error is the real signal.
    <Label basic color="yellow" content="Class missing" />
  );
};
ClassText.propTypes = { fieldPath: PropTypes.string.isRequired };

// The content of a complex substance of chemical origin's modal, after Type and
// Name: the fixed class text, the lipid assembly details (assembly type, mono
// layers, size, components) and the common complex-substance block.
export const ComplexSubstanceOfChemicalOriginFields = ({ fieldPath }) => (
  <>
    <ClassText fieldPath={fieldPath} />
    <LipidAssemblyDetails fieldPath={fieldPath} />
    <ComplexSubstanceCommonFields fieldPath={fieldPath} />
  </>
);

ComplexSubstanceOfChemicalOriginFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
