import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  setFakeVocabularyPicks,
  editUnrelatedField,
  clickOn,
  ValueProbe,
  readProbe,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ChemicalFields, CHEMICAL_GROUPS, summaryChemical } from "./index";

// The two leaves are faked, so the test asserts the composition (the paths
// ChemicalFields builds) and the summary, not the leaves' own behaviour
// (each has its own suite). The picker needs the network.
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory
jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
);

// Client-only row keys (jsdom has no WebCrypto): StringTableField builds on
// TableArrayField, which mints a key per row.
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

// The picker is faked (it queries the vocabulary API): it stands for what the
// block needs from it — the fieldPath it was handed, the value it shows, and
// a pick that calls the caller's onPicked with a suggestion.
jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyField()
);

// The shared title cache is mocked to answer synchronously (no network).
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyTitles()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const BASIC = `${ENTITY}.basic_information`;
const WATER_ID = "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N";

let container;

beforeEach(() => {
  setFakeVocabulary();
  // the picker's pick writes { id } (and calls onPicked -> the Name prefill)
  setFakeVocabularyPicks({
    chemicals: { id: WATER_ID, title_l10n: "Water" },
  });
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
      entities_of_interest: [{ type: "Chemical", ...fields }],
    },
  },
});

const FILLED = {
  name: "Water",
  basic_information: { id: WATER_ID },
  additional_specifications: ["HPLC grade"],
};

const chemical = () => (
  <>
    <ChemicalFields fieldPath={ENTITY} />
    <ValueProbe path={`${ENTITY}.name`} />
  </>
);

const picker = () => container.querySelector('[data-testid="picker"]');
const pickerValue = () =>
  container.querySelector('[data-testid="picker-value"]')?.textContent;
// the specifications are a one-column table; its cell input carries the column
// header as its aria-label
const specs = () =>
  container.querySelector('input[aria-label="Specification"]');

const renderSummary = (value) => {
  container = renderInForm(<>{summaryChemical(value)}</>, {});
  return container;
};

describe("ChemicalFields", () => {
  it("binds the picker and the specifications to the entity paths", () => {
    container = renderInForm(chemical(), { initialValues: entity(FILLED) });
    expect(picker().dataset.path).toBe(BASIC);
    expect(pickerValue()).toBe(WATER_ID);
    expect(specs().value).toBe("HPLC grade");
  });

  it("picking a chemical prefills an empty Name with its title", async () => {
    container = renderInForm(chemical(), { initialValues: entity() });
    expect(readProbe(container)).toBeNull();
    await clickOn(container.querySelector('[data-testid="pick"]'));
    expect(readProbe(container)).toBe("Water");
  });

  it("does not overwrite a Name the user already set", async () => {
    container = renderInForm(chemical(), {
      initialValues: entity({ name: "My water" }),
    });
    await clickOn(container.querySelector('[data-testid="pick"]'));
    expect(readProbe(container)).toBe("My water");
  });

  it("renders an entity without a pickable value without crashing", () => {
    container = renderInForm(chemical(), { initialValues: entity() });
    expect(picker().dataset.path).toBe(BASIC);
    expect(pickerValue()).toBe("");
    // no stored specification → no row (the array is optional, no virtual row)
    expect(specs()).toBeNull();
  });

  it("a saved manual chemical (manual: id) renders the picker, not the manual form", () => {
    container = renderInForm(chemical(), {
      initialValues: entity({ basic_information: { id: "manual:abc" } }),
    });
    expect(picker()).not.toBeNull();
    // the manual-entry form's Name input is not mounted
    expect(
      container.querySelector(`input[name="${BASIC}.title.en"]`)
    ).toBeNull();
  });

  it("shows a specifications error and keeps it after an unrelated edit", async () => {
    container = renderInForm(chemical(), {
      initialValues: entity(FILLED),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { additional_specifications: "Shorter than minimum length 1." },
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
    expect(messages()).toContain("Shorter than minimum length 1.");
    await editUnrelatedField(container);
    expect(messages()).toContain("Shorter than minimum length 1.");
  });
});

describe("summaryChemical", () => {
  it("shows the title and the formula from the cache", () => {
    setFakeVocabulary({
      [`chemicals/${WATER_ID}`]: {
        title: "Water",
        customFields: { chemical_formula: "H2O" },
      },
    });
    renderSummary({ basic_information: { id: WATER_ID } });
    expect(container.textContent).toBe("Water, H2O");
  });

  it("shows the title only when the cache knows no formula", () => {
    setFakeVocabulary({
      [`chemicals/${WATER_ID}`]: { title: "Water", customFields: {} },
    });
    renderSummary({ basic_information: { id: WATER_ID } });
    expect(container.textContent).toBe("Water");
  });

  it("returns '' when there is no basic information", () => {
    expect(summaryChemical({})).toBe("");
    expect(summaryChemical({ basic_information: {} })).toBe("");
  });

  it("shows a manual chemical's typed title", () => {
    expect(
      summaryChemical({ basic_information: { title: { en: "my lipid mix" } } })
    ).toBe("my lipid mix");
  });
});

describe("CHEMICAL_GROUPS", () => {
  it("lists only fields that exist on the Chemical model type", () => {
    for (const group of CHEMICAL_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        expect(yamlProperty("Chemical", name)).toBe(true);
      }
    }
  });
});
