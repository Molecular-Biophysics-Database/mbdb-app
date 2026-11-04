import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { TextField, NumberField, TextAreaField, autoRows } from "./TextField";
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

// The shared fake returns leaf labels for un-registered paths, but labels in
// these tests come from explicit props.
let container;

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

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
        <ValueProbe path="name" />
      </>,
      { initialValues: { name: "Lysozyme" } }
    );
    change(container.querySelector("input"), "");
    expect(readProbe(container)).toBeNull();
  });
});

describe("NumberField", () => {
  it("stores numbers, not strings, and clears to undefined", () => {
    render(
      <>
        <NumberField fieldPath="num" />
        <ValueProbe path="num" />
      </>
    );
    const input = container.querySelector("input");
    change(input, "12.5");
    expect(readProbe(container)).toBe(12.5);
    expect(typeof readProbe(container)).toBe("number");

    change(input, "");
    expect(readProbe(container)).toBeNull();
  });

  it("stores integers without truncation and drops unparseable input", () => {
    render(
      <>
        <NumberField fieldPath="num" integer />
        <ValueProbe path="num" />
      </>
    );
    const input = container.querySelector("input");
    change(input, "7");
    expect(readProbe(container)).toBe(7);
    expect(typeof readProbe(container)).toBe("number");

    // Simulate an event with input that is not a number (a number input
    // would sanitize it in the DOM); the key is removed instead of
    // keeping a raw string.
    act(() => {
      Simulate.change(input, { target: { value: "abc" } });
    });
    expect(readProbe(container)).toBeNull();
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
    // the class lands on the Form.Field so `.mbdb-monospace textarea` matches
    expect(container.querySelector(".mbdb-monospace textarea")).not.toBeNull();
    const links = [...container.querySelectorAll("a.button")];
    expect(links.map((a) => a.textContent.trim())).toEqual([
      "UniProt",
      "BLAST",
    ]);
    expect(links[0].getAttribute("href")).toBe("https://www.uniprot.org");
    expect(links[0].getAttribute("target")).toBe("_blank");
    expect(links[0].getAttribute("rel")).toBe("noreferrer");
    // anchors have no type="button" (ExternalLink)
    expect(links[0].getAttribute("type")).toBeNull();
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
        <ValueProbe path="seq" />
      </>,
      { initialValues: { seq: "MKAL" } }
    );
    change(container.querySelector("textarea"), "");
    expect(readProbe(container)).toBeNull();
  });

  it("shows the error from initialErrors", () => {
    render(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL" },
      initialErrors: { seq: "Not a valid sequence." },
    });
    expect(container.textContent).toContain("Not a valid sequence.");
  });
});
