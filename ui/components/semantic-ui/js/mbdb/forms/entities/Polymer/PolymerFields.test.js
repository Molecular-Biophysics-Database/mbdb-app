import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  typeInto,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  setStructuredUiModel,
  yamlEnum,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { PolymerFields, POLYMER_GROUPS, summaryPolymer } from "./index";
import { POLYMER_TYPES, EXPRESSION_SOURCE_TYPES } from "./constants";

// One fake per layer: the picker needs the network. The shared blocks under
// test (Sequence, MolecularWeight, ExternalDatabases, Modifications,
// QualityControls, SelectField, …) stay real; the shared factory feeds the
// structured `ui_model`.
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

let mockUiModel;

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const COMPONENT = `${ENTITY}.components.0`;

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

const entity = (fields) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [{ type: "Polymer", ...fields }],
    },
  },
});

const FILLED = {
  name: "Hemoglobin subunit beta",
  polymer_type: "polypeptide(L)",
  expression_source_type: "Recombinantly",
  variant: "V2A",
  sequence:
    "MAHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH",
  molecular_weight: { value: 16.0, unit: "kDa" },
  external_databases: ["Uniprot:P68871"],
  source_organism: { id: "taxid:12374" },
  modifications: {
    biological_postprocessing: [{ position: "S10", type: "Phosphorylation" }],
  },
};

const fields = (path = ENTITY) => <PolymerFields fieldPath={path} />;

const picker = (path) =>
  container.querySelector(`[data-testid="picker"][data-path="${path}"]`);

const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);

describe("Polymer constants", () => {
  it("POLYMER_TYPES equals the model enum", () => {
    expect(POLYMER_TYPES).toEqual(yamlEnum("Polymer", "polymer_type"));
  });
  it("EXPRESSION_SOURCE_TYPES equals the model enum", () => {
    expect(EXPRESSION_SOURCE_TYPES).toEqual(
      yamlEnum("Polymer", "expression_source_type")
    );
  });
});

describe("PolymerFields", () => {
  it("renders the filled fixture at the entity paths", () => {
    container = renderInForm(fields(), { initialValues: entity(FILLED) });
    // Identification
    expect(container.textContent).toContain("polypeptide(L)");
    expect(container.textContent).toContain("Recombinantly");
    expect(document.getElementById(`${ENTITY}.variant`).value).toBe("V2A");
    // Sequence: the textarea value and the residue counter
    expect(document.getElementById(`${ENTITY}.sequence`).value).toBe(
      FILLED.sequence
    );
    expect(container.textContent).toContain("residues");
    // Origin: the picker, at the entity path, showing the stored id
    expect(picker(`${ENTITY}.source_organism`).dataset.value).toBe(
      "taxid:12374"
    );
    // Molecular weight
    expect(document.getElementById(`${ENTITY}.molecular_weight`).value).toBe(
      "16"
    );
    expect(container.textContent).toContain("kDa");
    // External databases (parsed into a database select + an id input)
    expect(container.textContent).toContain("uniprot");
    expect(hasInputValue("P68871")).toBe(true);
    // Modifications (free-text cells, so the values live in the inputs)
    expect(hasInputValue("Phosphorylation")).toBe(true);
    expect(hasInputValue("S10")).toBe(true);
  });

  it("shows a field-level error and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(FILLED),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ variant: "Only ASCII letters allowed." }],
          },
        },
      },
      withUnrelatedField: true,
    });
    const messages = () =>
      [...container.querySelectorAll(".ui.pointing.prompt.label")].map(
        (l) => l.textContent
      );
    expect(messages()).toContain("Only ASCII letters allowed.");
    await editUnrelatedField(container);
    expect(messages()).toContain("Only ASCII letters allowed.");
  });

  it("works at a component path (reused for ComponentPolymer)", async () => {
    container = renderInForm(
      <>
        <PolymerFields fieldPath={COMPONENT} />
        <ValueProbe path={COMPONENT} />
      </>,
      {
        initialValues: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                {
                  type: "Molecular assembly",
                  components: [{ type: "Polymer" }],
                },
              ],
            },
          },
        },
      }
    );
    // every path is built from the given fieldPath, not entities_of_interest
    expect(picker(`${COMPONENT}.source_organism`)).not.toBeNull();
    await typeInto(document.getElementById(`${COMPONENT}.variant`), "V2A");
    expect(readProbe(container)).toEqual({ type: "Polymer", variant: "V2A" });
  });

  it("uses the polymer's own molecular_weight help, not the union's (D7)", () => {
    mockUiModel = {
      children: {
        metadata: {
          children: {
            general_parameters: {
              children: {
                entities_of_interest: {
                  children: {
                    child: {
                      children: {
                        molecular_weight: {
                          label: { en: "Molecular weight" },
                          help: { en: "Union help, not the polymer's" },
                        },
                      },
                      discriminator: "type",
                      variants: {
                        Polymer: {
                          children: {
                            molecular_weight: {
                              label: { en: "Molecular weight" },
                              help: {
                                en: "The molecular weight of the polymer",
                              },
                            },
                          },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
        },
      },
    };
    setStructuredUiModel(mockUiModel);
    container = renderInForm(fields(), {
      initialValues: entity({ molecular_weight: { value: 16, unit: "kDa" } }),
    });
    expect(container.textContent).toContain(
      "The molecular weight of the polymer"
    );
    expect(container.textContent).not.toContain(
      "Union help, not the polymer's"
    );
  });
});

describe("summaryPolymer", () => {
  it("joins polymer type, molecular weight and source organism", () => {
    setFakeVocabulary({
      "organisms/taxid:12374": { title: "Bacillus subtilis" },
    });
    container = renderInForm(<>{summaryPolymer(FILLED)}</>, {});
    expect(container.textContent).toBe(
      "polypeptide(L), 16 kDa, Bacillus subtilis"
    );
  });

  it("leaves out missing parts and returns '' for an empty entity", () => {
    container = renderInForm(
      <>{summaryPolymer({ polymer_type: "polypeptide(L)" })}</>,
      {}
    );
    expect(container.textContent).toBe("polypeptide(L)");
    expect(summaryPolymer({})).toBe("");
  });
});

describe("POLYMER_GROUPS", () => {
  it("lists only fields that exist on the Polymer model type", () => {
    for (const group of POLYMER_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        expect(yamlProperty("Polymer", name)).toBe(true);
      }
    }
  });
});
