import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
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
    // models/general_parameters-definitions-rdm.yaml: Size.type, LENGTH_UNITS
    expect(SIZE_TYPES).toEqual(["radius", "diameter", "path length"]);
    expect(LENGTH_UNITS).toEqual(["Å", "nm", "μm", "mm", "cm", "m"]);
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

  it("clearing numeric fields prunes their keys; type and unit cannot be un-set while size holds data", async () => {
    // required={filled} makes type/unit required whenever anything is
    // filled, and the blocks refuse to clear required fields (SelectField
    // hides its clear icon, ButtonGroupField ignores toggle-off), so once
    // type or unit is chosen the user cannot return to an absent size.
    // The numeric rows must still prune cleanly (never "" or {} behind).
    render(size(), {
      initialValues: {
        [PATH]: { type: "radius", unit: "nm", mean: 45, lower: 30 },
      },
    });
    await type(meanInput(), "");
    expect(probe()).toEqual({ type: "radius", unit: "nm", lower: 30 });
    await type(numberInputs()[2], ""); // lower (median, lower, upper order)
    // only the un-clearable required rows remain — the object is never {}
    expect(probe()).toEqual({ type: "radius", unit: "nm" });
    // the required unit select offers no clear icon while size is filled
    expect(container.querySelector(".dropdown .clear.icon")).toBeNull();
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

  it("unit is not pre-selected", () => {
    render(size());
    const dropdown = container.querySelector(".dropdown .default.text");
    // Semantic shows the placeholder (default text), not a chosen unit
    expect(dropdown).toBeNull();
  });
});
