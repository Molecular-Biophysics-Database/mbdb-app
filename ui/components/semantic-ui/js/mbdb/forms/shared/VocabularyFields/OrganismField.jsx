import React from "react";
import PropTypes from "prop-types";
import { MbdbVocabularyField } from "./MbdbVocabularyField";
import { describeOrganism } from "./describers";

// Organism picker with the taxonomic rank next to each option. The other
// vocabularies need no wrapper of their own; use MbdbVocabularyField with
// the vocabulary type directly.
export const OrganismField = (props) => (
  <MbdbVocabularyField
    vocabularyName="organisms"
    describe={describeOrganism}
    {...props}
  />
);

OrganismField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.node,
  help: PropTypes.node,
  required: PropTypes.bool,
};
