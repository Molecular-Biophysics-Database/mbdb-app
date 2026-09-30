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
const modalButton = (label) =>
  [...modal().querySelectorAll("button")].find((b) => b.textContent === label);

describe("EditModal", () => {
  it("renders header/content and fires Cancel and Done", () => {
    const calls = [];
    container = document.createElement("div");
    document.body.appendChild(container);
    act(() => {
      ReactDOM.render(
        <EditModal
          header="Edit something"
          open
          onCancel={() => calls.push("cancel")}
          onDone={() => calls.push("done")}
        >
          <p>modal body</p>
        </EditModal>,
        container
      );
    });
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
});
