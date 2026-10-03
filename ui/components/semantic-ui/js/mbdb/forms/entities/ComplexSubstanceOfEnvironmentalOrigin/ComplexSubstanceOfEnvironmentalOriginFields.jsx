import React from "react";
import PropTypes from "prop-types";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields";
import { Location } from "@js/mbdb/forms/shared/Location";
import { ComplexSubstanceCommonFields } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";

// The content of a complex substance of environmental origin's modal, after
// Type and Name: the environment-type vocabulary field, the sampling
// coordinates and the common complex-substance block. Composition only; every
// path is built from `fieldPath`. `environment-types` is the hyphenated name
// the server knows (plan step 2, P1).
export const ComplexSubstanceOfEnvironmentalOriginFields = ({ fieldPath }) => (
  <>
    <MbdbVocabularyField
      vocabularyName="environment-types"
      fieldPath={`${fieldPath}.environment_type`}
    />
    <Location fieldPath={`${fieldPath}.location`} />
    <ComplexSubstanceCommonFields fieldPath={fieldPath} />
  </>
);

ComplexSubstanceOfEnvironmentalOriginFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
