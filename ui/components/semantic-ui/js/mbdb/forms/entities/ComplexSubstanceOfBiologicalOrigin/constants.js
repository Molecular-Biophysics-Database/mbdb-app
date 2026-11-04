// Enums copied from the YAML (design ComplexSubstanceOfBiologicalOrigin and the
// four sub-type docs; guide §6). Equality is tested with yamlEnum, do not
// retype here.

// Complex_substance_of_biological_origin_base.derived_from
export const DERIVED_FROM = [
  "Body fluid",
  "Cell fraction",
  "Virion",
  "Solid tissue sample",
];

// Virion.genetic_material
export const VIRION_GENETIC_MATERIAL = [
  "No genetic material",
  "Virus genome",
  "Synthetic",
];

// Virion.capsid_type and Virion.envelope_type (the same list)
export const VIRION_PARTICLE_TYPES = [
  "None",
  "Native",
  "Genetically Engineered",
  "Synthetic",
];
