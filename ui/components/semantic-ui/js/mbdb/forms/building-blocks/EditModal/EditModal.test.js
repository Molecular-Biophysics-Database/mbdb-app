import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { EditModal } from "./EditModal";

let container;

afterEach(() => {
  if (!container) return;
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
  container = null;
  document
    .querySelectorAll(".ui.modals, .ui.dimmer")
    .forEach((el) => el.remove());
});

const modal = () => document.body.querySelector(".ui.modal");
const dimmer = () => document.body.querySelector(".ui.dimmer");
const modalButton = (label) =>
  [...modal().querySelectorAll("button")].find((b) => b.textContent === label);

const mount = (ui) => {
  container = document.createElement("div");
  document.body.appendChild(container);
  act(() => {
    ReactDOM.render(ui, container);
  });
};

describe("EditModal", () => {
  it("depth 1: no breadcrumb line, plain Cancel / Done, and the modal is large (Y14)", () => {
    mount(
      <EditModal
        header="Edit something"
        open
        onCancel={() => {}}
        onDone={() => {}}
      >
        <p>modal body</p>
      </EditModal>
    );
    expect(modal().querySelector(".mbdb-modal-trail")).toBeNull();
    expect(modalButton("Done").textContent).toBe("Done");
    expect(modal().className).toContain("large");
  });

  it("depth 2: shows the parent crumb, names the destination on Done, and is one size smaller (Y14)", () => {
    mount(
      <EditModal
        header="Edit entity"
        crumb={{
          label: "human Hemoglobin (Molecular assembly)",
          noun: "assembly",
        }}
        open
        onCancel={() => {}}
        onDone={() => {}}
      >
        <EditModal
          header="Edit Hemoglobin subunit alpha"
          crumb={{ label: "Hemoglobin subunit alpha", noun: "component" }}
          open
          onCancel={() => {}}
          onDone={() => {}}
        >
          inner body
        </EditModal>
      </EditModal>
    );
    // portals stack in creation order: [outer, inner]
    const all = [...document.body.querySelectorAll(".ui.modal")];
    expect(all).toHaveLength(2);
    const inner = all.find((m) =>
      m.textContent.includes("Edit Hemoglobin subunit alpha")
    );
    expect(inner).toBeDefined();
    const trail = inner.querySelector(".mbdb-modal-trail");
    expect(trail).not.toBeNull();
    expect(trail.textContent).toBe("human Hemoglobin (Molecular assembly) ›");
    // the crumb is text, not a link or button
    expect(trail.querySelector("a, button")).toBeNull();
    // the destination on the nested Done (option B2)
    const done = [...inner.querySelectorAll("button")].find((b) =>
      b.textContent.startsWith("Done")
    );
    expect(done.textContent).toBe("Done, back to assembly");
    // one size smaller than the entity modal (no `large`)
    expect(inner.className).not.toContain("large");
    const outer = all.find((m) => m.textContent.includes("Edit entity"));
    expect(outer.querySelector(".mbdb-modal-trail")).toBeNull();
    expect(outer.className).toContain("large");
  });

  it("renders header/content and fires Cancel and Done", () => {
    const calls = [];
    mount(
      <EditModal
        header="Edit something"
        open
        onCancel={() => calls.push("cancel")}
        onDone={() => calls.push("done")}
      >
        <p>modal body</p>
      </EditModal>
    );
    expect(modal()).not.toBeNull();
    expect(modal().textContent).toContain("Edit something");
    expect(modal().textContent).toContain("modal body");
    const cancel = modalButton("Cancel");
    const done = modalButton("Done");
    expect(cancel.type).toBe("button");
    expect(done.type).toBe("button");
    act(() => Simulate.click(done));
    act(() => Simulate.click(cancel));
    expect(calls).toEqual(["done", "cancel"]);
  });

  it("the content has a .ui.form ancestor that is a div, not a form element", () => {
    mount(
      <EditModal
        header="Edit something"
        open
        onCancel={() => {}}
        onDone={() => {}}
      >
        <input readOnly />
      </EditModal>
    );
    const input = modal().querySelector("input");
    const form = input.closest(".ui.form");
    // Semantic form CSS (labels, Form.Group columns, required asterisks,
    // textareas) needs a `.ui.form` ancestor — a Modal is a portal, so
    // nothing else provides one.
    expect(form).not.toBeNull();
    expect(form.tagName).not.toBe("FORM");
    expect(modal().contains(form)).toBe(true);
  });

  it("a dimmer click fires NEITHER callback (closeOnDimmerClick is false)", () => {
    const calls = [];
    mount(
      <EditModal
        header="Edit something"
        open
        onCancel={() => calls.push("cancel")}
        onDone={() => calls.push("done")}
      >
        <p>modal body</p>
      </EditModal>
    );
    expect(dimmer()).not.toBeNull();
    act(() => Simulate.click(dimmer()));
    // a stray dimmer click must not discard edits: the modal stays open and
    // neither Cancel nor Done fires
    expect(calls).toEqual([]);
    expect(modal()).not.toBeNull();
  });

  // Escape → onCancel: the repo's jest breaks on Simulate.keyDown(document)
  // (_jestGetType quirk when an assertion runs). Dispatching a real
  // KeyboardEvent on document reaches Semantic's document keydown listener;
  // best-effort: if the environment cannot deliver it, the production mapping
  // (Modal onClose → onCancel) is unchanged and untested here.
  it("Escape maps to Cancel, not a silent discard", () => {
    const calls = [];
    mount(
      <EditModal
        header="Edit something"
        open
        onCancel={() => calls.push("cancel")}
        onDone={() => calls.push("done")}
      >
        <p>modal body</p>
      </EditModal>
    );
    act(() => {
      document.dispatchEvent(
        new KeyboardEvent("keydown", { key: "Escape", bubbles: true })
      );
    });
    // Semantic calls onClose on Escape; our onClose IS onCancel
    expect(calls).toEqual(["cancel"]);
  });
});
