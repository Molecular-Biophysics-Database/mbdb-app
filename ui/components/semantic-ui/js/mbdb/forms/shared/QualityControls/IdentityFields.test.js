import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  ValueProbe,
  readProbe,
  typeInto,
  pickDropdown,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { IdentityFields } from "./index";
import {
  INTACT_MASS_METHODS,
  SEQUENCING_METHODS,
  FINGERPRINTING_METHODS,
} from "./constants";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

const PATH = "identity";

let container;

beforeEach(() => {
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const fields = () => (
  <>
    <IdentityFields fieldPath={PATH} />
    <ValueProbe path={PATH} />
  </>
);

const probe = () => readProbe(container);
const HINT = "Select at least one method, or choose No.";

// SUI Checkbox reads the native checked flag on change
const toggleCheckbox = async (label) => {
  const input = [...container.querySelectorAll(".ui.checkbox")]
    .find((c) => c.textContent.includes(label))
    .querySelector('input[type="checkbox"]');
  input.checked = !input.checked;
  await act(async () => {
    Simulate.change(input);
    await new Promise((r) => setTimeout(r, 0));
  });
};

describe("QualityControls method enums", () => {
  it("INTACT_MASS_METHODS equals the model enum", () => {
    expect(INTACT_MASS_METHODS).toEqual(yamlEnum("By_intact_mass", "method"));
  });
  it("SEQUENCING_METHODS equals the model enum", () => {
    expect(SEQUENCING_METHODS).toEqual(yamlEnum("By_sequencing", "method"));
  });
  it("FINGERPRINTING_METHODS equals the model enum", () => {
    expect(FINGERPRINTING_METHODS).toEqual(
      yamlEnum("By_fingerprinting", "method")
    );
  });
});

describe("IdentityFields", () => {
  it("shows the no-method hint and hides it once a method is picked", async () => {
    container = renderInForm(fields(), {
      initialValues: { [PATH]: { assessed: "Yes" } },
    });
    expect(container.textContent).toContain(HINT);
    await toggleCheckbox("By sequencing");
    await pickDropdown(`${PATH}.by_sequencing.method`, "Sanger sequencing");
    expect(container.textContent).not.toContain(HINT);
  });

  it("checking By fingerprinting writes nothing; picking its method writes it", async () => {
    container = renderInForm(fields(), {
      initialValues: { [PATH]: { assessed: "Yes" } },
    });
    await toggleCheckbox("By fingerprinting");
    // the open toggle is local state until something is entered
    expect(probe()).toEqual({ assessed: "Yes" });
    await pickDropdown(
      `${PATH}.by_fingerprinting.method`,
      "Protease digest + Mass spectrometry"
    );
    expect(probe()).toEqual({
      assessed: "Yes",
      by_fingerprinting: { method: "Protease digest + Mass spectrometry" },
    });
  });

  it('typing 0.5 into the deviation writes { value: 0.5, unit: "Da" }', async () => {
    container = renderInForm(fields(), {
      initialValues: { [PATH]: { assessed: "Yes", by_intact_mass: {} } },
    });
    await typeInto(
      document.getElementById(
        `${PATH}.by_intact_mass.deviation_from_expected_mass`
      ),
      "0.5"
    );
    expect(probe()).toEqual({
      assessed: "Yes",
      by_intact_mass: {
        deviation_from_expected_mass: { value: 0.5, unit: "Da" },
      },
    });
  });

  it("unparseable coverage leaves by_sequencing.coverage absent", async () => {
    container = renderInForm(fields(), {
      initialValues: { [PATH]: { assessed: "Yes", by_sequencing: {} } },
    });
    await typeInto(
      document.getElementById(`${PATH}.by_sequencing.coverage`),
      "abc"
    );
    // "" and unparseable input both clear (NumberField's empty-write
    // pruning): html number inputs report garbage as "", and clearing the
    // only key of by_sequencing prunes the empty object with it (guide §7)
    expect(probe()).toEqual({ assessed: "Yes" });
  });
});
