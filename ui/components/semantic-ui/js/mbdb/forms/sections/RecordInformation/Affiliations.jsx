import React from "react";
import PropTypes from "prop-types";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";

// The affiliations of one person: an array of ROR vocabulary references,
// edited one pick per modal. The picker's label/help are passed explicitly:
// the picker sits AT the array-item path, where the ui_model resolves the
// item node (an empty label), not the affiliations field's own texts.
export const Affiliations = ({ fieldPath }) => (
  <ModalArrayField
    fieldPath={fieldPath}
    itemLabel={() => "Affiliation"}
    newItemOptions={[{ label: "affiliation", value: {} }]}
    columns={[
      {
        label: "Affiliation",
        value: (v) =>
          v?.id ? <VocabularyValue vocabulary="affiliations" value={v} /> : "",
      },
    ]}
    renderForm={(itemPath) => (
      <MbdbVocabularyField
        fieldPath={itemPath}
        vocabularyName="affiliations"
        label="Affiliation"
        help="The affiliation of the person. Note that this is based on the Research Organization Registry (ROR)"
      />
    )}
  />
);

Affiliations.propTypes = {
  // the affiliations ARRAY path (`${personPath}.affiliations`)
  fieldPath: PropTypes.string.isRequired,
};
