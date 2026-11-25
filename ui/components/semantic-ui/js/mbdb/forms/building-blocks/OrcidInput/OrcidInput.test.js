import React, { useState } from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import ReactDOM from "react-dom";
import { OrcidInput } from "./OrcidInput";
import { unmountForm } from "@js/mbdb/forms/building-blocks/testUtils";

// OrcidInput is a plain controlled component (no formik, no model data), so
// it renders in a bare container with a local-state wrapper.

let container;

afterEach(() => {
  unmountForm(container);
  container = null;
});

const Harness = ({ initial }) => {
  const [boxes, setBoxes] = useState(
    Array.from({ length: 16 }, (_, i) => initial?.[i] ?? "")
  );
  return (
    <div>
      <OrcidInput value={boxes} onChange={setBoxes} />
      <span data-testid="digits">{JSON.stringify(boxes)}</span>
    </div>
  );
};

Harness.propTypes = {
  initial: PropTypes.string,
};

const render = (initial) => {
  container = document.createElement("div");
  document.body.appendChild(container);
  act(() => {
    ReactDOM.render(<Harness initial={initial} />, container);
  });
  return container;
};

const boxes = () => [...container.querySelectorAll(".mbdb-orcid-box input")];
const readDigits = () =>
  JSON.parse(container.querySelector('[data-testid="digits"]').textContent);
const type = (box, value) =>
  act(() => {
    box.value = value;
    Simulate.change(box, { target: { value } });
  });

describe("OrcidInput", () => {
  it("renders 16 boxes in four dash-separated groups", () => {
    render();
    expect(boxes()).toHaveLength(16);
    expect(container.querySelectorAll(".mbdb-orcid-dash")).toHaveLength(3);
  });

  it("types one digit per box, keeping the box position", () => {
    render();
    type(boxes()[0], "1");
    type(boxes()[4], "2");
    expect(readDigits()[0]).toBe("1");
    expect(readDigits()[4]).toBe("2");
    expect(boxes()[4].value).toBe("2");
    // the untouched boxes between them stay empty
    expect(readDigits().slice(1, 4)).toEqual(["", "", ""]);
  });

  it("ignores non-digits and multi-character input", () => {
    render();
    type(boxes()[0], "a");
    expect(readDigits()[0]).toBe("");
    type(boxes()[0], "12");
    expect(readDigits()[0]).toBe("");
  });

  it("initializes the boxes from the stored value", () => {
    render("000000021825009");
    expect(boxes().map((b) => b.value)).toEqual(
      Array.from({ length: 16 }, (_, i) => "000000021825009"[i] ?? "")
    );
  });

  it("paste fills the boxes from mixed text (an orcid.org URL)", () => {
    render();
    act(() => {
      Simulate.paste(boxes()[0], {
        clipboardData: {
          getData: () => "https://orcid.org/0000-0002-1825-0097",
        },
      });
    });
    expect(readDigits().join("")).toBe("0000000218250097");
    expect(boxes()[15].value).toBe("7");
  });

  it("backspace on an empty box clears and focuses the previous one", () => {
    render("00000000");
    // the 9th box (index 8) is empty: backspace there clears box 7
    act(() => {
      Simulate.keyDown(boxes()[8], { key: "Backspace" });
    });
    expect(readDigits().join("")).toBe("0000000");
    expect(document.activeElement).toBe(boxes()[7]);
  });

  it("arrow keys move the focus between boxes", () => {
    render();
    type(boxes()[0], "1");
    expect(document.activeElement).toBe(boxes()[1]);
    act(() => {
      Simulate.keyDown(boxes()[1], { key: "ArrowLeft" });
    });
    expect(document.activeElement).toBe(boxes()[0]);
  });
});
