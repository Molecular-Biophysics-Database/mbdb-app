import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { Field } from "formik";
import { FieldGroup } from "./FieldGroup";
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

// FieldGroup resolves title/help/required from the model when fieldPath is
// set; these tests pass explicit title/help everywhere, so explicit props win
// and no setFakeUiModel entries are needed.
let container;

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

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

  it("popup mode: no helptext under the header, one help icon in the header", () => {
    render(
      <FieldGroup
        title="Molecular weight"
        help="The molecular weight of the polymer"
        fieldPath="metadata.mw"
      >
        <input data-testid="child" />
      </FieldGroup>,
      { helpMode: "popup" }
    );
    expect(container.querySelector("label.helptext")).toBeNull();
    const icons = container.querySelectorAll('[aria-label^="Help"]');
    expect(icons.length).toBe(1);
    expect(container.querySelector("h5.ui.header").contains(icons[0])).toBe(
      true
    );
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

  it("stays red when another field is edited (initialErrors survive)", () => {
    render(
      <>
        <FieldGroup title="Mw" fieldPath="metadata.mw">
          fields
        </FieldGroup>
        <Field data-testid="other" name="other" />
      </>,
      {
        initialErrors: { metadata: { mw: "Required" } },
      }
    );
    expect(container.querySelector("h5.ui.header.red")).not.toBeNull();
    // Editing any field runs validation and Formik (no validation schema)
    // resets `errors` to {}; the header must not lose its red state.
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    act(() => {
      Simulate.change(other);
    });
    expect(container.querySelector("h5.ui.header.red")).not.toBeNull();
  });

  it("shows the group-path message under the header, surviving an unrelated edit", async () => {
    // a required group that the server flags shows its message, not
    // only a red header (Location-review F1).
    render(
      <>
        <FieldGroup title="Location" fieldPath="metadata.location">
          fields
        </FieldGroup>
        <Field data-testid="other" name="other" />
      </>,
      {
        initialErrors: {
          metadata: { location: "Missing data for required field." },
        },
      }
    );
    expect(container.textContent).toContain("Missing data for required field.");
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    await act(async () => {
      Simulate.change(other);
      await new Promise((r) => setTimeout(r, 0));
    });
    expect(container.textContent).toContain("Missing data for required field.");
  });

  it("renders actions straight after the header", () => {
    render(
      <FieldGroup title="Mw" actions={<button type="button">Clear</button>}>
        fields
      </FieldGroup>
    );
    const header = container.querySelector("h5.ui.header");
    // h5 stays a clean heading (no interactive child); the action follows it
    expect(header.querySelector("button")).toBeNull();
    expect(header.nextElementSibling.textContent).toBe("Clear");
  });

  it('does not mark the header red for a { severity: "warning" } node', () => {
    render(
      <FieldGroup title="Mw" fieldPath="metadata.mw">
        fields
      </FieldGroup>,
      {
        initialErrors: {
          metadata: { mw: { message: "Watch it.", severity: "warning" } },
        },
      }
    );
    expect(container.querySelector("h5.ui.header.red")).toBeNull();
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

  it("wraps children in a basic Segment when nested", () => {
    render(
      <FieldGroup title="Mw" nested>
        <input data-testid="child" />
      </FieldGroup>
    );
    const segment = container.querySelector(".ui.segment.basic.mbdb-nested");
    expect(segment).not.toBeNull();
    expect(segment.querySelector('[data-testid="child"]')).not.toBeNull();
  });

  it("renders a divider above the group when divided", () => {
    render(
      <FieldGroup title="Mw" divided>
        fields
      </FieldGroup>
    );
    const divider = container.querySelector(".ui.divider");
    expect(divider).not.toBeNull();
    expect(divider.nextElementSibling.tagName).toBe("H5");
  });

  it("shows the required asterisk in the header", () => {
    render(<FieldGroup title="Mw" required fieldPath="metadata.mw" />);
    const header = container.querySelector("h5.ui.header");
    expect(header.textContent).toBe("Mw*");
    expect(header.querySelector("span.mbdb-required").textContent).toBe("*");
  });
});
