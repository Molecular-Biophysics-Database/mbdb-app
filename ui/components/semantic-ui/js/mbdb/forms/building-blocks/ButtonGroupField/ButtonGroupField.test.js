import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
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

jest.mock("mbdb-semantic-ui-react", () => ({
  ...jest.requireActual("mbdb-semantic-ui-react"),
  ...jest.requireActual("mbdb-semantic-ui-react/FieldHelp"),
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
  it("renders a radiogroup with all options and sets the value on click", () => {
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
    const group = container.querySelector('[role="radiogroup"]');
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

  it("moves focus between options with arrow keys", () => {
    render(<ButtonGroupField fieldPath="source" options={OPTIONS} />);
    const group = container.querySelector('[role="radiogroup"]');
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
