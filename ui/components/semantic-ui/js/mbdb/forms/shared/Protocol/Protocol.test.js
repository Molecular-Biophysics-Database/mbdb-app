import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { Protocol } from "./Protocol";

jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// Client-only row keys (jsdom has no WebCrypto); incrementing, so rows differ
let mockKeyN = 0;
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => `key-${++mockKeyN}-uuid`,
}));

const PATH = "protocol";

const UI_MODEL = {
  [PATH]: {
    label: "Preparation protocol",
    helpText:
      "List of the steps performed during the preparation of the complex substance",
    required: true,
  },
  [`${PATH}.name`]: { label: "Name", required: true },
  [`${PATH}.description`]: { label: "Description", required: true },
};

// draft gvfzs-t5060, entity "Human serum"
const SAMPLE_STEPS = [
  {
    name: "Centrifugation",
    description:
      "Tubes were centrifuged for 10 min at 1,300g at 4°C within 2 hours of collection",
  },
  {
    name: "Aliquotation",
    description:
      "The supernatant was distributed among 0.5mL cryostorage tubes that were maintained at 4°C",
  },
];

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const value = getIn(values, path);
  return <span data-testid="probe">{JSON.stringify(value ?? null)}</span>;
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

const protocol = (props = {}) => (
  <>
    <Protocol fieldPath={PATH} {...props} />
    <Probe path={PATH} />
  </>
);

const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);

const type = async (el, value) => {
  el.value = value;
  // formik's SET_ERRORS lands in a promise: flush it before asserting
  await act(async () => {
    Simulate.change(el);
  });
};

const click = async (el) => {
  await act(async () => {
    Simulate.click(el);
  });
};

const nameInputs = () => [
  ...container.querySelectorAll('input[aria-label="Name"]'),
];
const descriptionAreas = () => [
  ...container.querySelectorAll('textarea[aria-label="Description"]'),
];

describe("Protocol", () => {
  it("renders the filled rows with their values", () => {
    render(protocol(), { initialValues: { [PATH]: SAMPLE_STEPS } });
    expect(nameInputs().map((i) => i.value)).toEqual([
      "Centrifugation",
      "Aliquotation",
    ]);
    expect(descriptionAreas().map((a) => a.value)).toEqual([
      SAMPLE_STEPS[0].description,
      SAMPLE_STEPS[1].description,
    ]);
  });

  it("with minItems={1} and no value: one virtual row, no remove button, nothing stored", () => {
    render(protocol({ minItems: 1 }));
    expect(nameInputs().length).toBe(1);
    expect(container.querySelector('[aria-label="Remove row 1"]')).toBeNull();
    expect(probe()).toBeNull();
  });

  it("without minItems: no rows; Add stores a row; removing it leaves the key absent", async () => {
    render(protocol());
    expect(nameInputs().length).toBe(0);

    const add = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "Add step"
    );
    await click(add);
    expect(nameInputs().length).toBe(1);
    expect(probe()).toEqual([{}]);

    await click(container.querySelector('[aria-label="Remove row 1"]'));
    expect(nameInputs().length).toBe(0);
    // never []: a minItems: 1 server side would reject it
    expect(probe()).toBeNull();
  });

  it("clearing a description removes the key, never an empty string", async () => {
    render(
      protocol({
        minItems: 0,
      }),
      {
        initialValues: {
          [PATH]: [{ name: "Centrifugation", description: "10 min at 4000 g" }],
        },
      }
    );
    await type(descriptionAreas()[0], "");
    expect(probe()).toEqual([{ name: "Centrifugation" }]);
  });

  it("shows a cell error from initialErrors; it stays after an edit in another cell", async () => {
    render(protocol(), {
      initialValues: {
        [PATH]: [
          { name: "Centrifugation" },
          { name: "Filtration", description: "0.22 µm filter" },
        ],
      },
      initialErrors: {
        [PATH]: [{ description: "Missing data for required field." }],
      },
    });
    expect(container.textContent).toContain("Missing data for required field.");

    // editing an unrelated cell makes formik reset `errors` to {}; the
    // server error on row 0 must keep showing (its own value is untouched)
    await type(nameInputs()[1], "Ultrafiltration");
    expect(container.textContent).toContain("Missing data for required field.");
    // still rendered as a red error label by the cell, not lost with `errors`
    // (Semantic Label is a div, so select by class, not element)
    expect(
      [...container.querySelectorAll(".red.label")].some((el) =>
        el.textContent.includes("Missing data for required field.")
      )
    ).toBe(true);
  });

  it("sizes the description textarea rows to the content", () => {
    render(protocol(), {
      initialValues: {
        [PATH]: [
          { name: "Long", description: "x".repeat(400) },
          { name: "Short", description: "short" },
        ],
      },
    });
    const rows = descriptionAreas().map((a) => Number(a.getAttribute("rows")));
    // 400 chars without breaks: 5 rows; a short description keeps the 3-row minimum
    expect(rows[0]).toBe(5);
    expect(rows[1]).toBe(3);
  });
});
