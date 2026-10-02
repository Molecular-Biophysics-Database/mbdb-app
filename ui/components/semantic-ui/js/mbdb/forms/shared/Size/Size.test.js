import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { Size } from "./Size";
import { SIZE_TYPES, LENGTH_UNITS } from "./constants";

jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

const PATH = "size";

// The group is optional; type/unit/mean are marked required in the model
// (they describe the inside of `size`),
// which the block overrides with "required only once filled".
const UI_MODEL = {
  [PATH]: {
    label: "Size",
    helpText: "The size of the lipid assembly",
    required: false,
  },
  [`${PATH}.type`]: { label: "Type", required: true },
  [`${PATH}.unit`]: { label: "Unit", required: true },
  [`${PATH}.mean`]: { label: "Mean", required: true },
  [`${PATH}.median`]: { label: "Median", required: false },
  [`${PATH}.lower`]: { label: "Lower", required: false },
  [`${PATH}.upper`]: { label: "Upper", required: false },
};

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const v = getIn(values, path);
  return (
    <span data-testid="probe">
      {v === undefined ? "null" : JSON.stringify(v)}
    </span>
  );
};
Probe.propTypes = { path: PropTypes.string.isRequired };

let container;

beforeEach(() => {
  setFakeUiModel(UI_MODEL);
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

const size = () => (
  <>
    <Size fieldPath={PATH} />
    <Probe path={PATH} />
  </>
);

const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);

// render order: mean row, then median/lower/upper
const numberInputs = () => [
  ...container.querySelectorAll('input[type="number"]'),
];

const type = async (el, value) => {
  el.value = value;
  await act(async () => {
    Simulate.change(el);
  });
};

const click = async (el) => {
  await act(async () => {
    Simulate.click(el);
  });
};

const meanInput = () => numberInputs()[0];

const requiredFields = () => container.querySelectorAll(".field.required");

describe("Size", () => {
  it("SIZE_TYPES and LENGTH_UNITS equal the YAML enums, μm is U+03BC", () => {
    // Read the enums from the model, so a model change or a retyped
    // character fails the test instead of matching a hand-copy.
    expect(SIZE_TYPES).toEqual(yamlEnum("Size", "type"));
    expect(LENGTH_UNITS).toEqual(yamlEnum("LENGTH_UNITS"));
    // the YAML encodes μm as the Greek letter mu (U+03BC) + m; the micro
    // sign µ (U+00B5) is a different string the server would reject
    expect(LENGTH_UNITS[2]).toBe("μm");
    expect(LENGTH_UNITS[2].charCodeAt(0)).toBe(0x03bc);
  });

  it("empty size shows no required markers; once mean is typed, type, unit and mean are marked", async () => {
    render(size());
    expect(requiredFields().length).toBe(0);

    await type(meanInput(), "45");
    expect(requiredFields().length).toBe(3);
    expect(probe()).toEqual({ mean: 45 });
  });

  it("stores the full statistics object as numbers", async () => {
    render(size(), {
      initialValues: {
        [PATH]: {
          type: "diameter",
          unit: "nm",
          mean: 120,
          lower: 90,
          upper: 150,
        },
      },
    });
    expect(probe()).toEqual({
      type: "diameter",
      unit: "nm",
      mean: 120,
      lower: 90,
      upper: 150,
    });
    expect(typeof numberInputs()[0].valueAsNumber).toBe("number");
  });

  it("Clear size removes the whole object, even with required rows filled (Size-review F1)", async () => {
    // required={filled} blocks clearing type/unit (ButtonGroupField ignores
    // toggle-off, required SelectField has no clear icon), so one click on
    // "radius" would otherwise trap an optional object that the server
    // rejects. "Clear size" is the way back to absent.
    render(size(), {
      initialValues: {
        [PATH]: { type: "radius", unit: "nm", mean: 45, lower: 30 },
      },
    });
    expect(container.querySelector(".dropdown .clear.icon")).toBeNull();
    const clearButton = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "Clear size"
    );
    expect(clearButton).toBeDefined();
    await click(clearButton);
    expect(probe()).toBeNull();
  });

  it("clicking only a Type button, then Clear size, leaves size absent", async () => {
    render(size());
    await click(
      [...container.querySelectorAll(".ui.buttons button")].find(
        (b) => b.textContent === "radius"
      )
    );
    expect(probe()).toEqual({ type: "radius" });
    const clearButton = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "Clear size"
    );
    await click(clearButton);
    expect(probe()).toBeNull();
  });

  it('clearing numeric fields prunes their keys (never "" or {} behind)', async () => {
    render(size(), {
      initialValues: {
        [PATH]: { type: "radius", unit: "nm", mean: 45, lower: 30 },
      },
    });
    await type(meanInput(), "");
    expect(probe()).toEqual({ type: "radius", unit: "nm", lower: 30 });
    await type(numberInputs()[2], ""); // upper (median, lower, upper order)
    expect(probe()).toEqual({ type: "radius", unit: "nm" });
  });

  it("a size without type/unit can be cleared back to absent", async () => {
    // a partially filled size (only numbers entered) returns to absent when
    // the last number is cleared — the pruning unset drops the empty object
    render(size(), { initialValues: { [PATH]: { mean: 45 } } });
    await type(meanInput(), "");
    expect(probe()).toBeNull();
  });

  it("row errors show and stay after an edit in another row", async () => {
    render(size(), {
      initialValues: { [PATH]: { mean: 45 } },
      initialErrors: {
        [PATH]: {
          type: "Missing data for required field.",
          unit: "Missing data for required field.",
        },
      },
    });
    // Semantic Label renders as a div — select by class, not element
    expect(
      container.querySelectorAll(".red.pointing.label").length
    ).toBeGreaterThan(0);

    // an edit elsewhere resets formik `errors`; the untouched server errors
    // must keep showing
    await type(meanInput(), "60");
    expect(container.textContent).toContain("Missing data for required field.");
    expect(
      container.querySelectorAll(".red.pointing.label").length
    ).toBeGreaterThan(0);
  });

  it("the object-level error shows under the group header (D1/Size-review F2)", () => {
    render(size(), {
      initialErrors: { [PATH]: "Missing data for required field." },
    });
    expect(container.querySelector("h5.ui.header.red")).not.toBeNull();
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".ui.pointing.prompt.label")).not.toBeNull();
  });

  it("unit is not pre-selected: the dropdown shows no chosen text", () => {
    render(size());
    // `.text` is what Semantic shows as the chosen option; an empty one means
    // no unit was written. (The old `.default.text` assertion could not fail.)
    // The chosen value is the direct-child text span; option rows inside
    // the menu carry `.text` too (and Semantic marks option 0 visually), so
    // scope it. Empty chosen text + nothing stored = not pre-selected.
    const text = container.querySelector(".dropdown > .text");
    expect(text === null ? "" : text.textContent.trim()).toBe("");
    expect(probe()).toBeNull();
  });
});
