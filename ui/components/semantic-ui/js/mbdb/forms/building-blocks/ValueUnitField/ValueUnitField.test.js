import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { Field } from "formik";
import { ValueUnitField } from "./ValueUnitField";
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

const numberInput = () => container.querySelector('input[type="number"]');
const typeValue = (value) => {
  numberInput().value = value;
  act(() => {
    Simulate.change(numberInput());
  });
};
const clickUnit = (text) => {
  const item = [...container.querySelectorAll(".dropdown .menu .item")].find(
    (el) => el.textContent.trim() === text
  );
  expect(item).toBeDefined();
  act(() => {
    Simulate.click(item);
  });
};

const field = (
  <>
    <ValueUnitField
      fieldPath="mw"
      label="Molecular weight"
      units={["Da", "kDa", "MDa"]}
      defaultUnit="kDa"
      help="The molecular weight of the polymer"
    />
    <ValueProbe path="mw" />
  </>
);

describe("ValueUnitField", () => {
  it("shows the default unit in the dropdown without writing it", () => {
    render(field);
    expect(container.querySelector(".dropdown .text").textContent).toBe("kDa");
    expect(readProbe(container)).toBeNull();
    expect(container.querySelector("label.helptext").textContent).toBe(
      "The molecular weight of the polymer"
    );
  });

  it("popup mode: no helptext under the control, one help icon next to the label", () => {
    render(field, { helpMode: "popup" });
    expect(container.querySelector("label.helptext")).toBeNull();
    expect(container.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("links label and input and gives the unit dropdown an aria-label", () => {
    render(field);
    expect(numberInput().id).toBe("mw");
    expect(container.querySelector("label").getAttribute("for")).toBe("mw");
    expect(
      container.querySelector(".dropdown").getAttribute("aria-label")
    ).toBe("Unit");
  });

  it("writes value as a number together with the default unit", () => {
    render(field);
    typeValue("14305.5");
    expect(readProbe(container)).toEqual({ value: 14305.5, unit: "kDa" });
  });

  it("keeps a unit picked while empty in local state and writes it with the value", () => {
    render(field);
    clickUnit("Da");
    // no partial { unit } ever reaches Formik
    expect(readProbe(container)).toBeNull();
    expect(container.querySelector(".dropdown .text").textContent).toBe("Da");
    typeValue("10");
    expect(readProbe(container)).toEqual({ value: 10, unit: "Da" });
  });

  it("removes the whole object when the value is cleared (default unit)", () => {
    render(field, {
      initialValues: { mw: { value: 14305.5, unit: "kDa" } },
    });
    typeValue("");
    expect(readProbe(container)).toBeNull();
  });

  it("removes the whole object and resets the unit when the value is cleared (non-default unit)", () => {
    render(field, {
      initialValues: { mw: { value: 14305.5, unit: "Da" } },
    });
    typeValue("");
    expect(readProbe(container)).toBeNull();
    // the picked unit does not linger: the dropdown shows the default again
    expect(container.querySelector(".dropdown .text").textContent).toBe("kDa");
  });

  it("shows errors on value or unit under the control", () => {
    render(field, {
      initialValues: { mw: { unit: "kDa" } },
      initialErrors: { mw: { value: "Missing data for required field." } },
    });
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it("shows an object-level error (missing required quantity)", () => {
    render(field, {
      initialErrors: { mw: "Missing data for required field." },
    });
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it("shows the message of a { message, severity } error object", () => {
    render(field, {
      initialErrors: {
        mw: { value: { message: "Bad number.", severity: "error" } },
      },
      initialValues: { mw: { value: 1, unit: "kDa" } },
    });
    expect(container.textContent).toContain("Bad number.");
  });

  it('does not show a { severity: "warning" } node as an error', () => {
    render(field, {
      initialErrors: {
        mw: { value: { message: "Big number.", severity: "warning" } },
      },
      initialValues: { mw: { value: 1, unit: "kDa" } },
    });
    expect(container.querySelector(".field.error")).toBeNull();
    expect(container.textContent).not.toContain("Big number.");
  });

  it("keeps an initialError visible after another field is edited", () => {
    render(
      <>
        <ValueUnitField
          fieldPath="mw"
          label="Molecular weight"
          units={["Da", "kDa", "MDa"]}
          defaultUnit="kDa"
        />
        <Field data-testid="other" name="other" />
      </>,
      {
        initialValues: { mw: { value: 1, unit: "kDa" } },
        initialErrors: { mw: { value: "Missing data for required field." } },
      }
    );
    expect(container.textContent).toContain("Missing data for required field.");
    // Validation on the first edit resets `errors` to {}; the server
    // error must still be shown.
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    act(() => {
      Simulate.change(other);
    });
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });
});
