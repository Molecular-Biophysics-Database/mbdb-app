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
