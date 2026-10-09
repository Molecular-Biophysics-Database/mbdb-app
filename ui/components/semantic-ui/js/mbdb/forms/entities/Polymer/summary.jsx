import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { joinParts, vocabularyPart } from "@js/mbdb/forms/entities/summary";

// Text of the entity table's "Details" column: polymer type, molecular weight
// and the source organism title, for example
// `polypeptide(L), 43 kDa, Bacillus subtilis`. Missing parts are left out
// (joinParts). The vocabulary title comes from the shared cache through
// `vocabularyPart` — never a hook in summaryPolymer itself.
export const summaryPolymer = (value) =>
  joinParts([
    value?.polymer_type,
    valueUnitText(value?.molecular_weight),
    vocabularyPart("organisms", value?.source_organism),
  ]);
