import { COMPLEX_SUBSTANCE_COMMON_GROUPS } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";

// The group spec of the complex substance of environmental origin: the
// environment type and the sampling location, then the common complex-substance
// groups. The form and its DetailView read it (guide §8). `environment_type` is
// a vocabulary reference; `location` is a plain nested object.
export const ENVIRONMENTAL_ORIGIN_GROUPS = [
  {
    title: "Environment",
    fields: [
      { field: "environment_type", vocabulary: "environment-types" },
      "location",
    ],
  },
  ...COMPLEX_SUBSTANCE_COMMON_GROUPS,
];
