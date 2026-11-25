import React from "react";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { ErrorMessages } from "./ErrorMessages";

// Presentation-only (no Formik), so render into a bare container.
let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const render = (ui) =>
  act(() => {
    ReactDOM.render(ui, container);
  });

describe("ErrorMessages", () => {
  it("renders nothing for an absent list", () => {
    render(<ErrorMessages />);
    expect(container.querySelector(".ui.label")).toBeNull();
  });

  it("renders nothing for an empty list", () => {
    render(<ErrorMessages messages={[]} />);
    expect(container.querySelector(".ui.label")).toBeNull();
  });

  it("renders two messages joined in one pointing prompt label", () => {
    render(<ErrorMessages messages={["First error.", "Second error."]} />);
    const label = container.querySelector(".ui.pointing.prompt.label");
    expect(label).not.toBeNull();
    expect(label.textContent).toBe("First error. Second error.");
  });
});
