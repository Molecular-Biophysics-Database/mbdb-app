// Unit enums copied from the model YAML; shared because several model types
// (storage, measurement conditions of other tabs) use them. Equality is
// tested with yamlEnum — do not retype.

// TEMPERATURE_UNITS (`°` is U+00B0, the degree sign)
export const TEMPERATURE_UNITS = ["K", "°C", "°F"];

// TIME_UNITS
export const TIME_UNITS = [
  "nanoseconds",
  "microseconds",
  "milliseconds",
  "seconds",
  "minutes",
  "hours",
  "days",
  "months",
  "years",
];

// CONCENTRATION_UNITS (`µ` is U+00B5, the micro sign)
export const CONCENTRATION_UNITS = [
  "M",
  "mM",
  "µM",
  "nM",
  "pM",
  "fM",
  "aM",
  "g/L",
  "mg/mL",
  "µg/mL",
  "ng/mL",
  "mol/kg",
  "mmol/kg",
  "v/v %",
  "w/w %",
  "v/w %",
  "w/v %",
  "U/ml",
  "% saturated",
];

// ENERGY_UNITS
export const ENERGY_UNITS = ["kcal/mol", "kJ/mol"];
