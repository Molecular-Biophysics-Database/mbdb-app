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
  ComplexSubstanceOfIndustrialOriginFields,
  INDUSTRIAL_ORIGIN_GROUPS,
  summaryIndustrialOrigin,
} from "./index";

// One fake per layer: the picker needs the network. The shared blocks under
// test (Protocol, Storage, ComplexSubstanceCommon) stay real; the shared
// factory feeds the structured `ui_model`.
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
        { type: "Complex substance of industrial origin", ...fields },
      ],
    },
  },
});

const FILLED = {
  name: "Whey sample",
  product: { id: "prod:2" },
  preparation_protocol: [{ name: "Filtration", description: "0.22 µm filter" }],
};

const fields = () => (
  <ComplexSubstanceOfIndustrialOriginFields fieldPath={ENTITY} />
);

const picker = () => container.querySelector('[data-testid="picker"]');
const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);

describe("ComplexSubstanceOfIndustrialOriginFields", () => {
  it("renders the filled fixture at the entity paths", () => {
    container = renderInForm(fields(), { initialValues: entity(FILLED) });
    expect(picker().dataset.path).toBe(`${ENTITY}.product`);
    expect(picker().dataset.value).toBe("prod:2");
    // the common block (Protocol) is at the entity path too
    expect(hasInputValue("Filtration")).toBe(true);
  });

  it("shows a field-level error and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(FILLED),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { preparation_protocol: "Missing data for required field." },
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

describe("summaryIndustrialOrigin", () => {
  it("shows the product title from the cache", () => {
    setFakeVocabulary({ "products/prod:2": { title: "Whey" } });
    container = renderInForm(<>{summaryIndustrialOrigin(FILLED)}</>, {});
    expect(container.textContent).toBe("Whey");
  });

  it("returns '' without a product", () => {
    expect(summaryIndustrialOrigin({})).toBe("");
    expect(summaryIndustrialOrigin({ product: {} })).toBe("");
  });
});

describe("INDUSTRIAL_ORIGIN_GROUPS", () => {
  it("lists only fields that exist on the industrial-origin model type", () => {
    for (const group of INDUSTRIAL_ORIGIN_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        expect(
          yamlProperty("Complex_substance_of_industrial_origin", name)
        ).toBe(true);
      }
    }
  });
});
