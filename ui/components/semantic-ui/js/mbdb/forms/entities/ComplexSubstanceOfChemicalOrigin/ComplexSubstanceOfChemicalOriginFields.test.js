import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  editUnrelatedField,
  setStructuredUiModel,
  realUiModel,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import {
  ComplexSubstanceOfChemicalOriginFields,
  CHEMICAL_ORIGIN_GROUPS,
  summaryChemicalOrigin,
} from "./index";

// One fake per layer: the picker needs the network. The shared blocks under
// test (LipidAssemblyDetails, Components, Protocol, Storage, the common block)
// stay real; the shared factory feeds the structured `ui_model`.
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory (plan 3R X6)
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

// Client-only row keys (jsdom has no WebCrypto); plan 3R X6.
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";

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

const entity = (fields = {}) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        { type: "Complex substance of chemical origin", ...fields },
      ],
    },
  },
});

const FILLED = {
  name: "POPC liposomes",
  class: "Lipid assembly",
  assembly_type: "Liposome",
  number_of_mono_layers: 2,
  size: { type: "diameter", unit: "nm", mean: 120, lower: 90, upper: 150 },
  components: [{ type: "Chemical", name: "POPC", copy_number: 120 }],
  preparation_protocol: [
    { name: "Extrusion", description: "21 passes through a 100 nm membrane" },
  ],
};

const fields = () => (
  <ComplexSubstanceOfChemicalOriginFields fieldPath={ENTITY} />
);

const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);

describe("ComplexSubstanceOfChemicalOriginFields", () => {
  it("renders the class text and the lipid assembly fields", () => {
    container = renderInForm(fields(), { initialValues: entity(FILLED) });
    expect(container.textContent).toContain("Class: Lipid assembly");
    expect(container.textContent).toContain("Liposome");
    expect(hasInputValue("2")).toBe(true); // number of mono layers
    expect(hasInputValue("120")).toBe(true); // size mean
    // the components table row and the common block (Protocol)
    expect(container.textContent).toContain("POPC");
    expect(hasInputValue("Extrusion")).toBe(true);
  });

  it("shows a warning label when class is missing", () => {
    container = renderInForm(fields(), {
      initialValues: entity({ name: "POPC liposomes" }),
    });
    expect(container.textContent).toContain("Class missing");
  });

  it("shows a field-level error and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(FILLED),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { assembly_type: "Missing data for required field." },
            ],
          },
        },
      },
      withUnrelatedField: true,
    });
    const messages = () =>
      [...container.querySelectorAll(".ui.pointing.prompt.label")].map(
        (l) => l.textContent
      );
    expect(messages()).toContain("Missing data for required field.");
    await editUnrelatedField(container);
    expect(messages()).toContain("Missing data for required field.");
  });
});

describe("summaryChemicalOrigin", () => {
  it("joins the class, the assembly type and the component count", () => {
    container = renderInForm(<>{summaryChemicalOrigin(FILLED)}</>, {});
    expect(container.textContent).toBe("Lipid assembly, Liposome, 1 component");
  });

  it("returns '' for an empty entity", () => {
    expect(summaryChemicalOrigin({})).toBe("");
  });
});

describe("CHEMICAL_ORIGIN_GROUPS", () => {
  it("lists only fields that exist on the model types", () => {
    // class and the common fields live on the chemical-origin base, the
    // assembly fields on Lipid_assembly
    const MODEL_TYPE = {
      assembly_type: "Lipid_assembly",
      number_of_mono_layers: "Lipid_assembly",
      size: "Lipid_assembly",
      components: "Lipid_assembly",
    };
    for (const group of CHEMICAL_ORIGIN_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        const type =
          MODEL_TYPE[name] ?? "Complex_substance_of_chemical_origin_base";
        expect(yamlProperty(type, name)).toBe(true);
      }
    }
  });
});
