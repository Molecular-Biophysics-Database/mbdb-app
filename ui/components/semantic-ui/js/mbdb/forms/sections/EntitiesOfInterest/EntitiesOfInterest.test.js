import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  clickOn,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  setStructuredUiModel,
  realUiModel,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ENTITY_SEEDS } from "@js/mbdb/forms/entities/seeds";
import { EntitiesOfInterestSectionComponent } from "./EntitiesOfInterest";
import { ENTITY_TYPE_ORDER } from "./entityTypes";
import { duplicateNames } from "./duplicateNames";

// buildUID lives in react-searchkit, whose d3 dependency (ESM) Jest cannot
// load. The section is the one module that imports it, so it is mocked here.
jest.mock("react-searchkit", () => ({
  buildUID: (prefix, id) => `${prefix}.${id}`,
}));

// The section composes every entity form, so the same one-fake-per-layer setup
// as the entity tests is needed; the shared factory feeds the structured
// `ui_model`.
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory
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

// Client-only row keys and entity ids (jsdom has no WebCrypto).
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const PATH = "metadata.general_parameters.entities_of_interest";

let container;

beforeEach(() => {
  setFakeVocabulary();
  setStructuredUiModel(realUiModel());
  setFakeUiModel({});
});

afterEach(() => {
  setStructuredUiModel();
  unmountForm(container);
  container = null;
});

const section = () => (
  <EntitiesOfInterestSectionComponent
    formConfig={{ overridableIdPrefix: "mbdb" }}
  />
);

const entities = (list) => ({
  metadata: { general_parameters: { entities_of_interest: list } },
});

const render = (list, opts = {}) =>
  renderInForm(
    <>
      {section()}
      <ValueProbe path={PATH} />
    </>,
    { initialValues: entities(list), ...opts }
  );

const addType = async (type) => {
  await clickOn(container.querySelector(".ui.dropdown"));
  const item = [...container.querySelectorAll(".menu .item")].find(
    (el) => el.textContent.trim() === type
  );
  await clickOn(item);
};

const rowCells = () => {
  const row = container.querySelector("tbody tr");
  return [...row.querySelectorAll("td")].map((td) => td.textContent.trim());
};

describe("EntitiesOfInterestSection", () => {
  it.each(ENTITY_TYPE_ORDER)(
    "Add %s writes the seed and an id",
    async (type) => {
      container = render(undefined);
      await addType(type);
      expect(readProbe(container)).toEqual([
        { type, ...(ENTITY_SEEDS[type] ?? {}), id: expect.any(String) },
      ]);
    }
  );

  it("a type change asks for confirmation and writes keep + new type + seed", async () => {
    container = render([
      {
        id: "e-1",
        type: "Polymer",
        name: "SigA",
        polymer_type: "polypeptide(L)",
      },
    ]);
    // Edit opens the entity modal; the type discriminator is its first dropdown
    await clickOn(
      [...container.querySelectorAll("button")].find(
        (b) => b.textContent === "Edit"
      )
    );
    const modal = document.body.querySelector(".ui.modal");
    const typeDropdown = modal.querySelector(".ui.dropdown");
    await clickOn(typeDropdown);
    const option = [...typeDropdown.querySelectorAll(".menu .item")].find(
      (el) => el.textContent.trim() === "Complex substance of chemical origin"
    );
    await clickOn(option);
    const confirm = [...document.body.querySelectorAll(".ui.modal")].find((m) =>
      m.textContent.includes("will be removed")
    );
    expect(confirm).toBeDefined();
    // not applied until confirmed
    expect(readProbe(container)[0].type).toBe("Polymer");
    await clickOn(
      [...confirm.querySelectorAll("button")].find(
        (b) => b.textContent === "Change"
      )
    );
    expect(readProbe(container)).toEqual([
      {
        id: "e-1",
        type: "Complex substance of chemical origin",
        class: "Lipid assembly",
      },
    ]);
  });

  it("does not offer to remove the only entity (minItems 1)", () => {
    container = render([{ id: "e-1", type: "Polymer", name: "SigA" }]);
    expect(container.querySelector('button[aria-label^="Remove "]')).toBeNull();
  });

  it("marks a duplicated name with a hint label on each row", () => {
    const serum = (id) => ({
      id,
      type: "Complex substance of biological origin",
      name: "Serum",
      derived_from: "Body fluid",
    });
    container = render([serum("e-1"), serum("e-2")]);
    const hints = [...container.querySelectorAll(".ui.label")].filter(
      (l) => l.textContent === "Duplicate name"
    );
    expect(hints).toHaveLength(2);
  });

  it("shows a row error count that survives an unrelated edit", async () => {
    container = render([{ id: "e-1", type: "Polymer", name: "SigA" }], {
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { name: "Missing data for required field." },
            ],
          },
        },
      },
      withUnrelatedField: true,
    });
    expect(container.textContent).toContain("1 error");
    await editUnrelatedField(container);
    expect(container.textContent).toContain("1 error");
  });
});

describe("Details column", () => {
  // one entity per type; the Details cell is the 4th cell (# / Name / Type /
  // Details). Vocabulary titles come from the mocked cache.
  const CASES = [
    [
      "Polymer",
      {
        type: "Polymer",
        name: "SigA",
        polymer_type: "polypeptide(L)",
        molecular_weight: { value: 43, unit: "kDa" },
      },
      "polypeptide(L), 43 kDa",
    ],
    [
      "Chemical",
      { type: "Chemical", name: "Water", basic_information: { id: "chem:1" } },
      "Water, H2O",
    ],
    [
      "Molecular assembly",
      {
        type: "Molecular assembly",
        name: "RNA polymerase",
        components: [{}, {}],
      },
      "2 components",
    ],
    [
      "Complex substance of biological origin",
      {
        type: "Complex substance of biological origin",
        name: "Human serum",
        derived_from: "Body fluid",
        source_organism: { id: "taxid:1" },
        fluid: { id: "bf:2" },
      },
      "Body fluid, Homo sapiens, Serum",
    ],
    [
      "Complex substance of environmental origin",
      {
        type: "Complex substance of environmental origin",
        name: "Brno pond water",
        environment_type: { id: "env:1" },
        location: { latitude: 49.2, longitude: 16.6 },
      },
      "Fresh water, 49.2, 16.6",
    ],
    [
      "Complex substance of chemical origin",
      {
        type: "Complex substance of chemical origin",
        name: "POPC liposomes",
        class: "Lipid assembly",
        assembly_type: "Liposome",
        components: [{}],
      },
      "Lipid assembly, Liposome, 1 component",
    ],
    [
      "Complex substance of industrial origin",
      {
        type: "Complex substance of industrial origin",
        name: "Whey sample",
        product: { id: "prod:1" },
      },
      "Whey",
    ],
  ];

  it.each(CASES)("shows the %s summary in Details", (_, entity, expected) => {
    setFakeVocabulary({
      "chemicals/chem:1": {
        title: "Water",
        customFields: { chemical_formula: "H2O" },
      },
      "organisms/taxid:1": { title: "Homo sapiens" },
      "body-fluids/bf:2": { title: "Serum" },
      "environment-types/env:1": { title: "Fresh water" },
      "products/prod:1": { title: "Whey" },
    });
    container = render([entity]);
    expect(rowCells()[3]).toBe(expected);
  });

  it("the expanded details do not repeat the row's Type and Name (P2-F1)", async () => {
    container = render([
      {
        id: "e-1",
        type: "Molecular assembly",
        name: "human Hemoglobin",
        molecular_weight: { value: 64.5, unit: "kDa" },
      },
    ]);
    await clickOn(
      container.querySelector('button[aria-label^="Show details of"]')
    );
    const details = container.querySelector(".mbdb-details");
    expect(details).not.toBeNull();
    // Type and Name are columns of the row above, so they are excluded
    expect(details.textContent).not.toContain("human Hemoglobin");
    expect(details.textContent).not.toContain("Molecular assembly");
    // ...but the entity's own fields are there
    expect(details.textContent).toContain("Molecular weight");
    expect(details.textContent).toContain("64.5 kDa");
  });
});

describe("ENTITY_TYPE_ORDER", () => {
  it("equals the model's Entity_base.type enum", () => {
    expect(ENTITY_TYPE_ORDER).toEqual(yamlEnum("Entity_base", "type"));
  });
});

describe("duplicateNames", () => {
  it.each([
    [[], []],
    [[{ name: "a" }, { name: "b" }], []],
    [[{ name: "a" }, { name: "a" }], ["a"]],
    [[{ name: "a" }, { name: "a" }, { name: "b" }], ["a"]],
    [[{ name: "a" }, { name: " a " }], ["a"]],
    [[{ name: "A" }, { name: "a" }], []],
    [[{}, { name: "  " }], []],
  ])("duplicateNames(%#)", (list, expected) => {
    expect([...duplicateNames(list)]).toEqual(expected);
  });
});
