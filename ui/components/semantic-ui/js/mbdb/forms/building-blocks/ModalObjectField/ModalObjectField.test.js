import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import { Input } from "mbdb-semantic-ui-react";
import { ModalObjectField } from "./ModalObjectField";
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

const TemperatureForm = ({ fieldPath }) => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <Input
      aria-label="Temperature"
      value={getIn(values, `${fieldPath}.temperature`) ?? ""}
      onChange={(e) =>
        setFieldValue(`${fieldPath}.temperature`, e.target.value)
      }
    />
  );
};
TemperatureForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};

const mount = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

const probe = () => readProbe(container);
const modal = () => document.body.querySelector(".ui.modal");
const modalButton = (label) =>
  [...modal().querySelectorAll("button")].find((b) => b.textContent === label);
const btn = (label) =>
  [...container.querySelectorAll("button")].find((b) =>
    b.textContent.includes(label)
  );

// A Formik-connected input for an unrelated field, so Simulate.change drives
// Formik's setFieldValue (and its async errors reset) — used by the F1 test.
const UnrelatedInput = () => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <input
      data-testid="other"
      value={values.other ?? ""}
      onChange={(e) => setFieldValue("other", e.target.value)}
    />
  );
};

const storage = (props = {}) => (
  <>
    <ModalObjectField
      fieldPath="storage"
      label="Storage"
      summary={(v) => [v.temperature, v.duration].filter(Boolean).join(", ")}
      initialValue={{ temperature: "4 °C" }}
      renderForm={(p) => <TemperatureForm fieldPath={p} />}
      {...props}
    />
    <ValueProbe path="storage" />
    <UnrelatedInput />
  </>
);

describe("ModalObjectField", () => {
  it("shows the Add button when absent and no summary", () => {
    mount(storage());
    expect(container.textContent).toContain("Storage");
    expect(container.textContent).toContain("Add Storage");
    expect(container.textContent).not.toContain("Edit");
  });

  it("popup mode: no helptext label, one help icon next to the label", () => {
    mount(storage({ help: "How the sample is stored" }), { helpMode: "popup" });
    expect(container.querySelector("label.helptext")).toBeNull();
    expect(container.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("Add sets the initial value, opens the modal; Cancel resets to undefined", () => {
    mount(storage());
    act(() => Simulate.click(btn("Add Storage")));
    expect(probe()).toEqual({ temperature: "4 °C" });
    expect(modal()).not.toBeNull();

    const input = modal().querySelector('input[aria-label="Temperature"]');
    input.value = "−80 °C";
    act(() => Simulate.change(input));
    act(() => Simulate.click(modalButton("Cancel")));
    expect(modal()).toBeNull();
    expect(probe()).toEqual(null);
  });

  it("shows the summary row when present and Edits through the modal", () => {
    mount(storage(), {
      initialValues: { storage: { temperature: "4 °C", duration: "3 days" } },
    });
    expect(container.textContent).toContain("4 °C, 3 days");

    act(() => Simulate.click(btn("Edit")));
    const input = modal().querySelector('input[aria-label="Temperature"]');
    input.value = "−20 °C";
    act(() => Simulate.change(input));
    act(() => Simulate.click(modalButton("Done")));
    expect(probe()).toEqual({ temperature: "−20 °C", duration: "3 days" });
  });

  it("removes after confirmation when data is present; no confirm for empty", () => {
    mount(storage(), { initialValues: { storage: {} } });
    // empty object: no confirm, removed immediately
    act(() =>
      Simulate.click(
        container.querySelector('button[aria-label="Remove Storage"]')
      )
    );
    expect(probe()).toEqual(null);

    // with data: confirm first
    mount(storage(), {
      initialValues: { storage: { temperature: "4 °C" } },
    });
    act(() =>
      Simulate.click(
        container.querySelector('button[aria-label="Remove Storage"]')
      )
    );
    const confirmModal = modal();
    expect(confirmModal).not.toBeNull();
    expect(confirmModal.textContent).toContain("Remove Storage?");
    const confirmBtn = [...confirmModal.querySelectorAll("button")].find(
      (b) => b.textContent === "Remove"
    );
    act(() => Simulate.click(confirmBtn));
    expect(probe()).toEqual(null);
  });

  it("required + absent shows 'Not filled in' and no remove button", () => {
    mount(storage({ required: true }));
    expect(container.textContent).toContain("Not filled in");

    // present + required: no remove
    mount(storage({ required: true }), {
      initialValues: { storage: { temperature: "4 °C" } },
    });
    expect(
      container.querySelector('button[aria-label="Remove Storage"]')
    ).toBeNull();
  });

  it("Edit → change → Cancel restores the original snapshot (F2)", () => {
    mount(storage(), {
      initialValues: { storage: { temperature: "4 °C", duration: "3 days" } },
    });
    act(() => Simulate.click(btn("Edit")));
    const input = modal().querySelector('input[aria-label="Temperature"]');
    input.value = "−20 °C";
    act(() => Simulate.change(input));
    expect(probe()).toEqual({ temperature: "−20 °C", duration: "3 days" });
    act(() => Simulate.click(modalButton("Cancel")));
    expect(probe()).toEqual({ temperature: "4 °C", duration: "3 days" });
  });

  it("Done on an object with no data treats it as Cancel (F4)", () => {
    mount(storage({ initialValue: {} }));
    act(() => Simulate.click(btn("Add Storage")));
    expect(probe()).toEqual({});
    act(() => Simulate.click(modalButton("Done")));
    expect(modal()).toBeNull();
    expect(probe()).toEqual(null);
  });

  it("shows the error badge from initialErrors and opens the modal on click (F2)", async () => {
    mount(storage(), {
      initialValues: { storage: { temperature: "" }, other: "" },
      initialErrors: {
        storage: { temperature: "Missing data for required field." },
      },
    });
    const badge = container.querySelector(".ui.red.label");
    expect(badge.textContent).toBe("1 error");

    // the badge survives an unrelated edit (SummaryItem F1)
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    await act(async () => Simulate.change(other));
    expect(container.querySelector(".ui.red.label").textContent).toBe(
      "1 error"
    );

    // clicking the badge opens the editor
    act(() => Simulate.click(container.querySelector(".ui.red.label")));
    expect(modal()).not.toBeNull();
  });
});
