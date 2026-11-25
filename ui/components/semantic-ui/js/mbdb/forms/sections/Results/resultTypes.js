import { LENGTH_UNITS } from "@js/mbdb/forms/shared/Size/constants";
import { MOLECULAR_WEIGHT_UNITS } from "@js/mbdb/forms/shared/MolecularWeight";
import { CONCENTRATION_UNITS, ENERGY_UNITS } from "@js/mbdb/forms/shared/units";

const PREFIXES = ["M", "mM", "µM", "nM"];
const withPowers = (suffixes) =>
  PREFIXES.flatMap((prefix) => suffixes.map((suffix) => `${prefix}${suffix}`));

// The order of rdm-12's type menu and the units of each type (the model's
// enums; tested against the YAML). Stoichiometry has no value of its own.
export const RESULT_UNITS = {
  Concentration: CONCENTRATION_UNITS,
  Stoichiometry: null,
  "Constant of association KA": withPowers(["^-1", "^-2"]),
  "Constant of dissociation KD": withPowers(["", "^2"]),
  "Association rate kOn": withPowers(["^-1 s^-1", "^-2 s^-1"]),
  "Dissociation rate kOff": ["s^-1"],
  "Change in enthalpy deltaH": ENERGY_UNITS,
  "Change in entropy deltaS": ["kcal/molK", "kJ/molK"],
  "Change in Gibbs free energy deltaG": ENERGY_UNITS,
  "Molecular weight": MOLECULAR_WEIGHT_UNITS,
  "Half maximal effective concentration EC50": CONCENTRATION_UNITS,
  "Hill coefficient": ["unitless"],
  "Correction of active concentration": ["unitless"],
  "Size of spherically represented entity": LENGTH_UNITS,
};

export const RESULT_TYPE_ORDER = Object.keys(RESULT_UNITS);

export const SIZE_RESULT_TYPE = "Size of spherically represented entity";
export const SIZE_TYPES = ["Radius", "Diameter"];

// A type with a single possible unit gets it on create and on a type change.
export const resultSeed = (type) =>
  RESULT_UNITS[type]?.length === 1 ? { unit: RESULT_UNITS[type][0] } : {};
