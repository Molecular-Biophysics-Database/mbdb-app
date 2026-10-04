import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext } from "formik";
import { DisclosureDefaultProvider, Table } from "mbdb-semantic-ui-react";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import { SummaryItem } from "./SummaryItem";
import {
  renderInForm,
  unmountForm,
} from "@js/mbdb/forms/building-blocks/testUtils";

// @js/oarepo_ui/forms/index pulls in react-searchkit (d3, ESM), which Jest
// cannot load; SummaryItem itself does not use it, but DetailView-based
// details do, so detail contents here are plain nodes.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

let container;

// ui is wrapped in a Table; `siblings` render outside the table (e.g. an
// unrelated input used to prove the badge survives edits elsewhere).
const mount = (ui, { siblings = null, ...opts } = {}) => {
  container = renderInForm(
    <>
      <Table compact>
        <Table.Body>{ui}</Table.Body>
      </Table>
      {siblings}
    </>,
    opts
  );
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

const row = (o) => (
  <SummaryItem
    fieldPath="o"
    cells={[(v) => v.name, (v) => v.type]}
    itemName="entity"
    detail={<div data-testid="detail">DETAILS</div>}
    {...o}
  />
);

// A Formik-connected input for an unrelated field, so Simulate.change drives
// Formik's setFieldValue (and its async errors reset) — used by the errors-after-edit test.
const UnrelatedInput = () => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <input
      data-testid="other"
      value={values.other ?? ""}
      onChange={(e) => setFieldValue("other", e.target.value)}
    />
  );
};

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);
// the ▸/▾ button; its label switches Show/Hide with the open state
const toggleButton = () =>
  container.querySelector('button[aria-label$="details of entity"]');
const removeButton = () =>
  container.querySelector('button[aria-label="Remove entity"]');
const confirmOnBody = () => document.body.querySelector(".ui.modal");

describe("SummaryItem", () => {
  it("renders column texts and a grey dash for empty cells", () => {
    mount(row({ onEdit: () => {}, onRemove: () => {} }), {
      initialValues: { o: { name: "Lysozyme" } },
    });
    expect(container.textContent).toContain("Lysozyme");
    expect(container.textContent).toContain("—");
    expect(container.textContent).toContain("Edit");
  });

  it("opens and hides the details row via the toggle button", () => {
    mount(row({ onEdit: () => {}, onRemove: () => {} }), {
      initialValues: { o: { name: "Lysozyme" } },
    });
    expect(byTestId("detail")).toBeNull();
    expect(toggleButton().getAttribute("aria-expanded")).toBe("false");
    expect(toggleButton().getAttribute("aria-label")).toBe(
      "Show details of entity"
    );

    act(() => Simulate.click(toggleButton()));
    expect(byTestId("detail")).not.toBeNull();
    expect(toggleButton().getAttribute("aria-expanded")).toBe("true");
    expect(toggleButton().getAttribute("aria-label")).toBe(
      "Hide details of entity"
    );
    expect(container.querySelector("tr.mbdb-details")).not.toBeNull();

    act(() => Simulate.click(toggleButton()));
    expect(byTestId("detail")).toBeNull();
  });

  it("toggles on Enter on the focused row", () => {
    mount(row({ onEdit: () => {}, onRemove: () => {} }), {
      initialValues: { o: { name: "Lysozyme" } },
    });
    const cell = container.querySelector("tr td:nth-child(2)");
    const tr = cell.closest("tr");
    expect(tr.getAttribute("tabindex")).toBe("0");
    act(() => Simulate.keyDown(cell, { key: "Enter" }));
    expect(byTestId("detail")).not.toBeNull();
    act(() => Simulate.keyDown(cell, { key: " " }));
    expect(byTestId("detail")).not.toBeNull(); // only Enter toggles
  });

  it("toggles on row background click but not on button clicks", () => {
    const onEdit = jest.fn();
    mount(row({ onEdit, onRemove: () => {} }), {
      initialValues: { o: { name: "Lysozyme" } },
    });
    // click a button: no toggle
    const edit = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "Edit"
    );
    act(() => Simulate.click(edit));
    expect(onEdit).toHaveBeenCalledTimes(1);
    expect(byTestId("detail")).toBeNull();

    // click the row cell background: toggles
    const cell = container.querySelector("tr td:nth-child(2)");
    act(() => Simulate.click(cell, { target: cell }));
    expect(byTestId("detail")).not.toBeNull();
  });

  it("tints an open pair: the summary row and its details row both carry mbdb-row-open (P5-F1)", () => {
    mount(row({ onEdit: () => {}, onRemove: () => {} }), {
      initialValues: { o: { name: "Lysozyme" } },
    });
    // closed -> nothing highlighted
    expect(container.querySelectorAll("tr.mbdb-row-open")).toHaveLength(0);
    act(() => Simulate.click(toggleButton()));
    const rows = [...container.querySelectorAll("tbody tr")];
    expect(rows.map((r) => r.classList.contains("mbdb-row-open"))).toEqual([
      true,
      true,
    ]);
    // the details row keeps its `.mbdb-details` marker too
    expect(container.querySelector("tr.mbdb-details")).not.toBeNull();
    // ... and only the details row is one, so the LESS tints the summary row
    // darker than the details row (2026-10-04, two-tone open pair)
    expect(rows[0].classList.contains("mbdb-details")).toBe(false);
    expect(rows[1].classList.contains("mbdb-details")).toBe(true);
  });

  it("hides the toggle when no detail is given", () => {
    mount(
      <SummaryItem
        fieldPath="o"
        cells={[(v) => v.name]}
        itemName="entity"
        onEdit={() => {}}
      />,
      { initialValues: { o: { name: "Lysozyme" } } }
    );
    expect(toggleButton()).toBeNull();
    expect(container.textContent).toContain("Lysozyme");
  });

  it("shows the error badge and routes its click to onEdit", () => {
    const onEdit = jest.fn();
    mount(row({ onEdit, onRemove: () => {} }), {
      initialValues: { o: { name: "Zn2+", extra: { deep: "x" } }, other: "a" },
      initialErrors: {
        o: {
          name: "Missing data for required field.",
          extra: { deep: "Bad." },
        },
      },
    });
    const badge = container.querySelector(".ui.red.label");
    expect(badge.textContent).toBe("2 errors");
    act(() => Simulate.click(badge));
    expect(onEdit).toHaveBeenCalledTimes(1);
  });

  it("keeps the badge after an unrelated edit clears Formik's errors (F1)", async () => {
    // The deposit form passes server errors as initialErrors and has no
    // validate; the first setFieldValue async-resets `errors` to {}. The badge
    // must survive via the initialErrors fallback (value at `o` is unchanged).
    mount(row({ onEdit: () => {}, onRemove: () => {} }), {
      initialValues: { o: { name: "" }, other: "" },
      initialErrors: { o: { name: "Missing data for required field." } },
      siblings: <UnrelatedInput />,
    });
    expect(container.querySelector(".ui.red.label").textContent).toBe(
      "1 error"
    );

    // edit the unrelated field; formik clears `errors` asynchronously (await)
    const other = container.querySelector('[data-testid="other"]');
    other.value = "changed";
    await act(async () => Simulate.change(other));
    expect(container.querySelector(".ui.red.label").textContent).toBe(
      "1 error"
    );
  });

  it("removes an empty object without confirmation", () => {
    const onRemove = jest.fn();
    mount(row({ onEdit: () => {}, onRemove }), {
      initialValues: { o: {} },
    });
    act(() => Simulate.click(removeButton()));
    expect(onRemove).toHaveBeenCalledTimes(1);
    expect(confirmOnBody()).toBeNull();
  });

  it("asks for confirmation before removing an object with data", () => {
    const onRemove = jest.fn();
    mount(row({ onEdit: () => {}, onRemove }), {
      initialValues: { o: { name: "Lysozyme" } },
    });
    act(() => Simulate.click(removeButton()));
    expect(onRemove).not.toHaveBeenCalled();
    const modal = confirmOnBody();
    expect(modal).not.toBeNull();
    expect(modal.textContent).toContain("Remove entity?");
    expect(modal.textContent).toContain("This cannot be undone.");

    const confirmBtn = [...modal.querySelectorAll("button")].find(
      (b) => b.textContent === "Remove"
    );
    act(() => Simulate.click(confirmBtn));
    expect(onRemove).toHaveBeenCalledTimes(1);
  });

  it("hides the remove button when onRemove is undefined", () => {
    mount(row({ onEdit: () => {}, onRemove: undefined }), {
      initialValues: { o: {} },
    });
    expect(removeButton()).toBeNull();
  });
});

describe("SummaryItem disclosure default (playground Expand all / Collapse all)", () => {
  it('starts open under DisclosureDefaultProvider value="open"; a click closes it', () => {
    mount(
      <DisclosureDefaultProvider value="open">
        {row({ onEdit: () => {}, onRemove: () => {} })}
      </DisclosureDefaultProvider>,
      { initialValues: { o: { name: "Lysozyme" } } }
    );
    expect(byTestId("detail")).not.toBeNull();
    expect(toggleButton().getAttribute("aria-expanded")).toBe("true");
    act(() => Simulate.click(toggleButton()));
    expect(byTestId("detail")).toBeNull();
  });

  it('opens a nested mini row inside the details under value="open" (Expand all reaches nested levels)', () => {
    mount(
      <DisclosureDefaultProvider value="open">
        <SummaryItem
          fieldPath="o"
          cells={[(v) => v.name]}
          itemName="assembly"
          onEdit={() => {}}
          detail={<DetailView fieldPath="o" groups={[]} />}
        />
      </DisclosureDefaultProvider>,
      {
        initialValues: {
          o: {
            name: "Assembly",
            components: [{ name: "Water", copy_number: 2 }],
          },
        },
      }
    );
    // the SummaryItem's own details row is open ...
    expect(container.querySelector("tr.mbdb-details")).not.toBeNull();
    // ... and the nested mini row, rendered inside those details, reads the
    // same one-shot default, so it is open too
    expect(
      container.querySelector('button[aria-label^="Hide details of item"]')
    ).not.toBeNull();
  });
});
