import { joinParts } from "@js/mbdb/forms/entities/summary";

// "3 components" / "1 component"; "" when the list has no item.
const componentCount = (components) => {
  const n = components?.length;
  if (!n) return "";
  return `${n} component${n === 1 ? "" : "s"}`;
};

// Text of the entity table's "Details" column: the (fixed) class, the assembly
// type and the component count, e.g. `Lipid assembly, Liposome, 3 components`.
// Missing parts are left out (joinParts).
export const summaryChemicalOrigin = (value) =>
  joinParts([
    value?.class,
    value?.assembly_type,
    componentCount(value?.components),
  ]);
