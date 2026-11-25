import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { setIn } from "formik";
import { StringTableField } from "./StringTableField";
import {
  setFakeUiModel,
  renderInForm,
  unmountForm,
  typeInto,
  ValueProbe,
  readProbe,
} from "@js/mbdb/forms/building-blocks/testUtils";

// One shared harness (guide §10). StringTableField reads no oarepo data itself,
// but TableArrayField (which it builds on) does, so the canonical fake is used.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);
// crypto.randomUUID needs https/localhost; jest must use the same key generator
// as the building block or TableArrayField cannot mint row keys.
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const FIELD =
  "metadata.general_parameters.entities_of_interest.0.additional_specifications";

let container;

beforeEach(() => {
  setFakeUiModel({ [FIELD]: { label: "Additional specifications" } });
});

afterEach(() => {
  unmountForm(container);
  container = null;
});

const stored = () => readProbe(container);
const specInputs = () => [
  ...container.querySelectorAll('input[aria-label="Specification"]'),
];

// `specs === undefined` = the key is absent; otherwise the stored array.
const render = (specs, extra = {}) =>
  renderInForm(
    <>
      <StringTableField
        fieldPath={FIELD}
        columnLabel="Specification"
        addButtonLabel="Add specification"
      />
      <ValueProbe path={FIELD} />
    </>,
    {
      initialValues: specs === undefined ? {} : setIn({}, FIELD, specs),
      ...extra,
    }
  );

describe("StringTableField", () => {
  it("renders one row per stored string, with the value in a cell input", () => {
    container = render(["RNase free water", "desalted"]);
    expect(specInputs().map((i) => i.value)).toEqual([
      "RNase free water",
      "desalted",
    ]);
    // the column header is the table's own text
    expect(container.querySelector("thead").textContent).toContain(
      "Specification"
    );
  });

  it("has no row-number column (showIndex is off)", () => {
    container = render(["a", "b"]);
    expect(container.querySelector("thead").textContent).not.toContain("#");
    // the header is the Specification column + the empty actions cell
    expect(container.querySelectorAll("thead th")).toHaveLength(2);
    // each row is the input cell + the actions cell, no leading index
    expect(
      container.querySelectorAll("tbody tr")[0].querySelectorAll("td")
    ).toHaveLength(2);
  });

  it("the field's own label comes from the model (not a prop)", () => {
    container = render(["x"]);
    const label = [...container.querySelectorAll("label")].find(
      (l) => l.htmlFor === FIELD
    );
    expect(label.textContent).toContain("Additional specifications");
  });

  it("editing a cell writes the string back, not the row object", async () => {
    container = render(["old"]);
    await typeInto(specInputs()[0], "new");
    expect(stored()).toEqual(["new"]);
  });

  it("'Add specification' appends an empty row (the one empty value written)", async () => {
    container = render(undefined);
    expect(specInputs()).toHaveLength(0);
    await act(async () => {
      Simulate.click(
        [...container.querySelectorAll("button")].find((b) =>
          b.textContent.includes("Add specification")
        )
      );
    });
    expect(specInputs()).toHaveLength(1);
    // accepted deviation (guide §7): the transient "" is dropped on save
    expect(stored()).toEqual([""]);
  });

  it("removing the last row leaves the key absent, never []", async () => {
    container = render(["only"]);
    await act(async () => {
      Simulate.click(container.querySelector('[aria-label="Remove row 1"]'));
    });
    expect(stored()).toBeNull();
  });

  it("shows a string error at <fieldPath>.<i> on that row and keeps it after an unrelated edit", async () => {
    container = render(["ok", ""], {
      initialErrors: setIn({}, FIELD, { 1: "Shorter than 1 character." }),
    });
    expect(container.textContent).toContain("Shorter than 1 character.");
    // an unrelated row's edit resets Formik `errors`; the server message at row
    // 1 must still show (errors ∪ initialErrors)
    await typeInto(specInputs()[0], "ok2");
    expect(container.textContent).toContain("Shorter than 1 character.");
  });
});
