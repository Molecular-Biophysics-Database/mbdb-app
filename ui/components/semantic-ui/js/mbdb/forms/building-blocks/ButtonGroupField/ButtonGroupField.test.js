import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, Field, useFormikContext, getIn } from "formik";
import { HelpModeProvider } from "mbdb-semantic-ui-react";
import { ButtonGroupField } from "./ButtonGroupField";

jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: () => ({
      label: undefined,
      helpText: undefined,
      required: undefined,
    }),
  }),
}));

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const v = getIn(values, path);
  return <span data-testid="value">{v === undefined ? "-" : String(v)}</span>;
};

Probe.propTypes = {
  path: PropTypes.string,
};

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const render = (ui, { initialValues = {}, initialErrors = {} } = {}) => {
  act(() => {
    ReactDOM.render(
      <Formik
        initialValues={initialValues}
        initialErrors={initialErrors}
        onSubmit={() => {}}
      >
        {ui}
      </Formik>,
      container
    );
  });
};

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);
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
        <Probe path="source" />
      </>
    );
    const group = container.querySelector('[role="group"]');
    expect(group).not.toBeNull();
    expect(buttons().length).toBe(3);

    click("Recombinantly");
    expect(byTestId("value").textContent).toBe("Recombinantly");
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
        <Probe path="source" />
      </>
    );
    click("Natively");
    expect(byTestId("value").textContent).toBe("Natively");
    click("Natively");
    expect(byTestId("value").textContent).toBe("-");
  });

  it("keeps the value when the field is required", () => {
    render(
      <>
        <ButtonGroupField fieldPath="source" required options={OPTIONS} />
        <Probe path="source" />
      </>
    );
    click("Natively");
    click("Natively");
    expect(byTestId("value").textContent).toBe("Natively");
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
        <Probe path="hom" />
      </>
    );
    click("No");
    expect(byTestId("value").textContent).toBe("false");
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
      <HelpModeProvider mode="popup">
        <ButtonGroupField
          fieldPath="source"
          label="Expression source type"
          help="How the polymer was produced"
          options={OPTIONS}
        />
      </HelpModeProvider>
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
});
