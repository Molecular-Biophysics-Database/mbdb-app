import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik } from "formik";
import {
  TextField,
  SelectField,
  ArrayField,
  TextAreaField,
} from "mbdb-react-invenio-forms";

jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: () => ({
      label: "Model label",
      helpText: "Model help",
      required: undefined,
    }),
  }),
}));

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

const helptexts = () => [...container.querySelectorAll("label.helptext")];

describe("wrapped fields", () => {
  it("TextField renders model label and exactly one help via FieldHelp", () => {
    render(<TextField fieldPath="name" />, { initialValues: { name: "abc" } });
    expect(container.querySelector("input").value).toBe("abc");
    expect(container.querySelector("label").textContent).toContain(
      "Model label"
    );
    expect(helptexts().length).toBe(1);
    expect(helptexts()[0].textContent).toBe("Model help");
  });

  it("explicit label/helpText win over the model", () => {
    render(<TextField fieldPath="name" label="Short" helpText="Short help" />);
    expect(container.querySelector("label").textContent).toContain("Short");
    expect(helptexts()[0].textContent).toBe("Short help");
  });

  it("TextField with neither model nor prop help renders no helptext", () => {
    render(<TextField fieldPath="name" helpText={null} />);
    expect(helptexts().length).toBe(0);
  });

  it("SelectField selects an option and shows model help once", () => {
    // Note: options arrive already as Semantic option objects; string
    // expansion happens one layer up (the SelectField building block).
    render(
      <SelectField
        fieldPath="kind"
        options={[
          { key: "a", value: "a", text: "a" },
          { key: "b", value: "b", text: "b" },
        ]}
      />
    );
    const item = [...container.querySelectorAll(".menu .item")].find(
      (el) => el.textContent.trim() === "b"
    );
    act(() => {
      Simulate.click(item);
    });
    expect(container.querySelector(".dropdown .text").textContent).toContain(
      "b"
    );
    expect(helptexts().length).toBe(1);
  });

  it("ArrayField renders children per item and adds a row via its button", () => {
    render(
      <ArrayField fieldPath="items" label="Items">
        {({ arrayPath, indexPath }) => (
          <TextField fieldPath={`${arrayPath}.${indexPath}.name`} />
        )}
      </ArrayField>,
      { initialValues: { items: [{ name: "first" }] } }
    );
    expect(container.querySelectorAll("input").length).toBe(1);
    const add = [...container.querySelectorAll("button")].find((b) =>
      b.textContent.includes("Add new row")
    );
    act(() => {
      Simulate.click(add);
    });
    expect(container.querySelectorAll("input").length).toBe(2);
  });

  it("TextAreaField renders value, label and help", () => {
    render(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL" },
    });
    expect(container.querySelector("textarea").value).toBe("MKAL");
    expect(container.querySelector("label").textContent).toContain(
      "Model label"
    );
    expect(helptexts().length).toBe(1);
  });
});
