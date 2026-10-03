import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  clickOn,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  setStructuredUiModel,
  realUiModel,
  yamlEnum,
  yamlProperty,
} from "@js/mbdb/forms/building-blocks/testUtils";
import {
  ComplexSubstanceOfBiologicalOriginFields,
  biologicalOriginGroups,
  summaryBiologicalOrigin,
  summaryVirion,
  summarySolidTissueSample,
  DERIVED_FROM,
  VIRION_GENETIC_MATERIAL,
  VIRION_PARTICLE_TYPES,
} from "./index";

// One fake per layer: the pickers need the network. The shared blocks under
// test (the sub-type fields, Protocol, Storage, the common block) stay real;
// the shared factory feeds the structured `ui_model`.
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
        { type: "Complex substance of biological origin", ...fields },
      ],
    },
  },
});

const BODY_FLUID = {
  id: "e-1",
  name: "Human serum",
  derived_from: "Body fluid",
  source_organism: { id: "taxid:12374" },
  fluid: { id: "bf:2" },
  health_status: "Healthy",
  preparation_protocol: [
    { name: "Centrifugation", description: "10 min at 1,300g" },
  ],
};

const fields = () => (
  <ComplexSubstanceOfBiologicalOriginFields fieldPath={ENTITY} />
);

const pickerFor = (path) =>
  container.querySelector(`[data-testid="picker"][data-path="${path}"]`);
const hasInputValue = (value) =>
  [...container.querySelectorAll("input")].some((el) => el.value === value);
const buttonIn = (root, label) =>
  [...root.querySelectorAll("button")].find((b) => b.textContent === label);
const modalButtonIn = (m, label) =>
  [...m.querySelectorAll("button")].find((b) => b.textContent === label);
const modalWith = (text) =>
  [...document.body.querySelectorAll(".ui.modal")].find((m) =>
    m.textContent.includes(text)
  );

describe("biological-origin constants", () => {
  it("DERIVED_FROM equals the model enum", () => {
    expect(DERIVED_FROM).toEqual(
      yamlEnum("Complex_substance_of_biological_origin_base", "derived_from")
    );
  });
  it("VIRION_GENETIC_MATERIAL equals the model enum", () => {
    expect(VIRION_GENETIC_MATERIAL).toEqual(
      yamlEnum("Virion", "genetic_material")
    );
  });
  it("VIRION_PARTICLE_TYPES equals the model enum", () => {
    expect(VIRION_PARTICLE_TYPES).toEqual(yamlEnum("Virion", "capsid_type"));
  });
});

describe("ComplexSubstanceOfBiologicalOriginFields", () => {
  it("shows only the discriminator and the hint before a sub-type is picked", () => {
    container = renderInForm(fields(), { initialValues: entity() });
    expect(container.textContent).toContain(
      "Select what the substance is derived from"
    );
    // no source organism, no sub-type fields, no common block
    expect(container.querySelector('[data-testid="picker"]')).toBeNull();
    expect(container.querySelectorAll("tbody tr")).toHaveLength(0);
  });

  it("picking Cell fraction on a bare item writes it with no confirmation", async () => {
    container = renderInForm(
      <>
        {fields()}
        <ValueProbe path={ENTITY} />
      </>,
      { initialValues: entity({ id: "e-1" }) }
    );
    await clickOn(buttonIn(container, "Cell fraction"));
    expect(readProbe(container)).toEqual({
      id: "e-1",
      type: "Complex substance of biological origin",
      derived_from: "Cell fraction",
    });
  });

  it("changing derived_from with data asks for confirmation, then keeps id, type and name", async () => {
    container = renderInForm(
      <>
        {fields()}
        <ValueProbe path={ENTITY} />
      </>,
      { initialValues: entity(BODY_FLUID) }
    );
    await clickOn(buttonIn(container, "Virion"));
    const confirm = modalWith("The type-specific data will be removed.");
    expect(confirm).toBeDefined();
    // not applied until confirmed
    expect(readProbe(container).derived_from).toBe("Body fluid");
    await clickOn(modalButtonIn(confirm, "Change"));
    expect(readProbe(container)).toEqual({
      id: "e-1",
      type: "Complex substance of biological origin",
      name: "Human serum",
      derived_from: "Virion",
    });
  });

  it("renders the Body fluid scenario at the entity paths", () => {
    container = renderInForm(fields(), { initialValues: entity(BODY_FLUID) });
    expect(pickerFor(`${ENTITY}.source_organism`).dataset.value).toBe(
      "taxid:12374"
    );
    expect(pickerFor(`${ENTITY}.fluid`).dataset.value).toBe("bf:2");
    expect(hasInputValue("Healthy")).toBe(true);
    expect(hasInputValue("Centrifugation")).toBe(true);
  });

  it("marks organ required for Solid tissue sample (D7 nested variant)", () => {
    container = renderInForm(fields(), {
      initialValues: entity({
        derived_from: "Solid tissue sample",
        organ: "liver",
      }),
    });
    expect(
      document.getElementById(`${ENTITY}.organ`).closest(".field").className
    ).toContain("required");
  });

  it("leaves organ optional for Cell fraction (D7 nested variant)", () => {
    container = renderInForm(fields(), {
      initialValues: entity({ derived_from: "Cell fraction", organ: "liver" }),
    });
    expect(
      document.getElementById(`${ENTITY}.organ`).closest(".field").className
    ).not.toContain("required");
  });

  it("shows a field-level error and keeps it after an unrelated edit", async () => {
    container = renderInForm(fields(), {
      initialValues: entity(BODY_FLUID),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { health_status: "Missing data for required field." },
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

describe("summaries", () => {
  it("summaryBiologicalOrigin joins derived_from, source organism and the key value", () => {
    setFakeVocabulary({
      "organisms/taxid:12374": { title: "Homo sapiens" },
      "body-fluids/bf:2": { title: "Serum" },
    });
    container = renderInForm(<>{summaryBiologicalOrigin(BODY_FLUID)}</>, {});
    expect(container.textContent).toBe("Body fluid, Homo sapiens, Serum");
    expect(summaryBiologicalOrigin({})).toBe("");
  });

  it("summaryVirion is '<capsid> capsid, <envelope> envelope'", () => {
    container = renderInForm(
      <>{summaryVirion({ capsid_type: "Native", envelope_type: "None" })}</>,
      {}
    );
    expect(container.textContent).toBe("Native capsid, None envelope");
  });

  it("summarySolidTissueSample covers true, false and unset", () => {
    container = renderInForm(
      <>{summarySolidTissueSample({ organ: "liver", homogenized: true })}</>,
      {}
    );
    expect(container.textContent).toBe("liver, homogenized");
    container = renderInForm(
      <>{summarySolidTissueSample({ organ: "liver", homogenized: false })}</>,
      {}
    );
    expect(container.textContent).toBe("liver, not homogenized");
    container = renderInForm(
      <>{summarySolidTissueSample({ organ: "liver" })}</>,
      {}
    );
    expect(container.textContent).toBe("liver");
  });
});

describe("biologicalOriginGroups", () => {
  it("lists the fields of each sub-type on its model type", () => {
    const FIELD_TYPE = {
      derived_from: "Complex_substance_of_biological_origin_base",
      source_organism: "Complex_substance_of_biological_origin_base",
      preparation_protocol: "Complex_substance_of_biological_origin_base",
      storage: "Complex_substance_of_biological_origin_base",
      additional_specifications: "Complex_substance_of_biological_origin_base",
      fluid: "Body_fluid",
      health_status: "Body_fluid",
      fraction: "Cell_fraction",
      tissue: "Cell_fraction",
      cell_type: "Cell_fraction",
      organ: "Solid_tissue_sample",
      homogenized: "Solid_tissue_sample",
      genetic_material: "Virion",
      capsid_type: "Virion",
      envelope_type: "Virion",
      host_organism: "Virion",
      host_cell_type: "Virion",
    };
    for (const derivedFrom of DERIVED_FROM) {
      for (const group of biologicalOriginGroups({
        derived_from: derivedFrom,
      })) {
        for (const entry of group.fields) {
          const name = typeof entry === "string" ? entry : entry.field;
          expect(yamlProperty(FIELD_TYPE[name], name)).toBe(true);
        }
      }
    }
  });
});
