import { ENTITY_TYPES } from "./entityTypes";
import { yamlProperties } from "@js/mbdb/forms/building-blocks/testUtils";

// The entity-type Fields import blocks whose chain reaches the ESM-only
// sanitize-html / oarepo modules Jest cannot load; the canonical fakes break
// it. Only the group SPECS are read here (nothing is rendered).
// eslint-disable-next-line no-restricted-syntax -- canonical shared fakes (§8)
jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
);
jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyField()
);
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyTitles()
);
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

// id/name/type are the row's own columns, never group fields.
const COMMON = ["id", "name", "type"];

const fieldNames = (groups) =>
  groups.flatMap((group) =>
    (group.fields ?? []).map((entry) =>
      typeof entry === "string" ? entry : entry.field
    )
  );

// Every model field of the type (minus the row columns) must be in its groups;
// that is what keeps the details' "Other" section empty (rule 6).
const missingFields = (modelTypes, groups) => {
  const covered = new Set(fieldNames(groups));
  return modelTypes
    .flatMap((t) => yamlProperties(t))
    .filter((f) => !COMMON.includes(f) && !covered.has(f));
};

const TYPES = [
  ["Polymer", ["Polymer"]],
  ["Chemical", ["Chemical"]],
  ["Molecular assembly", ["Molecular_assembly"]],
  [
    "Complex substance of environmental origin",
    ["Complex_substance_of_environmental_origin"],
  ],
  [
    "Complex substance of industrial origin",
    ["Complex_substance_of_industrial_origin"],
  ],
  [
    "Complex substance of chemical origin",
    ["Complex_substance_of_chemical_origin_base", "Lipid_assembly"],
  ],
];

// the biological origin's groups depend on `derived_from`; the model fields are
// the base plus that sub-type's.
const BIO_SUBTYPES = {
  "Body fluid": "Body_fluid",
  "Cell fraction": "Cell_fraction",
  Virion: "Virion",
  "Solid tissue sample": "Solid_tissue_sample",
};

describe("entity group specs cover every model field (review-mode rule 6)", () => {
  TYPES.forEach(([type, modelTypes]) => {
    it(`${type}: every model field is in its group spec`, () => {
      expect(missingFields(modelTypes, ENTITY_TYPES[type].groups({}))).toEqual(
        []
      );
    });
  });

  Object.entries(BIO_SUBTYPES).forEach(([derivedFrom, modelType]) => {
    it(`Complex substance of biological origin (${derivedFrom})`, () => {
      const groups = ENTITY_TYPES[
        "Complex substance of biological origin"
      ].groups({ derived_from: derivedFrom });
      expect(
        missingFields(
          ["Complex_substance_of_biological_origin_base", modelType],
          groups
        )
      ).toEqual([]);
    });
  });
});
