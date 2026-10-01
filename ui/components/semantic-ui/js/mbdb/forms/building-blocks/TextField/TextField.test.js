import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { TextField, NumberField, TextAreaField, autoRows } from "./TextField";

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
    render(<TextField fieldPath="name" label="Name" help="A unique name" />, {
      initialValues: { name: "Lysozyme" },
    });
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

  it("removes the key when cleared", () => {
    render(
      <>
        <TextField fieldPath="name" />
        <Probe path="name" />
      </>,
      { initialValues: { name: "Lysozyme" } }
    );
    change(container.querySelector("input"), "");
    expect(byTestId("value").textContent).toBe("-");
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

  it("stores integers without truncation and drops unparseable input", () => {
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
    // would sanitize it in the DOM); the key is removed instead of
    // keeping a raw string.
    act(() => {
      Simulate.change(input, { target: { value: "abc" } });
    });
    expect(byTestId("value").textContent).toBe("-");
  });

  it("defaults step to 1 for integers", () => {
    render(<NumberField fieldPath="num" integer />);
    expect(container.querySelector("input").getAttribute("step")).toBe("1");
  });

  it("shows the error from initialErrors", () => {
    render(<NumberField fieldPath="num" />, {
      initialValues: { num: 5 },
      initialErrors: { num: "Not a valid number." },
    });
    expect(container.textContent).toContain("Not a valid number.");
  });
});

describe("autoRows", () => {
  it("is 3 for short text, grows with length and line breaks, caps at 12", () => {
    expect(autoRows("")).toBe(3);
    expect(autoRows(undefined)).toBe(3);
    expect(autoRows("short")).toBe(3);
    // 400 chars without breaks: 400 / 80 = 5 rows
    expect(autoRows("x".repeat(400))).toBe(5);
    // 5 broken lines: 1 (length) + 4 (breaks)
    expect(autoRows("a\nb\nc\nd\ne")).toBe(5);
    // long text never exceeds the cap
    expect(autoRows("line\n".repeat(20))).toBe(12);
  });
});

describe("TextAreaField", () => {
  it("renders value, monospace class and link buttons", () => {
    render(
      <TextAreaField
        fieldPath="seq"
        label="Sequence"
        monospace
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

  it("autoHeight sizes rows to the content and stays off the DOM", () => {
    render(<TextAreaField fieldPath="seq" autoHeight />, {
      initialValues: { seq: "line\n".repeat(20) },
    });
    const textarea = container.querySelector("textarea");
    expect(Number(textarea.getAttribute("rows"))).toBeLessThanOrEqual(12);
    expect(textarea.getAttribute("autoheight")).toBeNull();
  });

  it("removes the key when cleared", () => {
    render(
      <>
        <TextAreaField fieldPath="seq" />
        <Probe path="seq" />
      </>,
      { initialValues: { seq: "MKAL" } }
    );
    change(container.querySelector("textarea"), "");
    expect(byTestId("value").textContent).toBe("-");
  });

  it("shows the error from initialErrors", () => {
    render(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL" },
      initialErrors: { seq: "Not a valid sequence." },
    });
    expect(container.textContent).toContain("Not a valid sequence.");
  });
});
