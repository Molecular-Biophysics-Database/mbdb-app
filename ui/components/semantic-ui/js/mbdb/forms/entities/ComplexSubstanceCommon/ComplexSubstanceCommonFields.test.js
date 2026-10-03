import React from "react";
import {
  renderInForm,
  unmountForm,
  setStructuredUiModel,
  realUiModel,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import {
  ComplexSubstanceCommonFields,
  COMPLEX_SUBSTANCE_COMMON_GROUPS,
} from "./index";

// The real model shape: the shared oarepo mock
// reads the ui_model set with setStructuredUiModel (the real-model fixture).
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory
jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
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
  setStructuredUiModel(realUiModel());
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
  preparation_protocol: [
    { name: "Centrifugation", description: "10 min at 4000 g" },
    { name: "Filtration", description: "0.22 µm filter" },
  ],
  storage: {
    temperature: { value: -80, unit: "°C" },
    duration: { value: 3, unit: "months" },
  },
  additional_specifications: ["Freshly prepared"],
};

const fields = (path = ENTITY) => (
  <ComplexSubstanceCommonFields fieldPath={path} />
);

const labelFor = (path) =>
  [...container.querySelectorAll("label")].find((l) => l.htmlFor === path);
const isBefore = (a, b) =>
  Boolean(a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING);
const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);

describe("ComplexSubstanceCommonFields", () => {
  it("renders the three blocks in this order, at the given fieldPath", () => {
    container = renderInForm(fields(), { initialValues: entity(FILLED) });
    // each block binds to the path it was given
    const protocol = labelFor(`${ENTITY}.preparation_protocol`);
    const storage = labelFor(`${ENTITY}.storage`);
    const specs = container.querySelector('[data-testid="specs"]');
    expect(protocol.textContent).toContain("Preparation protocol");
    expect(storage.textContent).toContain("Storage");
    expect(specs.dataset.path).toBe(`${ENTITY}.additional_specifications`);
    // the order is protocol, then storage, then the specifications
    expect(isBefore(protocol, storage)).toBe(true);
    expect(isBefore(storage, specs)).toBe(true);
    // values render: protocol cells, the storage summary, the specifications
    expect(hasInputValue("Centrifugation")).toBe(true);
    expect(container.textContent).toContain("for 3 months");
    expect(container.textContent).toContain("Freshly prepared");
  });

  it("with an empty item renders one protocol row, no storage and writes nothing", () => {
    container = renderInForm(
      <>
        {fields()}
        <ValueProbe path={ENTITY} />
      </>,
      { initialValues: entity() }
    );
    // one virtual row (minItems 1) with no remove button
    expect(container.querySelectorAll("tbody tr")).toHaveLength(1);
    expect(
      container.querySelector('button[aria-label^="Remove row"]')
    ).toBeNull();
    // storage is absent until added
    expect(container.textContent).toContain("Add Storage");
    // nothing under the fragment was written
    expect(readProbe(container)).toEqual({
      type: "Complex substance of industrial origin",
    });
  });

  it("shows a list-level error on preparation_protocol and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(),
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

describe("COMPLEX_SUBSTANCE_COMMON_GROUPS", () => {
  it("lists only fields that exist on every complex-substance model type", () => {
    const TYPES = [
      "Complex_substance_of_industrial_origin",
      "Complex_substance_of_environmental_origin",
      "Complex_substance_of_chemical_origin_base",
      "Complex_substance_of_biological_origin_base",
    ];
    for (const group of COMPLEX_SUBSTANCE_COMMON_GROUPS) {
      for (const entry of group.fields) {
        const name = typeof entry === "string" ? entry : entry.field;
        for (const type of TYPES) expect(yamlProperty(type, name)).toBe(true);
      }
    }
  });
});
