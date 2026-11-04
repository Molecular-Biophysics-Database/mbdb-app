import React from "react";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";
import { FUNDING_REFERENCES_PATH } from "./path";

// The group spec of one funding reference, read by the details view (guide
// §8). Funder and award are vocabulary references, so they declare their
// vocabularies.
export const FUNDING_REFERENCE_GROUPS = [
  {
    title: "Funding reference",
    fields: [
      { field: "funder", vocabulary: "funders" },
      { field: "award", vocabulary: "awards" },
    ],
  },
];

// The funding references: one row per grant in a summary table, each edited
// in a modal with the Funder and Award number pickers (OpenAIRE-based
// vocabularies). Label and help come from the model.
export const FundingReferences = () => (
  <ModalArrayField
    fieldPath={FUNDING_REFERENCES_PATH}
    itemLabel={() => "Funding reference"}
    newItemOptions={[{ label: "funding reference", value: {} }]}
    columns={[
      {
        label: "Funder",
        value: (v) =>
          v?.funder?.id ? (
            <VocabularyValue vocabulary="funders" value={v.funder} />
          ) : (
            ""
          ),
      },
      {
        label: "Award",
        value: (v) =>
          v?.award?.id ? (
            <VocabularyValue vocabulary="awards" value={v.award} />
          ) : (
            ""
          ),
      },
    ]}
    detailGroups={FUNDING_REFERENCE_GROUPS}
    renderForm={(itemPath) => (
      <>
        <MbdbVocabularyField
          fieldPath={`${itemPath}.funder`}
          vocabularyName="funders"
        />
        <MbdbVocabularyField
          fieldPath={`${itemPath}.award`}
          vocabularyName="awards"
        />
      </>
    )}
  />
);
