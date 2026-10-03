// The group spec every complex-substance type appends to its own groups
// (`[...X_GROUPS_OWN, ...COMPLEX_SUBSTANCE_COMMON_GROUPS]`), so the trailing
// block is the same everywhere (design ComplexSubstanceCommon). The title is a
// UI grouping with no model field behind it, so it is literal; the fields are
// the model's own names.
export const COMPLEX_SUBSTANCE_COMMON_GROUPS = [
  {
    title: "Preparation and storage",
    fields: ["preparation_protocol", "storage", "additional_specifications"],
  },
];
