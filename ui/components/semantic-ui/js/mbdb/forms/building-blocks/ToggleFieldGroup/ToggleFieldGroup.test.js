import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext } from "formik";
import { ToggleFieldGroup } from "./ToggleFieldGroup";
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

const mount = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

const probe = () => readProbe(container);
const checkbox = () => container.querySelector('input[type="checkbox"]');
// SUI Checkbox reads the native checked flag on change
const toggle = () => {
  checkbox().checked = !checkbox().checked;
  act(() => Simulate.change(checkbox()));
};
// A Formik-connected input for an unrelated field, so Simulate.change drives
// Formik's setFieldValue (and its async errors reset) — used by the errors-after-edit test.
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

const group = (props = {}, { withUnrelated = false } = {}) => (
  <>
    <ToggleFieldGroup
      fieldPath="identity.by_intact_mass"
      label="By intact mass"
      initialValue={{ method: "Mass spectrometry" }}
      {...props}
    >
      <span data-testid="body">FIELDS</span>
    </ToggleFieldGroup>
    <ValueProbe path="identity" />
    {withUnrelated && <UnrelatedInput />}
  </>
);

describe("ToggleFieldGroup", () => {
  it("is unchecked when the value is undefined and hides the body", () => {
    mount(group());
    expect(checkbox().checked).toBe(false);
    expect(container.querySelector('[data-testid="body"]')).toBeNull();
    expect(container.textContent).toContain("By intact mass");
  });

  it("keeps a <label> element inside the .ui.checkbox (the box is drawn from label:before)", () => {
    // Regression: passing a React node as Checkbox `label` makes semantic-ui-react
    // skip its own <label> (createHTMLLabel), so the checkbox square vanished.
    mount(group());
    expect(container.querySelector(".ui.checkbox > label")).not.toBeNull();
  });

  it("popup mode: no helptext under the checkbox, one help icon in its label", () => {
    mount(group({ help: "Measured by intact mass spectrometry" }), {
      helpMode: "popup",
    });
    expect(container.querySelector("label.helptext")).toBeNull();
    expect(container.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("checking writes initialValue and shows the indented body", () => {
    mount(group());
    toggle();
    expect(probe()).toEqual({
      by_intact_mass: { method: "Mass spectrometry" },
    });
    const body = container.querySelector('[data-testid="body"]');
    expect(body).not.toBeNull();
    expect(body.closest(".mbdb-indent")).not.toBeNull();
  });

  it("checking with an empty initialValue writes nothing but still opens (F2)", () => {
    mount(group({ initialValue: {} }));
    toggle();
    // checked (via local open state) and body visible, but no `{}` written
    expect(checkbox().checked).toBe(true);
    expect(container.querySelector('[data-testid="body"]')).not.toBeNull();
    expect(probe()).toBeNull(); // identity is not even created
  });

  it("is checked when a value exists", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: { deviation: "0.5" } } },
    });
    expect(checkbox().checked).toBe(true);
    expect(container.querySelector('[data-testid="body"]')).not.toBeNull();
  });

  it("unchecking an empty object removes it without confirmation, and empty parents are pruned", () => {
    mount(group(), { initialValues: { identity: { by_intact_mass: {} } } });
    toggle();
    // pruning unset: `by_intact_mass` was `identity`'s only key — the object
    // is gone entirely, never left as `{}` (guide §7)
    expect(probe()).toBeNull();
    expect(document.body.querySelector(".ui.modal")).toBeNull();
  });

  it("unchecking with data asks for confirmation, then removes", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: { deviation: "0.5" } } },
    });
    toggle();
    const modal = document.body.querySelector(".ui.modal");
    expect(modal).not.toBeNull();
    expect(modal.textContent).toContain("Remove By intact mass?");
    expect(probe()).toEqual({ by_intact_mass: { deviation: "0.5" } }); // still there

    const cancelBtn = [...modal.querySelectorAll("button")].find(
      (b) => b.textContent === "Cancel"
    );
    act(() => Simulate.click(cancelBtn));
    expect(probe()).toEqual({ by_intact_mass: { deviation: "0.5" } });

    toggle();
    const removeBtn = [
      ...document.body.querySelector(".ui.modal").querySelectorAll("button"),
    ].find((b) => b.textContent === "Remove");
    act(() => Simulate.click(removeBtn));
    expect(probe()).toBeNull();
  });

  it("marks the header on errors under fieldPath", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: {} } },
      initialErrors: { identity: { by_intact_mass: { method: "Required." } } },
    });
    // the header label carries the state; the field itself is not `.error`
    // (that would colour every child field)
    expect(container.querySelector("label.mbdb-error-text")).not.toBeNull();
    expect(container.querySelector(".field.error")).toBeNull();
  });

  it("keeps the error header after an unrelated edit clears Formik's errors", async () => {
    mount(group({}, { withUnrelated: true }), {
      initialValues: { identity: { by_intact_mass: {} }, other: "" },
      initialErrors: { identity: { by_intact_mass: { method: "Required." } } },
    });
    expect(container.querySelector("label.mbdb-error-text")).not.toBeNull();

    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    await act(async () => Simulate.change(other));
    expect(container.querySelector("label.mbdb-error-text")).not.toBeNull();
  });

  it("uses the DiscriminatorField confirm wording (F6)", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: { deviation: "0.5" } } },
    });
    toggle();
    const modal = document.body.querySelector(".ui.modal");
    expect(modal.textContent).toContain("The entered data will be removed.");
    expect(modal.textContent).not.toContain("This cannot be undone.");
  });
});
