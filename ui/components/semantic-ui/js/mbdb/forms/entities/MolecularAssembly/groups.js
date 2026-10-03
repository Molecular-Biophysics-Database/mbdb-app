// The group spec of the Molecular assembly entity. The entity form and its
// DetailView both read it (guide §8). None of its fields is a vocabulary
// reference, so every entry is a plain field name. The titles are the model
// labels of the named fields (a DetailView group needs a string title).
export const MOLECULAR_ASSEMBLY_GROUPS = [
  { title: "Molecular weight", fields: ["molecular_weight"] },
  { title: "Components", fields: ["components"] },
  { title: "External databases", fields: ["external_databases"] },
  { title: "Chemical modifications", fields: ["chemical_modifications"] },
  { title: "Quality controls", fields: ["quality_controls"] },
  { title: "Additional specifications", fields: ["additional_specifications"] },
];
