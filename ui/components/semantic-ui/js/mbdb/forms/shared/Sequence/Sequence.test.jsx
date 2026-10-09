import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { setIn } from "formik";
import { TextAreaField } from "@js/mbdb/forms/building-blocks/TextField";
import { Sequence } from "./Sequence";

// One shared harness: the fake "@js/oarepo_ui/forms" (model labels) and the
// Formik render helpers live in testUtils (guide §10; no per-file copies).
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);
const {
  setFakeUiModel,
  renderInForm,
  unmountForm,
  editUnrelatedField,
  ValueProbe,
  readProbe,
} = jest.requireActual("@js/mbdb/forms/building-blocks/testUtils");

const FIELD = "metadata.general_parameters.entities_of_interest.0.sequence";

let container;

const render = (options) =>
  renderInForm(
    <>
      <Sequence fieldPath={FIELD} />
      <ValueProbe path={FIELD} />
    </>,
    options
  );

beforeEach(() => {
  setFakeUiModel({});
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

// Blur with the same two-tick flush as typeInto/clickOn: a render from the
// prior change must land first, then formik's post-blur update settles, so
// by the time this returns the blur handler's setFieldValue (if any) ran.
const blurOn = async () => {
  const el = textarea();
  await act(async () => {
    await new Promise((r) => setTimeout(r, 0));
    Simulate.blur(el);
    await new Promise((r) => setTimeout(r, 0));
  });
};

const storedValue = () => readProbe(container);

describe("Sequence", () => {
  it("stores the normalized value on blur (header dropped, whitespace stripped)", () => {
    typeAndBlur(">sp|P20429\nMIEIEK PKIE\nTVEIS");
    expect(storedValue()).toBe("MIEIEKPKIETVEIS");
  });

  it("blur on an already-normalized value does not write; a value needing normalization writes once", async () => {
    // Spy on the write: a JSON compare cannot fail because formik's setIn
    // returns the same object for an equal value, so this intercepts
    // setFieldValue directly and asserts whether the handler calls it.
    const spy = jest.fn();
    unmountForm(container);
    container = renderInForm(
      <>
        <Sequence fieldPath={FIELD} />
        <ValueProbe path={FIELD} />
      </>,
      { initialValues: setIn({}, FIELD, "MIEIEK"), onSetFieldValue: spy }
    );
    // already normalized on mount; blur with nothing to do → no write
    await blurOn();
    expect(spy).not.toHaveBeenCalled();
    expect(storedValue()).toBe("MIEIEK");
    // a value needing normalization → exactly one write, of the normalized value
    const el = textarea();
    el.value = "MIE IEK";
    await act(async () => {
      Simulate.change(el);
      await new Promise((r) => setTimeout(r, 0));
    });
    spy.mockClear(); // discard the onChange write; only the blur write counts
    await blurOn();
    expect(spy).toHaveBeenCalledTimes(1);
    expect(spy).toHaveBeenCalledWith(FIELD, "MIEIEK");
  });

  it("removes the key when the textarea holds only whitespace, then blurs", () => {
    typeAndBlur("MIEI");
    expect(storedValue()).toBe("MIEI");
    typeAndBlur("   ");
    // ValueProbe renders null when the value is unset (JSON has no undefined)
    expect(storedValue()).toBeNull();
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

  it("onBlur passed to TextAreaField fires on blur of the textarea", () => {
    // The every-blur assertions above only pass because TextAreaField's
    // uiProps land on Semantic's Form.Field shell around the textarea and a
    // Simulate.blur on the textarea invokes the wrapper's handler. This is
    // the building block's one direct check of that wiring.
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

  it("shows a server error and keeps it after an unrelated edit", async () => {
    unmountForm(container);
    container = renderInForm(
      <>
        <Sequence fieldPath={FIELD} />
        <ValueProbe path={FIELD} />
      </>,
      {
        initialValues: setIn({}, FIELD, "MAH LTP"),
        initialErrors: setIn({}, FIELD, "Invalid sequence."),
        withUnrelatedField: true,
      }
    );
    expect(container.textContent).toContain("Invalid sequence.");
    // any change resets Formik `errors`; initialErrors survive while the value
    // at the error path is unchanged (guide §8, mergedErrorNode semantics)
    await editUnrelatedField(container);
    expect(container.textContent).toContain("Invalid sequence.");
  });
});
