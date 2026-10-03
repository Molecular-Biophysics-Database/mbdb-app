import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  ValueProbe,
  readProbe,
  typeInto,
  clickOn,
  editUnrelatedField,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { Modifications, ModificationTable, stepsLabel } from "./index";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// Client-only row keys (jsdom has no WebCrypto).
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const MODIFICATIONS = `${ENTITY}.modifications`;
const ASSEMBLY = `${ENTITY}.chemical_modifications`;

let container;

beforeEach(() => {
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const polymer = (modifications) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        { type: "Polymer", name: "Hemoglobin subunit beta", modifications },
      ],
    },
  },
});

const FILLED = {
  biological_postprocessing: [{ type: "Phosphorylation", position: "S10" }],
  chemical: [
    {
      type: "Deglycosylation",
      position: "N45",
      protocol: [
        { name: "PNGase F", description: "37 °C overnight" },
        { name: "Desalting", description: "Zeba spin column" },
      ],
    },
  ],
};

const modifications = () => (
  <>
    <Modifications fieldPath={MODIFICATIONS} />
    <ValueProbe path={MODIFICATIONS} />
  </>
);

const assembly = () => (
  <>
    <ModificationTable fieldPath={ASSEMBLY} />
    <ValueProbe path={ASSEMBLY} />
  </>
);

const probe = () => readProbe(container);
const buttons = () => [...container.querySelectorAll("button")];
const toggleTexts = () =>
  buttons()
    .map((b) => b.textContent)
    .filter((t) => /\d+ steps|1 step|No protocol/.test(t));

describe("stepsLabel", () => {
  it("labels the protocol count", () => {
    expect(stepsLabel(undefined)).toBe("No protocol");
    expect(stepsLabel([])).toBe("No protocol");
    expect(stepsLabel([{ name: "a" }])).toBe("1 step");
    expect(stepsLabel([{ name: "a" }, { name: "b" }])).toBe("2 steps");
  });
});

describe("Modifications", () => {
  it("renders the filled rows of both lists with their protocol toggles", () => {
    container = renderInForm(modifications(), {
      initialValues: polymer(FILLED),
    });
    const types = [...container.querySelectorAll('input[aria-label="Type"]')];
    expect(types.map((i) => i.value)).toEqual([
      "Phosphorylation",
      "Deglycosylation",
    ]);
    expect(toggleTexts()).toEqual(["No protocol ▸", "2 steps ▸"]);
  });

  it("names each list in the Add button's aria-label (the two tables share the text)", () => {
    container = renderInForm(modifications(), {
      initialValues: polymer(),
    });
    const labels = [
      ...container.querySelectorAll(
        'button[aria-label^="Add modification to "]'
      ),
    ].map((b) => b.getAttribute("aria-label"));
    expect(labels).toEqual([
      "Add modification to Biological postprocessing",
      "Add modification to Chemical",
    ]);
  });

  it("opens the protocol table and writes steps to <list>.<i>.protocol", async () => {
    container = renderInForm(modifications(), {
      initialValues: polymer({
        chemical: [{ type: "Biotinylation" }],
      }),
    });
    await clickOn(buttons().find((b) => b.textContent === "No protocol ▸"));
    // the design scenario: "Add step" writes [{}] there
    await clickOn(buttons().find((b) => b.textContent.includes("Add step")));
    expect(probe()).toEqual({
      chemical: [{ type: "Biotinylation", protocol: [{}] }],
    });
  });

  it("auto-opens a row with a nested protocol error and keeps the message after an unrelated edit", async () => {
    container = renderInForm(
      <>
        <Modifications fieldPath={MODIFICATIONS} />
        <ValueProbe path={MODIFICATIONS} />
      </>,
      {
        initialValues: polymer({
          chemical: [
            {
              type: "Deglycosylation",
              protocol: [
                { name: "PNGase F", description: "37 °C" },
                { name: "Desalting" },
              ],
            },
          ],
        }),
        initialErrors: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                {
                  modifications: {
                    chemical: [
                      {
                        protocol: [
                          null,
                          { description: "Missing data for required field." },
                        ],
                      },
                    ],
                  },
                },
              ],
            },
          },
        },
        withUnrelatedField: true,
      }
    );
    // row 1 of chemical is open without a click: the nested Protocol table
    // is rendered (its "Add step" button exists)
    const addStep = buttons().find((b) => b.textContent.includes("Add step"));
    expect(addStep).toBeDefined();
    // the message shows in the description cell
    const messages = () =>
      [...container.querySelectorAll(".ui.pointing.prompt.label")].map(
        (l) => l.textContent
      );
    expect(messages()).toContain("Missing data for required field.");
    await editUnrelatedField(container);
    expect(messages()).toContain("Missing data for required field.");
  });

  it("removing the only row of the only list leaves modifications absent, not {}", async () => {
    container = renderInForm(
      <>
        <Modifications fieldPath={MODIFICATIONS} />
        <ValueProbe path={MODIFICATIONS} />
      </>,
      { initialValues: polymer({ chemical: [{ type: "Biotinylation" }] }) }
    );
    await clickOn(container.querySelector('button[aria-label="Remove row 1"]'));
    expect(probe()).toBeNull();
  });

  it("ModificationTable at chemical_modifications writes there and nowhere else", async () => {
    container = renderInForm(assembly(), {
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ type: "Molecular assembly" }],
          },
        },
      },
    });
    await clickOn(
      buttons().find((b) => b.textContent.includes("Add modification"))
    );
    await typeInto(
      container.querySelector('input[aria-label="Type"]'),
      "Biotinylation"
    );
    expect(probe()).toEqual([{ type: "Biotinylation" }]);
  });
});
