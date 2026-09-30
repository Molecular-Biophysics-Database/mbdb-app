import React from "react";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { Formik } from "formik";
import { FieldGroup } from "./FieldGroup";

// The alias index.js does not export FieldHelp yet; simulate the state
// after that one-line export is added.
jest.mock("mbdb-semantic-ui-react", () => ({
  ...jest.requireActual("mbdb-semantic-ui-react"),
  ...jest.requireActual("mbdb-semantic-ui-react/FieldHelp"),
}));

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

describe("FieldGroup", () => {
  it("renders header as h5 with fieldPath id, help and children", () => {
    render(
      <FieldGroup
        title="Molecular weight"
        help="The molecular weight of the polymer"
        fieldPath="metadata.mw"
      >
        <input data-testid="child" />
      </FieldGroup>
    );
    const header = container.querySelector("h5.ui.header");
    expect(header.textContent).toBe("Molecular weight");
    expect(header.id).toBe("metadata.mw");
    expect(header.classList.contains("red")).toBe(false);
    expect(container.querySelector("label.helptext").textContent).toBe(
      "The molecular weight of the polymer"
    );
    expect(container.querySelector('[data-testid="child"]')).not.toBeNull();
  });

  it("turns the header red when an error exists under fieldPath", () => {
    render(
      <FieldGroup title="Mw" fieldPath="metadata.mw">
        fields
      </FieldGroup>,
      { initialErrors: { metadata: { mw: { value: "Required" } } } }
    );
    expect(container.querySelector("h5.ui.header.red")).not.toBeNull();
  });

  it("does not mark errors outside of fieldPath", () => {
    render(
      <FieldGroup title="Mw" fieldPath="metadata.mw">
        fields
      </FieldGroup>,
      { initialErrors: { metadata: { other: "Required" } } }
    );
    expect(container.querySelector("h5.ui.header.red")).toBeNull();
  });

  it("lays children out in one Form.Group row when inline", () => {
    render(
      <FieldGroup title="Size" inline>
        <input data-testid="child" />
      </FieldGroup>
    );
    const group = container.querySelector(".fields.equal.width");
    expect(group).not.toBeNull();
    expect(group.querySelector('[data-testid="child"]')).not.toBeNull();
  });

  it("shows the required asterisk in the header", () => {
    render(<FieldGroup title="Mw" required fieldPath="metadata.mw" />);
    expect(container.querySelector("h5.ui.header").textContent).toBe("Mw *");
  });
});
