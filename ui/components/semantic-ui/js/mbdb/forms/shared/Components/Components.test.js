import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  setFakeVocabularyPicks,
  clickOn,
  typeInto,
  ValueProbe,
  readProbe,
  setStructuredUiModel,
  realUiModel,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { Components, COMPONENT_TYPES } from "./index";

// One fake per layer: the picker needs the network. The real leaves
// (PolymerFields, ChemicalFields, Modifications, QualityControls, the modal
// blocks) stay real; the shared factory feeds the structured `ui_model`.
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory
jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
);

// The real wrapper shows the field's merged error under the dropdown; the fake
// does the same through the shared helper, so an object-level error at
// `basic_information` still surfaces in the modal.
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

// jsdom has no WebCrypto; client-only row keys.
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const PATH = `${ENTITY}.components`;

let container;

beforeEach(() => {
  setFakeVocabulary();
  setFakeVocabularyPicks();
  setStructuredUiModel();
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const assembly = (components) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Molecular assembly",
          name: "RNA polymerase",
          ...(components === undefined ? {} : { components }),
        },
      ],
    },
  },
});

const render = (opts) => {
  container = renderInForm(
    <>
      <Components fieldPath={PATH} />
      <ValueProbe path={PATH} />
    </>,
    opts
  );
  return container;
};

const probe = () => readProbe(container);

// portals stack in creation order: [outer, inner, ...]
const modals = () => [...document.body.querySelectorAll(".ui.modal")];
const modal = () => modals()[0] ?? null;
const modalButtonIn = (m, label) =>
  [...m.querySelectorAll("button")].find((b) => b.textContent === label);
const modalButton = (label) => modalButtonIn(modal(), label);

const buttonIn = (root, label) =>
  [...root.querySelectorAll("button")].find((b) => b.textContent === label);

const addOption = async (label) => {
  await clickOn(container.querySelector(".ui.dropdown"));
  const item = [...container.querySelectorAll(".menu .item")].find(
    (el) => el.textContent === label
  );
  await clickOn(item);
};

describe("COMPONENT_TYPES", () => {
  it("equals the model enum", () => {
    expect(COMPONENT_TYPES).toEqual(
      yamlEnum("Assembly_component_base", "type")
    );
  });
});

describe("Components", () => {
  it("Add → Polymer writes { type: 'Polymer' } (no id) and opens the modal with the polymer fields", async () => {
    render({ initialValues: assembly(undefined) });
    await addOption("Polymer");
    expect(probe()).toEqual([{ type: "Polymer" }]);
    expect(modal()).not.toBeNull();
    // a nameless new component: the header comes from itemLabel
    expect(modal().textContent).toContain("New Polymer component");
    // the polymer field set is mounted inside the component modal
    expect(modal().textContent).toContain("Polymer type");
  });

  it("Add → Chemical opens the modal with the chemical fields", async () => {
    render({ initialValues: assembly(undefined) });
    await addOption("Chemical");
    expect(probe()).toEqual([{ type: "Chemical" }]);
    const picker = modal().querySelector('[data-testid="picker"]');
    expect(picker.dataset.path).toBe(`${PATH}.0.basic_information`);
  });

  it("picking a chemical prefills the component's name, not the entity's", async () => {
    setFakeVocabularyPicks({
      chemicals: { id: "chem:1", title_l10n: "Water" },
    });
    render({
      initialValues: assembly([
        { type: "Chemical", name: "", copy_number: -1 },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    await clickOn(modal().querySelector('[data-testid="pick"]'));
    // the pick handler writes `${fieldPath}.name` at the component path
    expect(probe()[0].name).toBe("Water");
  });

  it("Cancel on a new component removes it and the key (never [])", async () => {
    render({ initialValues: assembly(undefined) });
    await addOption("Polymer");
    expect(probe()).toEqual([{ type: "Polymer" }]);
    await clickOn(modalButton("Cancel"));
    expect(modal()).toBeNull();
    expect(probe()).toBeNull();
    expect(container.textContent).toContain("No items yet");
  });

  it("renders the summary row; a copy number of -1 shows 'unknown'", () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "RNA polymerase alpha subunit",
          copy_number: 2,
        },
        { type: "Chemical", name: "Zn2+", copy_number: -1 },
      ]),
    });
    expect(container.textContent).toContain("RNA polymerase alpha subunit");
    expect(container.textContent).toContain("Polymer");
    expect(container.textContent).toContain("unknown");
  });

  it("renders each summary cell, including the copy number and the identity", () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "RNA polymerase alpha subunit",
          copy_number: 2,
          polymer_type: "polypeptide(L)",
          molecular_weight: { value: 34.8, unit: "kDa" },
        },
        { type: "Chemical", name: "Zn2+", copy_number: -1 },
      ]),
    });
    // the closed Add dropdown also renders "Polymer"/"Chemical", so assert
    // the cells of each body row, not the whole container (a container-wide
    // toContain cannot fail on a broken Type cell)
    const cellsOf = (needle) => {
      const row = [...container.querySelectorAll("tbody tr")].find((r) =>
        r.textContent.includes(needle)
      );
      return [...row.querySelectorAll("td")].map((td) => td.textContent.trim());
    };
    expect(cellsOf("RNA polymerase alpha subunit")).toEqual(
      expect.arrayContaining([
        "RNA polymerase alpha subunit",
        "Polymer",
        "2",
        // the identity: the entity summary reused for the component
        "polypeptide(L), 34.8 kDa",
      ])
    );
    expect(cellsOf("Zn2+")).toEqual(
      expect.arrayContaining(["Zn2+", "Chemical", "unknown"])
    );
  });

  it("a type change keeps name, copy number and additional specifications", async () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "Mg2+ cofactor",
          copy_number: 2,
          additional_specifications: ["HPLC grade"],
          polymer_type: "polypeptide(L)",
        },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    await clickOn(buttonIn(modal(), "Chemical"));
    const confirm = modals().find((m) =>
      m.textContent.includes("The type-specific data will be removed.")
    );
    expect(confirm).toBeDefined();
    await clickOn(modalButtonIn(confirm, "Change"));
    expect(probe()).toEqual([
      {
        type: "Chemical",
        name: "Mg2+ cofactor",
        copy_number: 2,
        additional_specifications: ["HPLC grade"],
      },
    ]);
  });

  it("▸ on a polymer row shows the polymer groups without Name/Type/Copy number", async () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "RNA polymerase alpha subunit",
          copy_number: 2,
          polymer_type: "polypeptide(L)",
          expression_source_type: "Recombinantly",
        },
      ]),
    });
    const toggle = container.querySelector(
      'button[aria-label^="Show details of"]'
    );
    expect(toggle).not.toBeNull();
    await clickOn(toggle);
    const details = container.querySelector("tr.mbdb-details");
    expect(details).not.toBeNull();
    expect(details.textContent).toContain("polypeptide(L)");
    // Name/Type/Copy number are already in the row (detailProps.exclude)
    expect(details.textContent).not.toContain("RNA polymerase alpha subunit");
  });

  it("shows the row error badge and the message at Basic information", async () => {
    render({
      initialValues: assembly([
        { type: "Polymer", name: "alpha", copy_number: 1 },
        { type: "Polymer", name: "beta", copy_number: 1 },
        { type: "Chemical", name: "Zn2+", copy_number: -1 },
      ]),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                components: [
                  {},
                  {},
                  { basic_information: "Missing data for required field." },
                ],
              },
            ],
          },
        },
      },
    });
    expect(container.textContent).toContain("1 error");
    const badge = [...container.querySelectorAll(".ui.red.label")].find((l) =>
      l.textContent.includes("error")
    );
    await clickOn(badge);
    expect(modal().textContent).toContain("Missing data for required field.");
  });

  it("renders a polymer component's Modifications and QualityControls inline (no third modal)", async () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "alpha",
          copy_number: 1,
          modifications: {
            chemical: [{ type: "Phosphorylation", position: "S10" }],
          },
          quality_controls: { purity: { assessed: "No" } },
        },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    expect(modals()).toHaveLength(1);
    const text = modal().textContent;
    expect(text).toContain("Modifications");
    expect(text).toContain("Quality controls");
  });

  it("reuses PolymerFields at the component path: typing a variant writes there", async () => {
    render({
      initialValues: assembly([
        { type: "Polymer", name: "alpha", copy_number: 1 },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    await typeInto(
      modal().querySelector(`input[name="${PATH}.0.variant"]`),
      "V2A"
    );
    expect(probe()[0].variant).toBe("V2A");
  });

  it("depth 2: Cancel on a component restores only that component", async () => {
    container = renderInForm(
      <>
        <ModalArrayField
          fieldPath="entities"
          label="Entities"
          itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
          columns={[{ label: "Name", value: (v) => v.name }]}
          renderForm={(p) => <Components fieldPath={`${p}.components`} />}
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
    expect(modals()).toHaveLength(1);
    expect(readProbe(container)[0].components[0].name).toBe("alpha");
  });

  it("uses the component's own name help, not the entity's", async () => {
    // the real fixture: the component's name help is its own, not
    // the entity's; both texts are in the real ui_model
    setStructuredUiModel(realUiModel());
    render({
      initialValues: assembly([
        { type: "Polymer", name: "alpha", copy_number: 1 },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    const text = modal().textContent;
    expect(text).toContain("given to the assembly component");
    expect(text).not.toContain("Short descriptive name (id) of the entity");
  });
});
