import React from "react";

import { Form } from "mbdb-semantic-ui-react";
import { FieldShell } from "./FieldShell";
import {
  renderInForm,
  unmountForm,
} from "@js/mbdb/forms/building-blocks/testUtils";

// The shell owns structure only; it reads no model data itself, so the
// shared harness suffices without setFakeUiModel overrides. The same
// useModelFieldData mock family the sibling tests use backs the harness.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

let container;

afterEach(() => {
  unmountForm(container);
  container = null;
});

const render = (ui, opts) => {
  container = renderInForm(ui, opts);
};

const field = () => container.querySelector(".field");

// The four slots, in the shell's fixed order: wrapping label, control,
// error label (the prompt .label), helptext.
const slotOrder = () =>
  [...field().children].map((el) =>
    el.classList.contains("label")
      ? "error"
      : el.classList.contains("helptext")
      ? "help"
      : el.tagName === "LABEL"
      ? "label"
      : "control"
  );

describe("FieldShell", () => {
  it("orders label, control, error label, helptext inside one root .field", () => {
    render(
      <FieldShell
        inputId="seq"
        label="Sequence"
        help="One-letter codes"
        messages={["Not a valid sequence."]}
      >
        <textarea id="seq" readOnly />
      </FieldShell>
    );
    expect(container.querySelectorAll(".field").length).toBe(1);
    expect(slotOrder()).toEqual(["label", "control", "error", "help"]);
    expect(field().querySelector('label[for="seq"]')).not.toBeNull();
    expect(field().querySelector('label[for="seq"]').textContent).toContain(
      "Sequence"
    );
    expect(field().querySelector(".label").textContent).toBe(
      "Not a valid sequence."
    );
    expect(field().querySelector("label.helptext").textContent).toBe(
      "One-letter codes"
    );
  });

  it("two shells in a Form.Group become exactly two columns, each holding its own help (D8)", () => {
    render(
      <Form.Group widths="equal">
        <FieldShell inputId="a" label="A" help="Help A">
          <input id="a" readOnly />
        </FieldShell>
        <FieldShell inputId="b" label="B" help="Help B">
          <input id="b" readOnly />
        </FieldShell>
      </Form.Group>
    );
    const group = container.querySelector(".fields");
    expect(group).not.toBeNull();
    const columns = [...group.children];
    expect(columns.length).toBe(2);
    columns.forEach((column, i) => {
      expect(column.className).toContain("field");
      const helps = column.querySelectorAll("label.helptext");
      expect(helps.length).toBe(1);
      expect(helps[0].textContent).toBe(["Help A", "Help B"][i]);
    });
  });

  it('messages ["a", "b"] mark the field error and join into one label reading "a b"', () => {
    render(
      <FieldShell label="Name" messages={["a", "b"]}>
        <input readOnly />
      </FieldShell>
    );
    expect(field().className).toContain("error");
    const errorLabels = field().querySelectorAll(".prompt.label");
    expect(errorLabels.length).toBe(1);
    expect(errorLabels[0].textContent).toBe("a b");
  });

  it("width={8} renders as an eight wide field", () => {
    render(
      <FieldShell label="Name" width={8}>
        <input readOnly />
      </FieldShell>
    );
    expect(field().className).toContain("eight wide field");
  });

  it('className="mbdb-monospace" lands on the .field and its LESS rule would match the child textarea', () => {
    render(
      <FieldShell label="Sequence" className="mbdb-monospace">
        <textarea readOnly />
      </FieldShell>
    );
    // the rule is .mbdb-monospace textarea (Sequence-review P2-F1): the
    // class must sit on the shell's root, never on the textarea itself
    expect(field().className).toContain("mbdb-monospace");
    expect(field().querySelector("textarea")).not.toBeNull();
    expect(field().querySelector("textarea").className).not.toContain(
      "mbdb-monospace"
    );
  });

  it("popup help mode: no label.helptext under the control, one ? icon inside the label", () => {
    render(
      <FieldShell inputId="seq" label="Sequence" help="One-letter codes">
        <textarea id="seq" readOnly />
      </FieldShell>,
      { helpMode: "popup" }
    );
    expect(container.querySelectorAll("label.helptext").length).toBe(0);
    const labelEl = container.querySelector('label[for="seq"]');
    expect(labelEl).not.toBeNull();
    expect(labelEl.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("without inputId the label still renders as a <label> (Semantic's styles apply)", () => {
    render(
      <FieldShell label={<span data-testid="own">Own label</span>} help="h">
        <input readOnly />
      </FieldShell>
    );
    const own = container.querySelector('[data-testid="own"]');
    expect(own).not.toBeNull();
    // FieldLabel without inputId wraps a plain <label> (valid HTML;
    // Semantic's `.field .label` styling + required markers need the element)
    expect(own.closest("label")).not.toBeNull();
  });

  it("no label and no help renders control only (errors still possible)", () => {
    render(
      <FieldShell messages={["Required."]}>
        <input readOnly />
      </FieldShell>
    );
    expect(slotOrder()).toEqual(["control", "error"]);
  });
});
