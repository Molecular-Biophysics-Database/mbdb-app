import { COMPLEX_SUBSTANCE_COMMON_GROUPS } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";

// The group specs of the biological origin and its four sub-types. They are
// read by the form's details view (guide §8). The sub-type groups are per
// derived_from, so the whole spec is a function of the item value.

export const BODY_FLUID_GROUPS = [
  {
    title: "Body fluid",
    fields: [{ field: "fluid", vocabulary: "body-fluids" }, "health_status"],
  },
];

export const CELL_FRACTION_GROUPS = [
  {
    title: "Cell fraction",
    fields: [
      { field: "fraction", vocabulary: "cell-fractions" },
      "health_status",
      "organ",
      "tissue",
      "cell_type",
    ],
  },
];

export const VIRION_GROUPS = [
  {
    title: "Virion characteristics",
    fields: ["genetic_material", "capsid_type", "envelope_type"],
  },
  {
    title: "Host",
    fields: [
      { field: "host_organism", vocabulary: "organisms" },
      "host_cell_type",
    ],
  },
];

export const SOLID_TISSUE_GROUPS = [
  {
    title: "Solid tissue sample",
    fields: ["organ", "health_status", "homogenized"],
  },
];

const SUBTYPE_GROUPS = {
  "Body fluid": BODY_FLUID_GROUPS,
  "Cell fraction": CELL_FRACTION_GROUPS,
  Virion: VIRION_GROUPS,
  "Solid tissue sample": SOLID_TISSUE_GROUPS,
};

// The full group spec for one biological-origin entity: the origin fields, the
// picked sub-type's groups (looked up the same way the form looks up its fields)
// and the common complex-substance groups. `value` is the entity item.
export const biologicalOriginGroups = (value) => [
  {
    title: "Origin",
    fields: [
      "derived_from",
      { field: "source_organism", vocabulary: "organisms" },
    ],
  },
  ...(SUBTYPE_GROUPS[value?.derived_from] ?? []),
  ...COMPLEX_SUBSTANCE_COMMON_GROUPS,
];
