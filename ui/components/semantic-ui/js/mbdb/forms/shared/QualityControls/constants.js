// Enums copied from the YAML (design QualityControls / Purity / Identity /
// Homogeneity) — equality is tested with yamlEnum, do not retype here.

// Purity_base/Identity_base/Homogeneity_base `assessed` (quoted strings in
// the YAML: these are strings, not booleans)
export const ASSESSED = ["Yes", "No"];

// Yes_purity.method
export const PURITY_METHODS = [
  "SDS-PAGE",
  "Capillary Electrophoresis",
  "Agarose Gel electrophoresis",
];

// Yes_purity.purity_percentage (the space before % is part of the value)
export const PURITY_PERCENTAGES = ["<90 %", ">90 %", ">95 %", ">99 %"];

// By_intact_mass.method
export const INTACT_MASS_METHODS = ["Mass spectrometry", "SDS-PAGE"];

// By_sequencing.method
export const SEQUENCING_METHODS = [
  "Mass spectrometry-Mass spectrometry",
  "Edman degradation",
  "Sanger sequencing",
  "Next generation sequencing",
];

// By_fingerprinting.method
export const FINGERPRINTING_METHODS = [
  "Protease digest + Mass spectrometry",
  "Restriction enzyme digest + Gel electrophoresis",
];

// Yes_homogeneity.method ("Dynamic light scattering" is new in the model)
export const HOMOGENEITY_METHODS = [
  "Dynamic light scattering",
  "Size exclusion chromatography",
  "Native Gel Electrophoresis",
  "Mass photometry",
];
