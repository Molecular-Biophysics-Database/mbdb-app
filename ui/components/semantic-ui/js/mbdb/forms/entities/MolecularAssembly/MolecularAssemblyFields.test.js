import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  typeInto,
  clickOn,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  setStructuredUiModel,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import {
  MolecularAssemblyFields,
  MOLECULAR_ASSEMBLY_GROUPS,
  summaryMolecularAssembly,
} from "./index";

// One fake per layer: the picker needs the network. The shared blocks under
// test (MolecularWeight, Components, ExternalDatabases, Modifications,
// QualityControls, …) stay real; the shared factory feeds the structured
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

// Client-only row keys (jsdom has no WebCrypto).
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const COMPONENTS = `${ENTITY}.components`;

let container;

beforeEach(() => {
  setFakeVocabulary();
  setStructuredUiModel();
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const entity = (fields = {}) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [{ type: "Molecular assembly", ...fields }],
    },
  },
});

const FILLED = {
  name: "human Hemoglobin",
  molecular_weight: { value: 64.5, unit: "kDa" },
  external_databases: ["pdb:2HCO"],
  components: [
    { type: "Polymer", name: "Hemoglobin subunit alpha", copy_number: 2 },
    { type: "Polymer", name: "Hemoglobin subunit beta", copy_number: 2 },
  ],
  chemical_modifications: [{ type: "Acetylation", position: "K1" }],
  quality_controls: {
    purity: { assessed: "Yes", method: "SDS-PAGE", purity_percentage: ">99 %" },
    homogeneity: { assessed: "No" },
  },
  additional_specifications: ["Freshly prepared"],
};

const fields = (path = ENTITY) => <MolecularAssemblyFields fieldPath={path} />;

const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);

// portals stack in creation order: [outer, inner, ...]
const modals = () => [...document.body.querySelectorAll(".ui.modal")];
const modal = () => modals()[0] ?? null;
const modalButtonIn = (m, label) =>
  [...m.querySelectorAll("button")].find((b) => b.textContent === label);
const buttonIn = (root, label) =>
  [...root.querySelectorAll("button")].find((b) => b.textContent === label);

const addOption = async (label) => {
  await clickOn(container.querySelector(".ui.dropdown"));
  const item = [...container.querySelectorAll(".menu .item")].find(
    (el) => el.textContent === label
  );
  await clickOn(item);
};

describe("MolecularAssemblyFields", () => {
  it("renders the filled fixture at the entity paths", () => {
    container = renderInForm(fields(), { initialValues: entity(FILLED) });
    // Molecular weight
    expect(document.getElementById(`${ENTITY}.molecular_weight`).value).toBe(
      "64.5"
    );
    // Components: the summary rows of the components table
    expect(container.textContent).toContain("Hemoglobin subunit alpha");
    expect(container.textContent).toContain("Hemoglobin subunit beta");
    // External databases (parsed into a database select + an id input)
    expect(hasInputValue("2HCO")).toBe(true);
    // Chemical modifications (free-text cells)
    expect(hasInputValue("Acetylation")).toBe(true);
    expect(hasInputValue("K1")).toBe(true);
    // Quality controls
    expect(container.textContent).toContain("Purity");
    expect(container.textContent).toContain("SDS-PAGE");
    // Additional specifications
    expect(container.textContent).toContain("Freshly prepared");
  });

  it("shows a field-level error and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(FILLED),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { molecular_weight: "Missing data for required field." },
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

  it("shows a list-level error on components and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity({ name: "human Hemoglobin" }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { components: "Missing data for required field." },
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

  it("Add → Polymer writes { type: 'Polymer' } (no id) at the entity path", async () => {
    container = renderInForm(
      <>
        {fields()}
        <ValueProbe path={COMPONENTS} />
      </>,
      { initialValues: entity() }
    );
    await addOption("Polymer");
    expect(readProbe(container)).toEqual([{ type: "Polymer" }]);
  });

  it("depth 2: Cancel on a component restores it and keeps the entity modal open", async () => {
    container = renderInForm(
      <>
        <ModalArrayField
          fieldPath="entities"
          label="Entities"
          itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
          columns={[{ label: "Name", value: (v) => v.name }]}
          renderForm={(p) => <MolecularAssemblyFields fieldPath={p} />}
        />
        <ValueProbe path="entities" />
      </>,
      {
        initialValues: {
          entities: [
            {
              type: "Molecular assembly",
              name: "RNA polymerase",
              components: [{ type: "Polymer", name: "alpha", copy_number: 1 }],
            },
          ],
        },
      }
    );
    await clickOn(buttonIn(container, "Edit"));
    expect(modal().textContent).toContain("Edit entity: RNA polymerase");
    await clickOn(buttonIn(modal(), "Edit"));
    expect(modals()).toHaveLength(2);
    const inner = () => modals()[1];
    await typeInto(
      inner().querySelector('input[name="entities.0.components.0.name"]'),
      "renamed"
    );
    expect(readProbe(container)[0].components[0].name).toBe("renamed");
    await clickOn(modalButtonIn(inner(), "Cancel"));
    // only the component edit is undone; the entity modal stays open
    expect(modals()).toHaveLength(1);
    expect(readProbe(container)[0].components[0].name).toBe("alpha");
  });
});

describe("summaryMolecularAssembly", () => {
  it("joins the component count and the molecular weight", () => {
    container = renderInForm(
      <>
        {summaryMolecularAssembly({
          components: [{}, {}],
          molecular_weight: { value: 64.5, unit: "kDa" },
        })}
      </>,
      {}
    );
    expect(container.textContent).toBe("2 components, 64.5 kDa");
  });

  it("uses the singular for one component and returns '' for an empty entity", () => {
    container = renderInForm(
      <>
        {summaryMolecularAssembly({
          components: [{}],
          molecular_weight: { value: 16, unit: "kDa" },
        })}
      </>,
      {}
    );
    expect(container.textContent).toBe("1 component, 16 kDa");
    expect(summaryMolecularAssembly({})).toBe("");
  });
});

describe("MOLECULAR_ASSEMBLY_GROUPS", () => {
  it("lists only fields that exist on the Molecular_assembly model type", () => {
    for (const group of MOLECULAR_ASSEMBLY_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        expect(yamlProperty("Molecular_assembly", name)).toBe(true);
      }
    }
  });
});
