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
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { Storage, summaryStorage } from "./index";
import { TEMPERATURE_UNITS, TIME_UNITS } from "@js/mbdb/forms/shared/units";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// Client-only row keys (jsdom has no WebCrypto); plan 3R X6.
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const PATH = `${ENTITY}.storage`;

let container;

beforeEach(() => {
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const substance = (storage) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Complex substance of industrial origin",
          name: "Lipid mix",
          ...(storage === undefined ? {} : { storage }),
        },
      ],
    },
  },
});

const FULL = {
  temperature: { value: -80, unit: "°C" },
  duration: { value: 3, unit: "months" },
  storage_preparation: [
    {
      name: "Flash freezing",
      description: "Aliquots frozen in liquid nitrogen",
    },
  ],
};

const storage = () => (
  <>
    <Storage fieldPath={PATH} />
    <ValueProbe path={PATH} />
  </>
);

const probe = () => readProbe(container);
const modal = () => document.body.querySelector(".ui.modal");
const modalButton = (label) =>
  [...modal().querySelectorAll("button")].find((b) => b.textContent === label);
const btn = (label) =>
  [...container.querySelectorAll("button")].find((b) =>
    b.textContent.includes(label)
  );

describe("unit enums", () => {
  it("TEMPERATURE_UNITS equals the model enum", () => {
    expect(TEMPERATURE_UNITS).toEqual(yamlEnum("TEMPERATURE_UNITS"));
  });
  it("TIME_UNITS equals the model enum", () => {
    expect(TIME_UNITS).toEqual(yamlEnum("TIME_UNITS"));
  });
});

describe("summaryStorage", () => {
  it("formats temperature, duration and steps", () => {
    expect(summaryStorage(FULL)).toBe(
      "-80 °C for 3 months, 1 preparation step"
    );
    expect(summaryStorage({ temperature: { value: -80, unit: "°C" } })).toBe(
      "-80 °C"
    );
    expect(
      summaryStorage({
        temperature: FULL.temperature,
        storage_preparation: [{ name: "a" }, { name: "b" }],
      })
    ).toBe("-80 °C, 2 preparation steps");
    expect(summaryStorage({ duration: { value: 3, unit: "months" } })).toBe(
      "for 3 months"
    );
    expect(summaryStorage({})).toBe("");
  });
});

describe("Storage", () => {
  it("Add → type -80 → Done stores the temperature with the default unit", async () => {
    container = renderInForm(storage(), { initialValues: substance() });
    await clickOn(btn("Add Storage"));
    await typeInto(document.getElementById(`${PATH}.temperature`), "-80");
    await clickOn(modalButton("Done"));
    expect(probe()).toEqual({ temperature: { value: -80, unit: "°C" } });
  });

  it("Add → Cancel, and Add → Done without typing: storage absent", async () => {
    container = renderInForm(storage(), { initialValues: substance() });
    await clickOn(btn("Add Storage"));
    await clickOn(modalButton("Cancel"));
    expect(probe()).toBeNull();

    await clickOn(btn("Add Storage"));
    await clickOn(modalButton("Done"));
    expect(probe()).toBeNull();
  });

  it("Edit → change the temperature → Cancel restores the old value", async () => {
    container = renderInForm(storage(), { initialValues: substance(FULL) });
    await clickOn(btn("Edit"));
    await typeInto(document.getElementById(`${PATH}.temperature`), "4");
    await clickOn(modalButton("Cancel"));
    expect(probe()).toEqual(FULL);
  });

  it("shows the row error badge; Edit shows the message under Temperature, staying after an unrelated edit", async () => {
    container = renderInForm(storage(), {
      initialValues: substance({ duration: { value: 3, unit: "months" } }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { storage: { temperature: "Missing data for required field." } },
            ],
          },
        },
      },
      withUnrelatedField: true,
    });
    // the summary row's error badge counts the nested error
    const badge = container.querySelector(".ui.red.label");
    expect(badge).not.toBeNull();
    expect(badge.textContent).toBe("1 error");
    // opening from the badge shows the message at the field in the modal
    await clickOn(badge);
    expect(modal()).not.toBeNull();
    const messages = () =>
      [...modal().querySelectorAll(".ui.pointing.prompt.label")].map(
        (l) => l.textContent
      );
    expect(messages()).toContain("Missing data for required field.");
    await editUnrelatedField(container);
    expect(messages()).toContain("Missing data for required field.");
  });
});
