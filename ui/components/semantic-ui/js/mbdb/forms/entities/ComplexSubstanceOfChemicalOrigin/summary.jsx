import { componentCount, joinParts } from "@js/mbdb/forms/entities/summary";

// Text of the entity table's "Details" column: the (fixed) class, the assembly
// type and the component count, e.g. `Lipid assembly, Liposome, 3 components`.
// Missing parts are left out (joinParts).
export const summaryChemicalOrigin = (value) =>
  joinParts([
    value?.class,
    value?.assembly_type,
    componentCount(value?.components),
  ]);
