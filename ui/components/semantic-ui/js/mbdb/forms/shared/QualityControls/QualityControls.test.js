import React from "react";
import {
  renderInForm,
  unmountForm,
  setStructuredUiModel,
  realUiModel,
  ValueProbe,
  readProbe,
  clickOn,
  pickDropdown,
  editUnrelatedField,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { QualityControls } from "./index";
import {
  ASSESSED,
  PURITY_METHODS,
  PURITY_PERCENTAGES,
  HOMOGENEITY_METHODS,
} from "./constants";

// The real model shape: the shared oarepo mock
// reads the ui_model set with setStructuredUiModel (the real-model fixture). A
// hand-built fake whose variant entries had no label/help hid the row-label
// bug.
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory, not a hand-rolled fake
jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const QC = `${ENTITY}.quality_controls`;

let container;

beforeEach(() => {
  setStructuredUiModel(realUiModel());
});

afterEach(() => {
  setStructuredUiModel();
  unmountForm(container);
  container = null;
});

const polymer = (qualityControls) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Polymer",
          name: "Hemoglobin subunit beta",
          ...(qualityControls === undefined
            ? {}
            : { quality_controls: qualityControls }),
        },
      ],
    },
  },
});

const controls = () => (
  <>
    <QualityControls fieldPath={QC} />
    <ValueProbe path={QC} />
  </>
);

const probe = () => readProbe(container);
const buttons = () => [...container.querySelectorAll(".ui.buttons button")];

describe("QualityControls constants", () => {
  it("ASSESSED equals every base enum", () => {
    for (const type of ["Purity_base", "Identity_base", "Homogeneity_base"])
      expect(ASSESSED).toEqual(yamlEnum(type, "assessed"));
  });
  it("PURITY_METHODS equals the model enum", () => {
    expect(PURITY_METHODS).toEqual(yamlEnum("Yes_purity", "method"));
  });
  it("PURITY_PERCENTAGES equals the model enum (the space is part of the value)", () => {
    expect(PURITY_PERCENTAGES).toEqual(
      yamlEnum("Yes_purity", "purity_percentage")
    );
  });
  it("HOMOGENEITY_METHODS equals the model enum (incl. Dynamic light scattering)", () => {
    expect(HOMOGENEITY_METHODS).toEqual(yamlEnum("Yes_homogeneity", "method"));
    expect(HOMOGENEITY_METHODS).toContain("Dynamic light scattering");
  });
});

describe("QualityControls", () => {
  it("labels the rows from the model, without a required marker", () => {
    container = renderInForm(controls(), { initialValues: polymer(undefined) });
    for (const check of ["Purity", "Identity", "Homogeneity"]) {
      const label = [...container.querySelectorAll("label")].find(
        (l) => l.textContent === check
      );
      expect(label).toBeDefined();
      // no required asterisk on a check whose value may stay absent
      expect(label.closest(".field.required")).toBeNull();
    }
  });

  it("keeps the Purity row label and help in every state", () => {
    // with the real model the variant entries carry the type's own texts
    // ("Yes purity" / "Empty object"); they must not reach the row
    for (const assessed of [undefined, "Yes", "No"]) {
      const c = renderInForm(controls(), {
        initialValues: polymer(assessed ? { purity: { assessed } } : undefined),
      });
      const label = [...c.querySelectorAll("label")].find(
        (l) => l.textContent === "Purity"
      );
      expect(label).toBeDefined();
      expect(c.textContent).toContain(
        "Information about if and how purity was assessed"
      );
      unmountForm(c);
    }
  });

  it('Empty → Yes on Purity writes { purity: { assessed: "Yes" } } and shows the Purity fields', async () => {
    container = renderInForm(controls(), { initialValues: polymer(undefined) });
    await clickOn(buttons().find((b) => b.textContent === "Yes"));
    expect(probe()).toEqual({ purity: { assessed: "Yes" } });
    expect(container.textContent).toContain("Method");
    expect(container.textContent).toContain("Purity percentage");
  });

  it("selecting a Purity method writes it as a string", async () => {
    container = renderInForm(controls(), { initialValues: polymer(undefined) });
    await clickOn(buttons().find((b) => b.textContent === "Yes"));
    await pickDropdown(`${QC}.purity.method`, "SDS-PAGE");
    expect(probe()).toEqual({
      purity: { assessed: "Yes", method: "SDS-PAGE" },
    });
  });

  it("Filled → Not specified on Purity (confirmed) removes purity only", async () => {
    container = renderInForm(controls(), {
      initialValues: polymer({
        purity: {
          assessed: "Yes",
          method: "SDS-PAGE",
          purity_percentage: ">99 %",
        },
        identity: { assessed: "No" },
        homogeneity: { assessed: "No" },
      }),
    });
    // the first row's "Not specified" button
    await clickOn(buttons().find((b) => b.textContent === "Not specified"));
    // confirm the data loss
    const remove = [...document.querySelectorAll(".ui.modal button")].find(
      (b) => b.textContent === "Remove"
    );
    expect(remove).toBeDefined();
    await clickOn(remove);
    expect(probe()).toEqual({
      identity: { assessed: "No" },
      homogeneity: { assessed: "No" },
    });
  });

  it('{ purity: { assessed: "No" } } only → Not specified leaves quality_controls absent', async () => {
    container = renderInForm(controls(), {
      initialValues: polymer({ purity: { assessed: "No" } }),
    });
    await clickOn(buttons().find((b) => b.textContent === "Not specified"));
    // only the answer is lost (no data besides the discriminator), so no
    // confirmation is asked
    const remove = [...document.querySelectorAll(".ui.modal button")].find(
      (b) => b.textContent === "Remove"
    );
    expect(remove).toBeUndefined();
    expect(probe()).toBeNull();
  });

  it("with assessed Yes, the Purity method label carries the required marker", async () => {
    container = renderInForm(controls(), {
      initialValues: polymer({ purity: { assessed: "Yes" } }),
    });
    const methodLabel = [...container.querySelectorAll(".field label")].find(
      (l) => l.textContent.includes("Method")
    );
    expect(methodLabel.closest(".field").className).toContain("required");
  });

  it("writes the clicked percentage exactly (the space is part of the value)", async () => {
    container = renderInForm(controls(), {
      initialValues: polymer({ purity: { assessed: "Yes" } }),
    });
    await clickOn(buttons().find((b) => b.textContent === ">95 %"));
    expect(probe()).toEqual({
      purity: { assessed: "Yes", purity_percentage: ">95 %" },
    });
  });

  it("shows a purity_percentage error at the field and keeps it after an unrelated edit", async () => {
    container = renderInForm(controls(), {
      initialValues: polymer({
        purity: { assessed: "Yes", method: "SDS-PAGE" },
      }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                quality_controls: {
                  purity: {
                    purity_percentage: "Missing data for required field.",
                  },
                },
              },
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
