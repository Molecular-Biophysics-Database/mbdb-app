import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { TextField, NumberField, TextAreaField } from "./TextField";

// The real "@js/oarepo_ui/forms" index cannot load under Jest
// (sanitize-html -> postcss is ESM); the model data hook is mocked so
// labels in these tests come from explicit props.
jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: () => ({
      label: undefined,
      helpText: undefined,
      required: undefined,
    }),
  }),
}));

// The alias index.js does not export FieldHelp yet; simulate the state
// after that one-line export is added.
jest.mock("mbdb-semantic-ui-react", () => ({
  ...jest.requireActual("mbdb-semantic-ui-react"),
  ...jest.requireActual("mbdb-semantic-ui-react/FieldHelp"),
}));

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const v = getIn(values, path);
  return (
    <div>
      <span data-testid="value">{v === undefined ? "-" : String(v)}</span>
      <span data-testid="type">{typeof v}</span>
    </div>
  );
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
const change = (input, value) => {
  input.value = value;
  act(() => {
    Simulate.change(input);
  });
};

describe("TextField", () => {
  it("renders value, explicit label and help text", () => {
    render(
      <TextField fieldPath="name" label="Name" helpText="A unique name" />,
      { initialValues: { name: "Lysozyme" } }
    );
    expect(container.querySelector("input").value).toBe("Lysozyme");
    expect(container.querySelector("label").textContent).toBe("Name");
    expect(container.querySelector("label.helptext").textContent).toBe(
      "A unique name"
    );
    // exactly one helptext (RIF native rendering is suppressed)
    expect(container.querySelectorAll("label.helptext").length).toBe(1);
  });

  it("shows the error from initialErrors", () => {
    render(<TextField fieldPath="name" />, {
      initialValues: { name: "" },
      initialErrors: { name: "Missing data for required field." },
    });
    expect(container.textContent).toContain("Missing data for required field.");
  });
});

describe("NumberField", () => {
  it("stores numbers, not strings, and clears to undefined", () => {
    render(
      <>
        <NumberField fieldPath="num" />
        <Probe path="num" />
      </>
    );
    const input = container.querySelector("input");
    change(input, "12.5");
    expect(byTestId("value").textContent).toBe("12.5");
    expect(byTestId("type").textContent).toBe("number");

    change(input, "");
    expect(byTestId("value").textContent).toBe("-");
  });

  it("parses integers and keeps unparseable input as a raw string", () => {
    render(
      <>
        <NumberField fieldPath="num" integer />
        <Probe path="num" />
      </>
    );
    const input = container.querySelector("input");
    change(input, "7");
    expect(byTestId("value").textContent).toBe("7");
    expect(byTestId("type").textContent).toBe("number");

    // Simulate an event with input that is not a number (a number input
    // would sanitize it in the DOM); the raw string is kept for the
    // server to report.
    act(() => {
      Simulate.change(input, { target: { value: "abc" } });
    });
    expect(byTestId("value").textContent).toBe("abc");
    expect(byTestId("type").textContent).toBe("string");
  });
});

describe("TextAreaField", () => {
  it("renders value, monospace class and link buttons", () => {
    render(
      <TextAreaField
        fieldPath="seq"
        label="Sequence"
        monospace
        autoHeight
        links={[
          { label: "UniProt", href: "https://www.uniprot.org" },
          { label: "BLAST", href: "https://blast.ncbi.nlm.nih.gov" },
        ]}
      />,
      { initialValues: { seq: "MKALIVLG" } }
    );
    expect(container.querySelector("textarea").value).toBe("MKALIVLG");
    expect(container.querySelector(".mbdb-monospace")).not.toBeNull();
    const links = [...container.querySelectorAll("a.button")];
    expect(links.map((a) => a.textContent)).toEqual(["UniProt", "BLAST"]);
    expect(links[0].getAttribute("href")).toBe("https://www.uniprot.org");
    expect(links[0].getAttribute("target")).toBe("_blank");
    expect(links[0].getAttribute("type")).toBe("button");
  });
});
