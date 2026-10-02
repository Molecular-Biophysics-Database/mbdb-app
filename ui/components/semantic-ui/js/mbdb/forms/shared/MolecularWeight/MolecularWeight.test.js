import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { Field } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  yamlEnum,
  ValueProbe,
  readProbe,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { MolecularWeight, MOLECULAR_WEIGHT_UNITS } from "./MolecularWeight";

jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// Used at entities_of_interest.<i>.molecular_weight (Polymer, Molecular
// assembly, polymer components) — required there.
const PATH =
  "metadata.general_parameters.entities_of_interest.0.molecular_weight";

const UI_MODEL = {
  [PATH]: {
    label: "Molecular weight",
    helpText: "The molecular weight of the polymer",
    required: true,
  },
};

let container;

beforeEach(() => {
  setFakeUiModel(UI_MODEL);
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

// typing into the Semantic number Input — Simulate.change reads the value
// from the element (the blocks' onChange paths run inside act)
const typeValue = async (value) => {
  const input = container.querySelector('input[type="number"]');
  input.value = value;
  await act(async () => {
    Simulate.change(input);
  });
};

const clickUnit = async (text) => {
  const item = [...container.querySelectorAll(".dropdown .menu .item")].find(
    (el) => el.textContent.trim() === text
  );
  await act(async () => {
    Simulate.click(item);
  });
};

const probe = () => readProbe(container);

describe("MolecularWeight", () => {
  it("the unit list matches the YAML MOLECULAR_WEIGHT_UNITS enum", () => {
    // read from the model so a model change or a retyped character fails
    expect(MOLECULAR_WEIGHT_UNITS).toEqual(yamlEnum("MOLECULAR_WEIGHT_UNITS"));
  });

  it("offers exactly MOLECULAR_WEIGHT_UNITS in the dropdown, none pre-written", () => {
    render(
      <>
        <MolecularWeight fieldPath={PATH} />
        <ValueProbe path={PATH} />
      </>
    );
    const shown = [...container.querySelectorAll(".dropdown .menu .item")].map(
      (el) => el.textContent.trim()
    );
    expect(shown).toEqual(MOLECULAR_WEIGHT_UNITS);
    // kDa is pre-selected in the control but nothing is stored
    expect(container.querySelector(".dropdown .text").textContent).toBe("kDa");
    expect(probe()).toBeNull();
  });

  it("typing 34.8 stores { value: 34.8, unit: kDa } with a numeric value", async () => {
    render(
      <>
        <MolecularWeight fieldPath={PATH} />
        <ValueProbe path={PATH} />
      </>
    );
    await typeValue("34.8");
    const stored = probe();
    expect(stored).toEqual({ value: 34.8, unit: "kDa" });
    expect(typeof stored.value).toBe("number");
  });

  it("a unit picked before the value is written together with the value", async () => {
    render(
      <>
        <MolecularWeight fieldPath={PATH} />
        <ValueProbe path={PATH} />
      </>
    );
    await clickUnit("Da");
    // the pick stays local: no partial { unit } object
    expect(probe()).toBeNull();
    await typeValue("10");
    expect(probe()).toEqual({ value: 10, unit: "Da" });
  });

  it("clearing the value removes the whole object", async () => {
    render(
      <>
        <MolecularWeight fieldPath={PATH} />
        <ValueProbe path={PATH} />
      </>,
      {
        initialValues: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                { molecular_weight: { value: 64.5, unit: "kDa" } },
              ],
            },
          },
        },
      }
    );
    await typeValue("");
    expect(probe()).toBeNull();
  });

  it("shows the object-level server error, still shown after an unrelated edit", async () => {
    render(
      <>
        <MolecularWeight fieldPath={PATH} />
        <Field data-testid="other" name="unrelated" />
      </>,
      {
        initialErrors: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                { molecular_weight: "Missing data for required field." },
              ],
            },
          },
        },
      }
    );
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();

    // formik clears `errors` on the first edit anywhere (no validate); the
    // server error must keep showing from initialErrors.
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    await act(async () => {
      Simulate.change(other);
    });
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it("accepts a different default unit (manual chemicals use g/mol)", () => {
    render(<MolecularWeight fieldPath={PATH} defaultUnit="g/mol" />);
    expect(container.querySelector(".dropdown .text").textContent).toBe(
      "g/mol"
    );
  });
});
