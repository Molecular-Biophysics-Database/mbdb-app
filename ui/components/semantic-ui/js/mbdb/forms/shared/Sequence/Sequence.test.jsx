import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn, setIn } from "formik";
import {
  TextField,
  TextAreaField,
} from "@js/mbdb/forms/building-blocks/TextField";
import { Sequence } from "./Sequence.jsx";

// One shared harness: the fake "@js/oarepo_ui/forms" (model labels) and the
// Formik render helpers live in testUtils (guide §10; no per-file copies).
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);
const { setFakeUiModel, renderInForm, unmountForm } = jest.requireActual(
  "@js/mbdb/forms/building-blocks/testUtils"
);

const FIELD = "metadata.general_parameters.entities_of_interest.0.sequence";

// Reads the stored value out of Formik so tests assert stored data, not DOM.
const Probe = ({ onValues }) => {
  onValues(useFormikContext().values);
  return null;
};
Probe.propTypes = { onValues: PropTypes.func.isRequired };

let container;
let values;
const collectValues = (v) => {
  values = v;
};

const render = (options) =>
  renderInForm(
    <>
      <Sequence fieldPath={FIELD} />
      <Probe onValues={collectValues} />
    </>,
    options
  );

beforeEach(() => {
  setFakeUiModel({});
  values = undefined;
  container = render();
});

afterEach(() => {
  unmountForm(container);
});

const textarea = () => container.querySelector("textarea");

// Change and blur must be separate act batches: the blur handler reads the
// value from the Formik context closure, which updates on the re-render the
// change triggers. Batching them fires blur against the pre-change values —
// in the browser the two events are always separate queue dispatches.
const typeAndBlur = (text) => {
  const el = textarea();
  el.value = text;
  act(() => {
    Simulate.change(el);
  });
  act(() => {
    Simulate.blur(el);
  });
};

const storedValue = () => getIn(values, FIELD);

describe("Sequence", () => {
  it("stores the normalized value on blur (header dropped, whitespace stripped)", () => {
    typeAndBlur(">sp|P20429\nMIEIEK PKIE\nTVEIS");
    expect(storedValue()).toBe("MIEIEKPKIETVEIS");
  });

  it("blur on an already-normalized value leaves the stored value untouched", () => {
    typeAndBlur("MIEIEK");
    const before = JSON.stringify(values);
    act(() => {
      Simulate.blur(textarea());
    });
    // the design's "no second setFieldValue": a write, even of an equal
    // string, replaces the values object — byte-identical means none happened
    expect(JSON.stringify(values)).toBe(before);
    expect(storedValue()).toBe("MIEIEK");
  });

  it("removes the key when the textarea holds only whitespace, then blurs", () => {
    typeAndBlur("MIEI");
    expect(storedValue()).toBe("MIEI");
    typeAndBlur("   ");
    expect(storedValue()).toBeUndefined();
  });

  it("updates the residue counter while typing", () => {
    const counter = () =>
      [...container.querySelectorAll(".ui.label")].find((l) =>
        /residues$/.test(l.textContent)
      );
    expect(counter().textContent).toBe("0 residues");
    const el = textarea();
    el.value = "AC<Hyp>G";
    act(() => {
      Simulate.change(el);
    });
    expect(el.value).toBe("AC<Hyp>G"); // never normalized mid-typing
    expect(counter().textContent).toBe("4 residues");
  });

  it("shows the BLAST link only when a sequence is present", () => {
    expect(container.querySelector("a.button")).toBeNull();
    const el = textarea();
    el.value = "MIEI";
    act(() => {
      Simulate.change(el);
    });
    const link = container.querySelector("a.button");
    expect(link.textContent).toContain("BLAST");
    expect(link.getAttribute("href")).toBe(
      "https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins&PROGRAM=blastp&QUERY=MIEI"
    );
  });

  it("onBlur through uiProps reaches the textarea (TextAreaField forwards it)", () => {
    // The every-blur assertions above only pass because the wrapper's onBlur
    // arrives at RIF's Form.TextArea. This is the design's one direct check
    // of that pass-through, kept on the building block it guards.
    let fired = 0;
    const probe = renderInForm(
      <TextAreaField fieldPath="x" onBlur={() => (fired += 1)} />,
      { initialValues: { x: "a" } }
    );
    act(() => {
      Simulate.blur(probe.querySelector("textarea"));
    });
    expect(fired).toBe(1);
    unmountForm(probe);
  });

  it("shows a server error and keeps it after an unrelated edit", () => {
    unmountForm(container);
    container = renderInForm(
      <>
        <TextField fieldPath="title" />
        <Sequence fieldPath={FIELD} />
        <Probe onValues={collectValues} />
      </>,
      {
        initialValues: setIn({ title: "x" }, FIELD, "MAH LTP"),
        initialErrors: setIn({}, FIELD, "Invalid sequence."),
      }
    );
    expect(container.textContent).toContain("Invalid sequence.");
    // any change resets Formik `errors`; initialErrors survive while the value
    // at the error path is unchanged (guide §8, mergedErrorNode semantics)
    const titleInput = container.querySelector("input");
    titleInput.value = "edited";
    act(() => {
      Simulate.change(titleInput);
    });
    expect(container.textContent).toContain("Invalid sequence.");
  });
});
