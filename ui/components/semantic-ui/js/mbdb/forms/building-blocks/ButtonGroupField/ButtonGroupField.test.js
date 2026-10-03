import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { Field } from "formik";
import { ButtonGroupField } from "./ButtonGroupField";
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

const buttons = () => [...container.querySelectorAll("button")];
const buttonByText = (text) =>
  buttons().find((b) => b.textContent.trim() === text);
const click = (text) =>
  act(() => {
    Simulate.click(buttonByText(text));
  });

const OPTIONS = ["Natively", "Recombinantly", "Synthetically"];

describe("ButtonGroupField", () => {
  it("renders a group with all options and sets the value on click", () => {
    render(
      <>
        <ButtonGroupField
          fieldPath="source"
          label="Expression source type"
          options={OPTIONS}
        />
        <ValueProbe path="source" />
      </>
    );
    const group = container.querySelector('[role="group"]');
    expect(group).not.toBeNull();
    expect(buttons().length).toBe(3);

    click("Recombinantly");
    expect(readProbe(container)).toBe("Recombinantly");
    expect(buttonByText("Recombinantly").classList.contains("primary")).toBe(
      true
    );
    expect(buttonByText("Recombinantly").getAttribute("aria-pressed")).toBe(
      "true"
    );
  });

  it("clears the value when the active button is clicked again (optional)", () => {
    render(
      <>
        <ButtonGroupField fieldPath="source" options={OPTIONS} />
        <ValueProbe path="source" />
      </>
    );
    click("Natively");
    expect(readProbe(container)).toBe("Natively");
    click("Natively");
    expect(readProbe(container)).toBeNull();
  });

  it("keeps the value when the field is required", () => {
    render(
      <>
        <ButtonGroupField fieldPath="source" required options={OPTIONS} />
        <ValueProbe path="source" />
      </>
    );
    click("Natively");
    click("Natively");
    expect(readProbe(container)).toBe("Natively");
  });

  it("supports boolean option values", () => {
    render(
      <>
        <ButtonGroupField
          fieldPath="hom"
          options={[
            { value: true, text: "Yes" },
            { value: false, text: "No" },
          ]}
        />
        <ValueProbe path="hom" />
      </>
    );
    click("No");
    expect(readProbe(container)).toBe(false);
    expect(buttonByText("No").getAttribute("aria-pressed")).toBe("true");
  });

  it("shows the error from initialErrors", () => {
    render(<ButtonGroupField fieldPath="source" options={OPTIONS} />, {
      initialValues: { source: "Natively" },
      initialErrors: { source: "Not a valid choice." },
    });
    expect(container.textContent).toContain("Not a valid choice.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it("keeps an initialError visible after another field is edited", () => {
    render(
      <>
        <ButtonGroupField fieldPath="source" options={OPTIONS} />
        <Field data-testid="other" name="other" />
      </>,
      {
        initialValues: { source: "Natively" },
        initialErrors: { source: "Not a valid choice." },
      }
    );
    expect(container.textContent).toContain("Not a valid choice.");
    // Validation on the first edit resets `errors` to {}; the server
    // error at `source` must still be shown.
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    act(() => {
      Simulate.change(other);
    });
    expect(container.textContent).toContain("Not a valid choice.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it("shows the message of a { message, severity } error object", () => {
    render(<ButtonGroupField fieldPath="source" options={OPTIONS} />, {
      initialValues: { source: "Natively" },
      initialErrors: {
        source: { message: "Not a valid choice.", severity: "error" },
      },
    });
    expect(container.textContent).toContain("Not a valid choice.");
  });

  it('does not show a { severity: "warning" } node as an error', () => {
    render(<ButtonGroupField fieldPath="source" options={OPTIONS} />, {
      initialValues: { source: "Natively" },
      initialErrors: {
        source: { message: "Sounds wrong.", severity: "warning" },
      },
    });
    expect(container.querySelector(".field.error")).toBeNull();
    expect(container.textContent).not.toContain("Sounds wrong.");
  });

  it("popup mode: no helptext label, one help icon next to the label", () => {
    render(
      <ButtonGroupField
        fieldPath="source"
        label="Expression source type"
        help="How the polymer was produced"
        options={OPTIONS}
      />,
      { helpMode: "popup" }
    );
    expect(container.querySelector("label.helptext")).toBeNull();
    expect(container.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("falls back to a SelectField for more than 5 options", () => {
    render(
      <ButtonGroupField
        fieldPath="source"
        options={["a", "b", "c", "d", "e", "f"]}
      />
    );
    expect(container.querySelector(".ui.dropdown")).not.toBeNull();
    expect(container.querySelector('[role="group"]')).toBeNull();
  });

  it("moves focus between options with arrow keys", () => {
    render(<ButtonGroupField fieldPath="source" options={OPTIONS} />);
    const group = container.querySelector('[role="group"]');
    buttons()[0].focus();
    expect(document.activeElement).toBe(buttons()[0]);
    act(() => {
      Simulate.keyDown(group, { key: "ArrowRight" });
    });
    expect(document.activeElement).toBe(buttons()[1]);
    act(() => {
      Simulate.keyDown(group, { key: "ArrowLeft" });
    });
    expect(document.activeElement).toBe(buttons()[0]);
  });

  it("clearing the only value of an object removes the object key, not leaves {}", () => {
    // D4: optional group whose value is the only key of `obj`. Toggle the
    // active button off × the parent object must be dropped, not left empty.
    render(
      <>
        <ButtonGroupField fieldPath="obj.opt" options={["A", "B"]} />
        <ValueProbe path="obj" />
      </>,
      { initialValues: { obj: { opt: "A" } } }
    );
    expect(readProbe(container)).toEqual({ opt: "A" });
    click("A"); // toggle the active button off
    expect(readProbe(container)).toBeNull();
  });
});
