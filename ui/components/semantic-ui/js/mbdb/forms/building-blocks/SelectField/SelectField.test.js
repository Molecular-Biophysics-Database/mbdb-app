import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { SelectField } from "./SelectField";
import {
  renderInForm,
  unmountForm,
  ValueProbe,
  readProbe,
} from "@js/mbdb/forms/building-blocks/testUtils";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

let container;

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});
const clickItem = (text) => {
  const item = [...container.querySelectorAll(".menu .item")].find(
    (el) => el.textContent.trim() === text
  );
  expect(item).toBeDefined();
  act(() => {
    Simulate.click(item);
  });
};

describe("SelectField", () => {
  it("selects a string option and stores the string value", () => {
    render(
      <>
        <SelectField
          fieldPath="pt"
          label="Polymer type"
          options={["polypeptide(L)", "polypeptide(D)"]}
        />
        <ValueProbe path="pt" />
      </>
    );
    clickItem("polypeptide(D)");
    expect(readProbe(container)).toBe("polypeptide(D)");
  });

  it("is clearable when optional and not clearable when required", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "a" },
    });
    expect(container.querySelector(".dropdown i.icon.clear")).not.toBeNull();

    render(<SelectField fieldPath="pt" required options={["a", "b"]} />, {
      initialValues: { pt: "a" },
    });
    expect(container.querySelector(".dropdown i.icon.clear")).toBeNull();
  });

  it("removes the key when cleared via the clear icon", () => {
    render(
      <>
        <SelectField fieldPath="pt" options={["a", "b"]} />
        <ValueProbe path="pt" />
      </>,
      { initialValues: { pt: "a" } }
    );
    const clearIcon = container.querySelector(".dropdown i.icon.clear");
    act(() => {
      Simulate.click(clearIcon);
    });
    expect(readProbe(container)).toBeNull();
  });

  it("keeps an unknown stored value visible and marks it with a label", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "old-value" },
    });
    // RIF ensureSelectedValuesInOptions keeps it displayed
    expect(container.querySelector(".dropdown .text").textContent).toContain(
      "old-value"
    );
    expect(container.textContent).toContain("Unknown value");
  });

  it("lets a known value through without the Unknown value label", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "a" },
    });
    expect(container.textContent).not.toContain("Unknown value");
  });

  it("shows the error from initialErrors", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "a" },
      initialErrors: { pt: "Missing data for required field." },
    });
    expect(container.textContent).toContain("Missing data for required field.");
  });
});
