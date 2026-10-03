import React from "react";
import {
  VocabularyValue,
  valueUnitText,
} from "@js/mbdb/forms/building-blocks/DetailView/values";
import { joinParts } from "@js/mbdb/forms/entities/summary";

// Text of the entity table's "Details" column: polymer type, molecular weight
// and the source organism title, for example
// `polypeptide(L), 43 kDa, Bacillus subtilis`. Missing parts are left out
// (joinParts). The vocabulary title comes from the shared cache through
// `VocabularyValue`, a component — never a hook in summaryPolymer itself
// (plan step 4).
export const summaryPolymer = (value) =>
  joinParts([
    value?.polymer_type,
    valueUnitText(value?.molecular_weight),
    value?.source_organism ? (
      <VocabularyValue vocabulary="organisms" value={value.source_organism} />
    ) : (
      ""
    ),
  ]);
