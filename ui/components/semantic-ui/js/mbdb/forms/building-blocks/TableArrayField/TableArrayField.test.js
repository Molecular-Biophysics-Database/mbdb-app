import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { TableArrayField } from "./TableArrayField";

// The oarepo forms index is not loadable in Jest (react-searchkit/d3 ESM).
jest.mock("@js/oarepo_ui/forms", () => ({
  FormConfigProvider: ({ children }) => children,
  FieldDataProvider: ({ children }) => children,
  useFieldData: () => ({
    getFieldData: ({ fieldPath }) => ({ label: fieldPath, helpText: null }),
  }),
}));
const { FormConfigProvider, FieldDataProvider } = jest.requireMock(
  "@js/oarepo_ui/forms"
);

let container;

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const value = getIn(values, path);
  return <span data-testid="probe">{JSON.stringify(value ?? null)}</span>;
};

Probe.propTypes = {
  path: PropTypes.string,
};

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
            {ui}
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
});

const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);
const input = (label) =>
  container.querySelector(`input[aria-label="${label}"]`);
const type = (el, value) => {
  el.value = value;
  act(() => Simulate.change(el));
};
const buttons = () => [...container.querySelectorAll("button")];

const PROTOCOL_COLUMNS = [
  { field: "name", label: "Name", required: true, width: 4 },
  { field: "description", label: "Description", required: true },
];

const protocol = (props = {}) => (
  <>
    <TableArrayField
      fieldPath="steps"
      label="Preparation protocol"
      required
      minItems={1}
      addButtonLabel="Add step"
      columns={PROTOCOL_COLUMNS}
      {...props}
    />
    <Probe path="steps" />
  </>
);

describe("TableArrayField", () => {
  it("creates minItems empty rows on first render and renders headers", () => {
    mount(protocol());
    expect(probe()).toEqual([{}]);
    expect(container.textContent).toContain("Preparation protocol");
    expect(container.textContent).toContain("Name *");
    expect(container.textContent).toContain("Description *");
    expect(buttons().some((b) => b.textContent.includes("Add step"))).toBe(
      true
    );
    // the minItems row has no remove button
    expect(
      container.querySelector('button[aria-label="Remove row 1"]')
    ).toBeNull();
  });

  it("renders initial values and keeps extra minItems rows removable", () => {
    mount(protocol(), {
      initialValues: {
        steps: [
          { name: "Centrifugation", description: "10 min" },
          { name: "Filtration", description: "0.22 µm" },
        ],
      },
    });
    expect(input("Name").value).toBe("Centrifugation");
    expect(
      container.querySelector('button[aria-label="Remove row 1"]')
    ).toBeNull();
    expect(
      container.querySelector('button[aria-label="Remove row 2"]')
    ).not.toBeNull();
  });

  it("writes edits back to Formik", () => {
    mount(protocol(), {
      initialValues: { steps: [{ name: "old", description: "" }] },
    });
    type(input("Name"), "new name");
    expect(probe()).toEqual([{ name: "new name", description: "" }]);
  });

  it("adds a row with the Add button and removes rows with remove", () => {
    mount(protocol());
    const add = buttons().find((b) => b.textContent.includes("Add step"));
    act(() => Simulate.click(add));
    expect(probe()).toEqual([{}, {}]);
    type(container.querySelectorAll('input[aria-label="Name"]')[1], "step 2");
    expect(probe()).toEqual([{}, { name: "step 2" }]);

    act(() =>
      Simulate.click(
        container.querySelector('button[aria-label="Remove row 2"]')
      )
    );
    expect(probe()).toEqual([{}]);
  });

  it("stores numbers as numbers and clears them to undefined", () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[{ field: "amount", label: "Amount", type: "number" }]}
        />
        <Probe path="rows" />
      </>,
      { initialValues: { rows: [{ amount: 1 }] } }
    );
    type(input("Amount"), "2.5");
    expect(probe()).toEqual([{ amount: 2.5 }]);
    type(input("Amount"), "");
    expect(probe()).toEqual([{}]);
  });

  it("serializes column edits through serialize/deserialize (external databases)", () => {
    const serialize = ({ database, id }) =>
      !database && !id ? "" : `${database ?? ""}:${id ?? ""}`;
    const deserialize = (stored) => {
      const [database = "", id = ""] = (stored ?? "").split(":");
      return { database, id };
    };
    mount(
      <>
        <TableArrayField
          fieldPath="dbs"
          columns={[
            { field: "database", label: "Database" },
            { field: "id", label: "ID" },
          ]}
          serialize={serialize}
          deserialize={deserialize}
          rowHint={(row) =>
            (row.database || row.id) && !(row.database && row.id)
              ? "Incomplete"
              : null
          }
        />
        <Probe path="dbs" />
      </>,
      { initialValues: { dbs: ["pdb:1GWD"] } }
    );
    expect(input("Database").value).toBe("pdb");
    expect(input("ID").value).toBe("1GWD");

    // one part emptied: partial string kept + yellow Incomplete hint
    type(input("Database"), "");
    expect(probe()).toEqual([":1GWD"]);
    expect(container.textContent).toContain("Incomplete");

    // both empty: empty string for the serializer to drop
    type(input("ID"), "");
    expect(probe()).toEqual([""]);
    expect(container.textContent).not.toContain("Incomplete");
  });

  it("select column renders a dropdown with clearable options", () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[
            {
              field: "unit",
              label: "Unit",
              type: "select",
              options: ["Da", "kDa"],
            },
          ]}
        />
        <Probe path="rows" />
      </>,
      { initialValues: { rows: [{ unit: "kDa" }] } }
    );
    const dropdown = container.querySelector(".ui.dropdown");
    expect(dropdown.textContent).toContain("kDa");
    act(() => Simulate.click(dropdown));
    const item = [...dropdown.querySelectorAll(".menu .item")].find(
      (el) => el.textContent === "Da"
    );
    act(() => Simulate.click(item));
    expect(probe()).toEqual([{ unit: "Da" }]);
  });

  it("textarea column renders a textarea", () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[{ field: "note", label: "Note", type: "textarea" }]}
        />
        <Probe path="rows" />
      </>,
      { initialValues: { rows: [{ note: "hello" }] } }
    );
    const area = container.querySelector("textarea");
    type(area, "multi line");
    expect(probe()).toEqual([{ note: "multi line" }]);
  });

  it("render column shows computed read-only content", () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[
            { field: "id", label: "ID" },
            { field: "link", label: "Open", render: (row) => `link:${row.id}` },
          ]}
        />
        <Probe path="rows" />
      </>,
      { initialValues: { rows: [{ id: "1GWD" }] } }
    );
    expect(container.textContent).toContain("link:1GWD");
    // render columns are read-only: no input for them
    expect(container.querySelectorAll("input")).toHaveLength(1);
  });

  it("shows cell errors as red inputs with a pointing label", () => {
    mount(protocol(), {
      initialValues: { steps: [{ name: "", description: "ok" }] },
      initialErrors: { steps: [{ name: "Missing data for required field." }] },
    });
    // SUI puts the .error class on the input's wrapper div
    expect(input("Name").closest(".ui.input").className).toContain("error");
    expect(container.querySelector(".ui.red.pointing.label").textContent).toBe(
      "Missing data for required field."
    );
  });

  it("supports an expandable editable row, auto-opened on errors", () => {
    mount(
      <>
        <TableArrayField
          fieldPath="mods"
          columns={[{ field: "position", label: "Position", type: "number" }]}
          expandToggle={(row) => `${(row.steps ?? []).length} steps`}
          renderExpanded={(itemPath) => (
            <div data-testid={`expanded-${itemPath}`}>EXPANDED</div>
          )}
        />
        <Probe path="mods" />
      </>,
      {
        initialValues: { mods: [{ position: 3, steps: [{ name: "s" }] }] },
        initialErrors: { mods: [{ steps: [{ name: "Required." }] }] },
      }
    );
    // auto-open because of the nested error
    expect(byTestId(container)).not.toBeNull();
    const toggle = buttons().find((b) => b.textContent.includes("steps"));
    expect(toggle.textContent).toContain("1 steps");
    expect(toggle.getAttribute("aria-expanded")).toBe("true");
  });
});

const byTestId = (c) => c.querySelector('[data-testid^="expanded-"]');
