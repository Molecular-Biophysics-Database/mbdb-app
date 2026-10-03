import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  typeInto,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  yamlEnum,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { PolymerFields, POLYMER_GROUPS, summaryPolymer } from "./index";
import { POLYMER_TYPES, EXPRESSION_SOURCE_TYPES } from "./constants";

// One fake per layer. The picker needs the network (MbdbVocabularyField) and
// oarepo's StringArrayField needs a context the mbdb wrapper does not pass
// here; the shared blocks under test (Sequence, MolecularWeight,
// ExternalDatabases, Modifications, QualityControls, SelectField, …) stay
// real. The title cache answers synchronously.
// eslint-disable-next-line no-restricted-syntax -- kept local: oarepo fake + a StringArrayField stand-in + a ui_model for the D7 variant (see comment)
jest.mock("@js/oarepo_ui/forms", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const base = jest.requireActual(
    "@js/mbdb/forms/building-blocks/testUtils"
  ).oarepoFake;
  const StringArrayField = ({ fieldPath }) => {
    const { values } = useFormikContext();
    const items = getIn(values, fieldPath) ?? [];
    return R.createElement(
      "div",
      { "data-testid": "specs", "data-path": fieldPath },
      items.join(", ")
    );
  };
  StringArrayField.propTypes = { fieldPath: PropTypesActual.string.isRequired };
  // mockUiModel drives the variant-aware lookup; undefined falls back to the
  // shared flat fake (setFakeUiModel).
  return {
    ...base,
    StringArrayField,
    useFormConfig: () => ({ config: { ui_model: mockUiModel } }),
  };
});

jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const FakeMbdbVocabularyField = ({ fieldPath }) => {
    const { values } = useFormikContext();
    const v = getIn(values, fieldPath);
    return R.createElement("div", {
      "data-testid": "picker",
      "data-path": fieldPath,
      "data-value": v?.id ?? v?.title?.en ?? "",
    });
  };
  FakeMbdbVocabularyField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
  };
  return { MbdbVocabularyField: FakeMbdbVocabularyField };
});

let mockTitles = {};
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () => ({
  useVocabularyItem: (type, id) => mockTitles[`${type}/${id}`] ?? {},
  useVocabularyTitle: (type, id) => mockTitles[`${type}/${id}`]?.title,
  rememberItem: () => {},
}));

// Client-only row keys (jsdom has no WebCrypto), as in Storage.test.js.
let mockKeyN = 0;
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => `key-${++mockKeyN}-uuid`,
}));

let mockUiModel;

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const COMPONENT = `${ENTITY}.components.0`;

let container;

beforeEach(() => {
  mockTitles = {};
  mockUiModel = undefined;
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
    mockTitles = { "organisms/taxid:12374": { title: "Bacillus subtilis" } };
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
