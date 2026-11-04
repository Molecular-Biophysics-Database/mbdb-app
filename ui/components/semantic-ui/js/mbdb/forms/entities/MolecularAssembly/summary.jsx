import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { componentCount, joinParts } from "@js/mbdb/forms/entities/summary";

// Text of the entity table's "Details" column: the component count and the
// molecular weight, for example `2 components, 64.5 kDa`. Missing parts are
// left out (joinParts); "" for an empty entity. A plain function called inside
// a map, so no hooks here.
export const summaryMolecularAssembly = (value) =>
  joinParts([
    componentCount(value?.components),
    valueUnitText(value?.molecular_weight),
  ]);
