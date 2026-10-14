import { COMPLEX_SUBSTANCE_COMMON_GROUPS } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";

// The group spec of the complex substance of industrial origin: its own
// `product` vocabulary field, then the common complex-substance groups. The
// form and its DetailView read it (guide §8). The title is the model label of
// the group's one field.
export const INDUSTRIAL_ORIGIN_GROUPS = [
  { title: "Product", fields: [{ field: "product", vocabulary: "products" }] },
  ...COMPLEX_SUBSTANCE_COMMON_GROUPS,
];
