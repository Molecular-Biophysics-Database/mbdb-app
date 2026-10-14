import { COMPLEX_SUBSTANCE_COMMON_GROUPS } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";
import { LIPID_ASSEMBLY_GROUPS } from "@js/mbdb/forms/shared/LipidAssemblyDetails";

// The group spec of the complex substance of chemical origin: the fixed class,
// the lipid assembly fields, then the common complex-substance groups. The form
// and its DetailView read it (guide §8).
export const CHEMICAL_ORIGIN_GROUPS = [
  { title: "Class", fields: ["class"] },
  ...LIPID_ASSEMBLY_GROUPS,
  ...COMPLEX_SUBSTANCE_COMMON_GROUPS,
];
