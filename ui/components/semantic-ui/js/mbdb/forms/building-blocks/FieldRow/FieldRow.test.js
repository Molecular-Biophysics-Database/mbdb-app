import React from "react";
import { FieldRow } from "./FieldRow";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import {
  renderInForm,
  unmountForm,
} from "@js/mbdb/forms/building-blocks/testUtils";

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

const field = () => container.querySelector(".field");
const help = () => field().querySelector("label.helptext");
const buttonRow = () => field().querySelector('[role="group"]');

const button = (props = {}) =>
  renderInForm(
    <ButtonGroupField
      fieldPath="a"
      label="A"
      help="Help A"
      options={["x", "y"]}
      {...props}
    />
  );

describe("FieldRow", () => {
  it("renders a Form.Group (Semantic .fields) holding its children", () => {
    container = renderInForm(
      <FieldRow widths="equal">
        <ButtonGroupField
          fieldPath="a"
          label="A"
          help="HA"
          options={["x", "y"]}
        />
        <ButtonGroupField
          fieldPath="b"
          label="B"
          help="HB"
          options={["x", "y"]}
        />
      </FieldRow>
    );
    const group = container.querySelector(".fields");
    expect(group).not.toBeNull();
    expect(group.children.length).toBe(2);
    expect(group.children[0].className).toContain("field");
  });

  it("a button group in a row puts its help under the control, not under the label", () => {
    container = renderInForm(
      <FieldRow>
        <ButtonGroupField
          fieldPath="a"
          label="A"
          help="Help A"
          options={["x", "y"]}
        />
      </FieldRow>
    );
    const labelEl = field().querySelector("label");
    const h = help();
    expect(h).not.toBeNull();
    // the row moves it: NOT the label's next sibling...
    expect(labelEl.nextElementSibling).not.toBe(h);
    // ...it follows the control, and drops the under-label class
    expect(buttonRow().nextElementSibling).toBe(h);
    expect(h.classList.contains("mbdb-field-help-under-label")).toBe(false);
  });

  it("the same button group outside a row keeps its help under the label", () => {
    container = button();
    const labelEl = field().querySelector("label");
    expect(labelEl.nextElementSibling).toBe(help());
    expect(help().classList.contains("mbdb-field-help-under-label")).toBe(true);
  });

  it("a discriminator button row in a row also puts its help under the control", () => {
    container = renderInForm(
      <FieldRow>
        <DiscriminatorField
          objectPath="o"
          field="assessed"
          options={["Yes", "No"]}
          label="Assessed"
          help="Help"
        />
      </FieldRow>
    );
    const labelEl = field().querySelector("label");
    const h = help();
    expect(labelEl.nextElementSibling).not.toBe(h);
    expect(buttonRow().nextElementSibling).toBe(h);
  });
});
