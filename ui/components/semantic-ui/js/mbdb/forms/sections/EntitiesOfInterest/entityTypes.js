import {
  PolymerFields,
  POLYMER_GROUPS,
  summaryPolymer,
} from "@js/mbdb/forms/entities/Polymer";
import {
  ChemicalFields,
  CHEMICAL_GROUPS,
  summaryChemical,
} from "@js/mbdb/forms/entities/Chemical";
import {
  MolecularAssemblyFields,
  MOLECULAR_ASSEMBLY_GROUPS,
  summaryMolecularAssembly,
} from "@js/mbdb/forms/entities/MolecularAssembly";
import {
  ComplexSubstanceOfBiologicalOriginFields,
  biologicalOriginGroups,
  summaryBiologicalOrigin,
} from "@js/mbdb/forms/entities/ComplexSubstanceOfBiologicalOrigin";
import {
  ComplexSubstanceOfEnvironmentalOriginFields,
  ENVIRONMENTAL_ORIGIN_GROUPS,
  summaryEnvironmentalOrigin,
} from "@js/mbdb/forms/entities/ComplexSubstanceOfEnvironmentalOrigin";
import {
  ComplexSubstanceOfChemicalOriginFields,
  CHEMICAL_ORIGIN_GROUPS,
  summaryChemicalOrigin,
} from "@js/mbdb/forms/entities/ComplexSubstanceOfChemicalOrigin";
import {
  ComplexSubstanceOfIndustrialOriginFields,
  INDUSTRIAL_ORIGIN_GROUPS,
  summaryIndustrialOrigin,
} from "@js/mbdb/forms/entities/ComplexSubstanceOfIndustrialOrigin";

// The order of the model's `type` enum; the order of the Add menu and of a type
// change. The seven values match the model, do not retype elsewhere.
export const ENTITY_TYPE_ORDER = [
  "Polymer",
  "Chemical",
  "Molecular assembly",
  "Complex substance of biological origin",
  "Complex substance of environmental origin",
  "Complex substance of chemical origin",
  "Complex substance of industrial origin",
];

// A fixed group spec as a function of the item, so every type has one signature
// (the biological origin's groups depend on `derived_from`).
const fixedGroups = (groups) => () => groups;

// The only place that knows all seven entity types: for each, the modal form,
// the details groups (`groups(value)`) and the "Details" summary. `Fields` is
// the composition the entity doc defines, called at the entity item path.
// `noun` is the short name a *nested* modal's Done button returns to ("Done,
// back to assembly", design ModalArrayField.md "where am I in stacked modals").
export const ENTITY_TYPES = {
  Polymer: {
    Fields: PolymerFields,
    groups: fixedGroups(POLYMER_GROUPS),
    summary: summaryPolymer,
    noun: "polymer",
  },
  Chemical: {
    Fields: ChemicalFields,
    groups: fixedGroups(CHEMICAL_GROUPS),
    summary: summaryChemical,
    noun: "chemical",
  },
  "Molecular assembly": {
    Fields: MolecularAssemblyFields,
    groups: fixedGroups(MOLECULAR_ASSEMBLY_GROUPS),
    summary: summaryMolecularAssembly,
    noun: "assembly",
  },
  "Complex substance of biological origin": {
    Fields: ComplexSubstanceOfBiologicalOriginFields,
    groups: biologicalOriginGroups,
    summary: summaryBiologicalOrigin,
    noun: "substance",
  },
  "Complex substance of environmental origin": {
    Fields: ComplexSubstanceOfEnvironmentalOriginFields,
    groups: fixedGroups(ENVIRONMENTAL_ORIGIN_GROUPS),
    summary: summaryEnvironmentalOrigin,
    noun: "substance",
  },
  "Complex substance of chemical origin": {
    Fields: ComplexSubstanceOfChemicalOriginFields,
    groups: fixedGroups(CHEMICAL_ORIGIN_GROUPS),
    summary: summaryChemicalOrigin,
    noun: "substance",
  },
  "Complex substance of industrial origin": {
    Fields: ComplexSubstanceOfIndustrialOriginFields,
    groups: fixedGroups(INDUSTRIAL_ORIGIN_GROUPS),
    summary: summaryIndustrialOrigin,
    noun: "substance",
  },
};
