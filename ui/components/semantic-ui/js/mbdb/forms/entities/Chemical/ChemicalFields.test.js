import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  editUnrelatedField,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ChemicalFields, CHEMICAL_GROUPS, summaryChemical } from "./index";

// The two leaves are faked, so the test asserts the composition (the paths
// ChemicalFields builds) and the summary, not the leaves' own behaviour
// (each has its own suite). The picker needs the network; oarepo's
// StringArrayField needs props/context the mbdb wrapper does not pass here.
// eslint-disable-next-line no-restricted-syntax -- kept local: oarepo fake + a StringArrayField stand-in (see comment)
jest.mock("@js/oarepo_ui/forms", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const base = jest.requireActual(
    "@js/mbdb/forms/building-blocks/testUtils"
  ).oarepoFake;
  // Stand-in for oarepo's StringArrayField: renders the current list so the
  // test can read the values the wrapper is bound to.
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
  return { ...base, StringArrayField };
});

// The picker is faked (it queries the vocabulary API): it stands for what the
// block needs from it — the fieldPath it was handed and the value it shows.
jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const FakeMbdbVocabularyField = ({ fieldPath }) => {
    const { values } = useFormikContext();
    const v = getIn(values, fieldPath);
    return R.createElement(
      "div",
      { "data-testid": "picker", "data-path": fieldPath },
      R.createElement(
        "span",
        { "data-testid": "picker-value" },
        v?.id ?? v?.title?.en ?? ""
      )
    );
  };
  FakeMbdbVocabularyField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
  };
  return { MbdbVocabularyField: FakeMbdbVocabularyField };
});

// The shared title cache is mocked to answer synchronously (no network).
let mockItems = {};
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () => ({
  useVocabularyItem: (type, id) =>
    mockItems[`${type}/${id}`] ?? {
      title: undefined,
      customFields: undefined,
    },
  useVocabularyTitle: (type, id) => (mockItems[`${type}/${id}`] ?? {}).title,
  rememberItem: () => {},
}));

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const BASIC = `${ENTITY}.basic_information`;
const SPECS = `${ENTITY}.additional_specifications`;
const WATER_ID = "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N";

let container;

beforeEach(() => {
  mockItems = {};
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

const chemical = () => <ChemicalFields fieldPath={ENTITY} />;

const picker = () => container.querySelector('[data-testid="picker"]');
const pickerValue = () =>
  container.querySelector('[data-testid="picker-value"]')?.textContent;
const specs = () => container.querySelector('[data-testid="specs"]');

const renderSummary = (value) => {
  container = renderInForm(<>{summaryChemical(value)}</>, {});
  return container;
};

describe("ChemicalFields", () => {
  it("binds the picker and the specifications to the entity paths", () => {
    container = renderInForm(chemical(), { initialValues: entity(FILLED) });
    expect(picker().dataset.path).toBe(BASIC);
    expect(pickerValue()).toBe(WATER_ID);
    expect(specs().dataset.path).toBe(SPECS);
    expect(specs().textContent).toBe("HPLC grade");
  });

  it("renders an entity without a pickable value without crashing", () => {
    container = renderInForm(chemical(), { initialValues: entity() });
    expect(picker().dataset.path).toBe(BASIC);
    expect(pickerValue()).toBe("");
    expect(specs().textContent).toBe("");
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
    mockItems = {
      [`chemicals/${WATER_ID}`]: {
        title: "Water",
        customFields: { chemical_formula: "H2O" },
      },
    };
    renderSummary({ basic_information: { id: WATER_ID } });
    expect(container.textContent).toBe("Water, H2O");
  });

  it("shows the title only when the cache knows no formula", () => {
    mockItems = {
      [`chemicals/${WATER_ID}`]: { title: "Water", customFields: {} },
    };
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
