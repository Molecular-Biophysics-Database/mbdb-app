import React from "react";
import PropTypes from "prop-types";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields";
import { ComplexSubstanceCommonFields } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";

// The content of a complex substance of industrial origin's modal, after Type
// and Name: the product vocabulary field, then the common complex-substance
// block. Composition only; every path is built from `fieldPath`.
export const ComplexSubstanceOfIndustrialOriginFields = ({ fieldPath }) => (
  <>
    <MbdbVocabularyField
      vocabularyName="products"
      fieldPath={`${fieldPath}.product`}
    />
    <ComplexSubstanceCommonFields fieldPath={fieldPath} />
  </>
);

ComplexSubstanceOfIndustrialOriginFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
