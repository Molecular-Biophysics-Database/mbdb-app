import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { Field } from "formik";
import { DiscriminatorField } from "./DiscriminatorField";
import {
  renderInForm,
  unmountForm,
  ValueProbe,
  readProbe,
  setFakeUiModel,
} from "@js/mbdb/forms/building-blocks/testUtils";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

let container;

// The confirm headers assert the raw field path ("Change o.type to …"), the
// old hand-rolled fake returned `label: fieldPath`. Pin that label so the
// assertions stay exact now the fake falls back to a readable leaf label.
beforeEach(() => {
  setFakeUiModel({ "o.type": { label: "o.type" } });
});

const mount = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

const probe = () => readProbe(container);
const modal = () => document.body.querySelector(".ui.modal");
const button = (label) =>
  [...container.querySelectorAll("button")].find(
    (b) => b.textContent === label
  );
const ENTITY_TYPES = [
  "Polymer",
  "Chemical",
  "Molecular assembly",
  "Complex substance of biological origin",
  "Other",
];

// 5 entity types default to the dropdown variant; buttons tested explicitly
const typeField = (props = {}) => (
  <>
    <DiscriminatorField
      objectPath="o"
      field="type"
      options={ENTITY_TYPES}
      variant="buttons"
      keep={["id"]}
      {...props}
    />
    <ValueProbe path="o" />
  </>
);

describe("DiscriminatorField", () => {
  it("buttons variant: marks the current option primary and changes without confirm when no other data", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
    });
    expect(button("Polymer").className).toContain("primary");
    expect(button("Chemical").className).not.toContain("primary");

    act(() => Simulate.click(button("Chemical")));
    expect(probe()).toEqual({ id: "e1", type: "Chemical" });
    expect(modal()).toBeNull(); // nothing lost, no confirm asked
  });

  it("popup mode: no helptext label, one help icon next to the label", () => {
    mount(typeField({ label: "Entity type", help: "The kind of entity" }), {
      helpMode: "popup",
    });
    expect(container.querySelector("label.helptext")).toBeNull();
    expect(container.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("exposes pressed state and arrow-key focus on the option buttons", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
    });
    const group = container.querySelector('[role="group"]');
    expect(group).not.toBeNull();
    expect(button("Polymer").getAttribute("aria-pressed")).toBe("true");
    expect(button("Chemical").getAttribute("aria-pressed")).toBe("false");

    button("Polymer").focus();
    act(() => {
      Simulate.keyDown(group, { key: "ArrowRight" });
    });
    expect(document.activeElement).toBe(button("Chemical"));
  });

  it("does nothing when the current option is clicked again", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
    });
    act(() => Simulate.click(button("Polymer")));
    expect(probe()).toEqual({ id: "e1", type: "Polymer" });
    expect(modal()).toBeNull();
  });

  it("asks before changing when other data would be lost, and keeps only keep keys", () => {
    mount(typeField(), {
      initialValues: {
        o: { id: "e1", type: "Polymer", name: "Lysozyme", sequence: "ABC" },
      },
    });
    act(() => Simulate.click(button("Chemical")));
    const m = modal();
    expect(m).not.toBeNull();
    expect(m.textContent).toContain('Change o.type to "Chemical"?');
    expect(m.textContent).toContain(
      'The data entered for "Polymer" will be removed.'
    );
    expect(probe()).toEqual({
      id: "e1",
      type: "Polymer",
      name: "Lysozyme",
      sequence: "ABC",
    });

    const changeBtn = [...m.querySelectorAll("button")].find(
      (b) => b.textContent === "Change"
    );
    act(() => Simulate.click(changeBtn));
    expect(probe()).toEqual({ id: "e1", type: "Chemical" });
  });

  it("confirm copy does not promise deletion when keep preserves fields above the discriminator", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="c"
          field="type"
          options={["Polymer", "Chemical"]}
          variant="buttons"
          keep={["name", "copy_number"]}
        />
        <ValueProbe path="c" />
      </>,
      {
        initialValues: {
          c: {
            name: "RNA polymerase",
            copy_number: 2,
            polymer_type: "polypeptide(L)",
          },
        },
      }
    );
    act(() => Simulate.click(button("Chemical")));
    const m = modal();
    expect(m.textContent).toContain("The type-specific data will be removed.");
    expect(m.textContent).not.toContain("The data entered for");

    const changeBtn = [...m.querySelectorAll("button")].find(
      (b) => b.textContent === "Change"
    );
    act(() => Simulate.click(changeBtn));
    // name and copy_number survive; only the type-specific data is dropped
    expect(probe()).toEqual({
      name: "RNA polymerase",
      copy_number: 2,
      type: "Chemical",
    });
  });

  it("seed writes keep keys + the new value + the seed in one change", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="type"
          options={["Polymer", "Chemical origin"]}
          variant="buttons"
          keep={["id", "name"]}
          seed={(t) =>
            t === "Chemical origin" ? { class: "Lipid assembly" } : undefined
          }
        />
        <ValueProbe path="o" />
      </>,
      { initialValues: { o: { id: "e1", name: "SigA", type: "Polymer" } } }
    );
    act(() => Simulate.click(button("Chemical origin")));
    expect(probe()).toEqual({
      id: "e1",
      name: "SigA",
      type: "Chemical origin",
      class: "Lipid assembly",
    });
  });

  it("a seed value wins over a keep key of the same name (seed applied last)", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="class"
          options={["Lipid assembly", "Other class"]}
          variant="buttons"
          keep={["id", "name", "class"]}
          seed={() => ({ class: "seeded" })}
        />
        <ValueProbe path="o" />
      </>,
      {
        initialValues: { o: { id: "e1", name: "X", class: "Lipid assembly" } },
      }
    );
    act(() => Simulate.click(button("Other class")));
    expect(probe()).toEqual({ id: "e1", name: "X", class: "seeded" });
  });

  it("cancel of the confirm leaves the object untouched", () => {
    mount(typeField(), {
      initialValues: { o: { type: "Polymer", name: "Lysozyme" } },
    });
    act(() => Simulate.click(button("Chemical")));
    const cancelBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Cancel"
    );
    act(() => Simulate.click(cancelBtn));
    expect(probe()).toEqual({ type: "Polymer", name: "Lysozyme" });
  });

  it("dropping extra keys beyond keep also guarded: id kept, others dropped", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer", name: "X" } },
    });
    act(() => Simulate.click(button("Other")));
    const changeBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Change"
    );
    act(() => Simulate.click(changeBtn));
    expect(probe()).toEqual({ id: "e1", type: "Other" });
  });

  it("confirm header and body show option labels, not raw values", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="type"
          options={[
            { value: "polymer", label: "Polymer" },
            { value: "chemical", label: "Chemical" },
          ]}
          variant="buttons"
        />
        <ValueProbe path="o" />
      </>,
      {
        initialValues: { o: { type: "polymer", name: "Lysozyme" } },
      }
    );
    act(() => Simulate.click(button("Chemical")));
    const m = modal();
    expect(m.textContent).toContain('Change o.type to "Chemical"?');
    expect(m.textContent).toContain(
      'The data entered for "Polymer" will be removed.'
    );
  });

  it("allowUnset adds an unset button that clears the whole object", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="assessed"
          options={["Yes", "No"]}
          allowUnset
          unsetLabel="Not specified"
        />
        <ValueProbe path="o" />
      </>,
      { initialValues: { o: { assessed: "Yes", method: "SDS-PAGE" } } }
    );
    expect(button("Yes").className).toContain("primary");
    act(() => Simulate.click(button("Not specified")));
    expect(modal()).not.toBeNull(); // data present: confirm first
    const removeBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Remove"
    );
    act(() => Simulate.click(removeBtn));
    expect(probe()).toEqual(null);
  });

  it("unset is active when the object is absent", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="assessed"
          options={["Yes", "No"]}
          allowUnset
          unsetLabel="Not specified"
        />
        <ValueProbe path="o" />
      </>,
      { initialValues: {} }
    );
    expect(button("Not specified").className).toContain("primary");
    expect(button("Yes").className).not.toContain("primary");
    // choosing Yes from unset: no data to lose → no confirm
    act(() => Simulate.click(button("Yes")));
    expect(probe()).toEqual({ assessed: "Yes" });
    expect(modal()).toBeNull();
  });

  it("unset is not active for an object without the field, and removes it after confirm", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="assessed"
          options={["Yes", "No"]}
          allowUnset
          unsetLabel="Not specified"
        />
        <ValueProbe path="o" />
      </>,
      // object exists with data, but `assessed` was never set
      { initialValues: { o: { method: "SDS-PAGE" } } }
    );
    expect(button("Not specified").className).not.toContain("primary");
    expect(button("Yes").className).not.toContain("primary");
    act(() => Simulate.click(button("Not specified")));
    expect(modal()).not.toBeNull(); // data would be lost: confirm first
    const removeBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Remove"
    );
    act(() => Simulate.click(removeBtn));
    expect(probe()).toEqual(null);
  });

  it("dropdown variant renders a plain dropdown and changes value", () => {
    mount(
      typeField({ variant: "dropdown", options: ["Polymer", "Chemical"] }),
      {
        initialValues: { o: { id: "e1", type: "Polymer" } },
      }
    );
    const dropdown = container.querySelector(".ui.dropdown");
    expect(dropdown).not.toBeNull();
    // no nested .field inside the block's Form.Field
    expect(dropdown.closest(".field").querySelector(".field")).toBeNull();
    act(() => Simulate.click(dropdown));
    const item = [...dropdown.querySelectorAll(".menu .item")].find(
      (el) => el.textContent === "Chemical"
    );
    act(() => Simulate.click(item));
    expect(probe()).toEqual({ id: "e1", type: "Chemical" });
  });

  it("shows discriminator and object-path errors from initialErrors", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
      initialErrors: { o: { type: "Not a valid type." } },
    });
    expect(container.textContent).toContain("Not a valid type.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it("shows a string error at the object path", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
      initialErrors: { o: "Missing data for required field." },
    });
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });

  it('does not show a { severity: "warning" } node as an error', () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
      initialErrors: {
        o: { type: { message: "Odd type.", severity: "warning" } },
      },
    });
    expect(container.querySelector(".field.error")).toBeNull();
    expect(container.textContent).not.toContain("Odd type.");
  });

  it("keeps an initialError visible after another field is edited", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="type"
          options={["Polymer", "Chemical"]}
        />
        <ValueProbe path="o" />
        <Field data-testid="other" name="other" />
      </>,
      {
        initialValues: { o: { id: "e1", type: "Polymer" } },
        initialErrors: { o: { type: "Not a valid type." } },
      }
    );
    expect(container.textContent).toContain("Not a valid type.");
    // Validation on the first edit resets `errors` to {}; the server
    // error must still be shown.
    const other = container.querySelector('[data-testid="other"]');
    other.value = "x";
    act(() => {
      Simulate.change(other);
    });
    expect(container.textContent).toContain("Not a valid type.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });
});
