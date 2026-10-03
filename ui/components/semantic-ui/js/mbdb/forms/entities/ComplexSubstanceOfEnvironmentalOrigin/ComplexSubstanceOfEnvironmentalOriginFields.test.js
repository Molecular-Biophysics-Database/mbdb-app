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
  ComplexSubstanceOfEnvironmentalOriginFields,
  ENVIRONMENTAL_ORIGIN_GROUPS,
  summaryEnvironmentalOrigin,
} from "./index";

// One fake per layer: the picker needs the network. The shared blocks under
// test (Location, Protocol, Storage, ComplexSubstanceCommon) stay real; the
// shared factory feeds the structured `ui_model`.
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
        { type: "Complex substance of environmental origin", ...fields },
      ],
    },
  },
});

const FILLED = {
  name: "Brno pond water",
  environment_type: { id: "env:1" },
  location: { latitude: 49.1951, longitude: 16.6068, altitude: 237 },
  preparation_protocol: [{ name: "Filtration", description: "0.22 µm filter" }],
};

const fields = () => (
  <ComplexSubstanceOfEnvironmentalOriginFields fieldPath={ENTITY} />
);

const picker = () => container.querySelector('[data-testid="picker"]');
const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);

describe("ComplexSubstanceOfEnvironmentalOriginFields", () => {
  it("renders the filled fixture at the entity paths", () => {
    container = renderInForm(fields(), { initialValues: entity(FILLED) });
    expect(picker().dataset.path).toBe(`${ENTITY}.environment_type`);
    expect(picker().dataset.value).toBe("env:1");
    // Location: the number fields hold the stored values
    expect(hasInputValue("49.1951")).toBe(true);
    expect(hasInputValue("237")).toBe(true);
    // the common block (Protocol) is at the entity path too
    expect(hasInputValue("Filtration")).toBe(true);
  });

  it("shows the object-level error at location under the Location header", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(FILLED),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { location: "Missing data for required field." },
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

describe("summaryEnvironmentalOrigin", () => {
  it("joins the environment type title and the coordinates", () => {
    setFakeVocabulary({ "environment-types/env:1": { title: "Fresh water" } });
    container = renderInForm(<>{summaryEnvironmentalOrigin(FILLED)}</>, {});
    expect(container.textContent).toBe("Fresh water, 49.1951, 16.6068");
  });

  it("leaves out the coordinates when either is missing", () => {
    setFakeVocabulary({ "environment-types/env:1": { title: "Fresh water" } });
    container = renderInForm(
      <>
        {summaryEnvironmentalOrigin({
          environment_type: { id: "env:1" },
          location: { altitude: 10 },
        })}
      </>,
      {}
    );
    expect(container.textContent).toBe("Fresh water");
  });

  it("returns '' for an empty entity", () => {
    expect(summaryEnvironmentalOrigin({})).toBe("");
    expect(summaryEnvironmentalOrigin({ location: { latitude: 1 } })).toBe("");
  });
});

describe("ENVIRONMENTAL_ORIGIN_GROUPS", () => {
  it("lists only fields that exist on the environmental-origin model type", () => {
    for (const group of ENVIRONMENTAL_ORIGIN_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        expect(
          yamlProperty("Complex_substance_of_environmental_origin", name)
        ).toBe(true);
      }
    }
  });
});
