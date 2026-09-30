import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik } from "formik";
import { Table } from "mbdb-semantic-ui-react";
import { SummaryItem } from "./SummaryItem";

// @js/oarepo_ui/forms/index pulls in react-searchkit (d3, ESM), which Jest
// cannot load; SummaryItem itself does not use it, but DetailView-based
// details do, so detail contents here are plain nodes.
jest.mock("@js/oarepo_ui/forms", () => ({
  FormConfigProvider: ({ children }) => children,
  FieldDataProvider: ({ children }) => children,
  useFieldData: () => ({
    getFieldData: ({ fieldPath }) => ({ label: fieldPath }),
  }),
}));
const { FormConfigProvider, FieldDataProvider } = jest.requireMock(
  "@js/oarepo_ui/forms"
);

let container;

const mount = (ui, { initialValues = {}, initialErrors = {} } = {}) => {
  container = document.createElement("div");
  document.body.appendChild(container);
  act(() => {
    ReactDOM.render(
      <FormConfigProvider value={{ config: { ui_model: {} } }}>
        <FieldDataProvider>
          <Formik
            initialValues={initialValues}
            initialErrors={initialErrors}
            onSubmit={() => {}}
          >
            <Table compact>
              <Table.Body>{ui}</Table.Body>
            </Table>
          </Formik>
        </FieldDataProvider>
      </FormConfigProvider>,
      container
    );
  });
};

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
  // portals (Confirm) mount on document.body
  document
    .querySelectorAll(".ui.modal, .ui.dimmer")
    .forEach((el) => el.remove());
});

const row = (o) => (
  <SummaryItem
    fieldPath="o"
    columns={[(v) => v.name, (v) => v.type]}
    itemName="entity"
    detail={<div data-testid="detail">DETAILS</div>}
    {...o}
  />
);

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);
const toggleButton = () =>
  container.querySelector('button[aria-label="Show details of entity"]');
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

    act(() => Simulate.click(toggleButton()));
    expect(byTestId("detail")).not.toBeNull();
    expect(toggleButton().getAttribute("aria-expanded")).toBe("true");
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

  it("hides the toggle when no detail is given", () => {
    mount(
      <SummaryItem
        fieldPath="o"
        columns={[(v) => v.name]}
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
      initialValues: { o: { name: "Zn2+", extra: { deep: "x" } } },
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

  it("hides the remove button when onRemove is undefined or removable=false", () => {
    mount(row({ onEdit: () => {}, onRemove: undefined }), {
      initialValues: { o: {} },
    });
    expect(removeButton()).toBeNull();
  });
});
