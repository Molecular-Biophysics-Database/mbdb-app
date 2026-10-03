import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik } from "formik";
import { HelpModeProvider } from "mbdb-semantic-ui-react";
import { TableArrayField } from "./TableArrayField";
import {
  setFakeUiModel,
  ValueProbe,
  readProbe,
} from "@js/mbdb/forms/building-blocks/testUtils";

// Model labels/help are injected per test through setFakeUiModel
// (testUtils). The test needs Formik re-render on one container, so it keeps
// its own tree/render helpers below instead of renderInForm.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// Client-only row keys (jsdom has no WebCrypto); incrementing, so keys differ
let mockKeyN = 0;
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => `key-${++mockKeyN}-uuid`,
}));

let container;

// kept local: one test re-renders with NEW initialErrors on the SAME mounted
// Formik, which renderInForm (fresh container per call) cannot express. The
// oarepo providers are passthroughs (testUtils), so Formik alone is enough.
const tree = (
  ui,
  { initialValues = {}, initialErrors = {}, enableReinitialize = false } = {}
) => (
  <Formik
    initialValues={initialValues}
    initialErrors={initialErrors}
    enableReinitialize={enableReinitialize}
    onSubmit={() => {}}
  >
    {ui}
  </Formik>
);

const render = (element) => {
  act(() => {
    ReactDOM.render(element, container);
  });
};

const mount = (ui, opts = {}) => {
  container = document.createElement("div");
  document.body.appendChild(container);
  render(tree(ui, opts));
};

beforeEach(() => {
  setFakeUiModel({});
});

afterEach(() => {
  if (!container) return;
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
  container = null;
});

const probe = () => readProbe(container);
const input = (label) =>
  container.querySelector(`input[aria-label="${label}"]`);
const inputs = (label) => [
  ...container.querySelectorAll(`input[aria-label="${label}"]`),
];
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
const buttons = () => [...container.querySelectorAll("button")];
const byTestId = (c) => c.querySelector('[data-testid^="expanded-"]');

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
    <ValueProbe path="steps" />
  </>
);

// string-array table ("db:id"), as in ExternalDatabases
const serialize = ({ database, id }) =>
  !database && !id ? "" : `${database ?? ""}:${id ?? ""}`;
const deserialize = (stored) => {
  const [database = "", id = ""] = (stored ?? "").split(":");
  return { database, id };
};
const databases = (props = {}) => (
  <>
    <TableArrayField
      fieldPath="dbs"
      label="External databases"
      columns={[
        {
          field: "database",
          label: "Database",
          type: "select",
          options: ["pdb", "uniprot"],
          allowAdditions: true,
        },
        { field: "id", label: "ID" },
      ]}
      defaultNewValue=""
      serialize={serialize}
      deserialize={deserialize}
      rowHint={(row) =>
        (row.database || row.id) && !(row.database && row.id)
          ? "Incomplete"
          : null
      }
      {...props}
    />
    <ValueProbe path="dbs" />
  </>
);

describe("TableArrayField", () => {
  it("renders minItems rows as VIRTUAL rows: shown, but nothing is written yet (F11)", () => {
    mount(protocol());
    // no seeding write — the form stays clean
    expect(probe()).toBeNull();
    expect(container.textContent).toContain("Preparation protocol");
    expect(container.textContent).toContain("Name *");
    expect(container.textContent).toContain("Description *");
    // the row is there and editable
    expect(input("Name")).not.toBeNull();
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

  it("writes edits back to Formik", async () => {
    mount(protocol(), {
      initialValues: { steps: [{ name: "old", description: "" }] },
    });
    await type(input("Name"), "new name");
    expect(probe()).toEqual([{ name: "new name", description: "" }]);
  });

  it("clearing a text cell removes the key instead of writing an empty string (F4)", async () => {
    mount(protocol({ minItems: 0 }), {
      initialValues: { steps: [{ name: "a", description: "b" }] },
    });
    await type(input("Name"), "");
    expect(probe()).toEqual([{ description: "b" }]);
  });

  it("adds a row with the Add button and removes rows with remove", async () => {
    mount(protocol({ minItems: 0 }));
    const add = buttons().find((b) => b.textContent.includes("Add step"));
    await click(add);
    expect(probe()).toEqual([{}]);
    await click(add);
    expect(probe()).toEqual([{}, {}]);
    await type(inputs("Name")[1], "step 2");
    expect(probe()).toEqual([{}, { name: "step 2" }]);

    await click(container.querySelector('button[aria-label="Remove row 2"]'));
    expect(probe()).toEqual([{}]);
  });

  it("removing the last row removes the whole array key (F5)", async () => {
    mount(protocol({ minItems: 0 }), {
      initialValues: { steps: [{ name: "only" }] },
    });
    await click(container.querySelector('button[aria-label="Remove row 1"]'));
    expect(probe()).toBeNull();
  });

  it("keeps other rows' content and expand state when a middle row is removed (F6)", async () => {
    mount(
      <>
        <TableArrayField
          fieldPath="mods"
          columns={[{ field: "name", label: "Name" }]}
          renderExpanded={(itemPath) => (
            <div data-testid={`expanded-${itemPath}`}>EXPANDED</div>
          )}
        />
        <ValueProbe path="mods" />
      </>,
      {
        initialValues: {
          mods: [{ name: "A" }, { name: "B" }, { name: "C" }],
        },
      }
    );
    // open the last row's expanded content
    const toggles = buttons().filter((b) => b.textContent.includes("Details"));
    expect(toggles).toHaveLength(3);
    await click(toggles[2]);
    expect(byTestId(container)).not.toBeNull();

    await click(container.querySelector('button[aria-label="Remove row 1"]'));
    expect(probe()).toEqual([{ name: "B" }, { name: "C" }]);
    // rows B and C kept their identity: B's content, C still expanded
    expect(inputs("Name").map((i) => i.value)).toEqual(["B", "C"]);
    expect(byTestId(container)).not.toBeNull();
  });

  it("stores numbers as numbers and clears them to undefined", async () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[{ field: "amount", label: "Amount", type: "number" }]}
        />
        <ValueProbe path="rows" />
      </>,
      { initialValues: { rows: [{ amount: 1 }] } }
    );
    await type(input("Amount"), "2.5");
    expect(probe()).toEqual([{ amount: 2.5 }]);
    await type(input("Amount"), "");
    expect(probe()).toEqual([{}]);
  });

  it("stores undefined — never NaN — for unparseable number input", async () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[{ field: "amount", label: "Amount", type: "number" }]}
        />
        <ValueProbe path="rows" />
      </>,
      { initialValues: { rows: [{ amount: 1 }] } }
    );
    await type(input("Amount"), "abc");
    expect(probe()).toEqual([{}]);
  });

  it("serializes column edits through serialize/deserialize (external databases)", async () => {
    mount(databases(), { initialValues: { dbs: ["pdb:1GWD"] } });
    expect(input("ID").value).toBe("1GWD");

    // clearing a text cell maps "" to undefined; serialize keeps the partial
    await type(input("ID"), "");
    expect(probe()).toEqual(["pdb:"]);
    expect(container.textContent).toContain("Incomplete");
  });

  it('Add on a serialize table pushes the stored shape (""), not a row object (F3)', async () => {
    mount(databases(), { initialValues: { dbs: ["pdb:1GWD"] } });
    const add = buttons().find((b) => b.textContent.includes("Add"));
    await click(add);
    expect(probe()).toEqual(["pdb:1GWD", ""]);
    // the new row shows empty inputs (deserialize("") does not throw)
    expect(inputs("ID")[1].value).toBe("");
  });

  it("writes an edited virtual minItems row into the store (F11)", async () => {
    mount(databases({ minItems: 1 }));
    expect(probe()).toBeNull();
    // the virtual row: editing it materializes the array
    const idInput = container.querySelector('input[aria-label="ID"]');
    await type(idInput, "1GWD");
    expect(probe()).toEqual([":1GWD"]);
    // still exactly one row (the virtual one became real)
    expect(inputs("ID")).toHaveLength(1);
  });

  it("select column renders a dropdown with clearable options, and shows an added value (F9)", async () => {
    mount(databases(), { initialValues: { dbs: ["emdb:1234"] } });
    // "emdb" is not in options but must be visible (allowAdditions)
    const dropdown = container.querySelector(".ui.dropdown");
    expect(dropdown.textContent).toContain("emdb");
    await click(dropdown);
    const item = [...dropdown.querySelectorAll(".menu .item")].find(
      (el) => el.textContent === "pdb"
    );
    await click(item);
    expect(probe()).toEqual(["pdb:1234"]);
  });

  it("textarea column renders a textarea", async () => {
    mount(
      <>
        <TableArrayField
          fieldPath="rows"
          columns={[{ field: "note", label: "Note", type: "textarea" }]}
        />
        <ValueProbe path="rows" />
      </>,
      { initialValues: { rows: [{ note: "hello" }] } }
    );
    const area = container.querySelector("textarea");
    await type(area, "multi line");
    expect(probe()).toEqual([{ note: "multi line" }]);
  });

  it("textarea rows grow with the content (SUIR TextArea has no autoHeight)", () => {
    mount(
      <TableArrayField
        fieldPath="rows"
        columns={[{ field: "note", label: "Note", type: "textarea" }]}
      />,
      { initialValues: { rows: [{ note: "x".repeat(400) }] } }
    );
    const area = container.querySelector("textarea");
    expect(Number(area.getAttribute("rows"))).toBe(5);
    expect(area.getAttribute("autoheight")).toBeNull();
  });

  it("a short textarea cell stays one row high (table cells use a floor of 1)", () => {
    mount(
      <TableArrayField
        fieldPath="rows"
        columns={[{ field: "note", label: "Note", type: "textarea" }]}
      />,
      { initialValues: { rows: [{ note: "short" }] } }
    );
    expect(
      Number(container.querySelector("textarea").getAttribute("rows"))
    ).toBe(1);
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
        <ValueProbe path="rows" />
      </>,
      { initialValues: { rows: [{ id: "1GWD" }] } }
    );
    expect(container.textContent).toContain("link:1GWD");
    // render columns are read-only: no input for them
    expect(container.querySelectorAll("input")).toHaveLength(1);
  });

  it("takes column labels from the model when not passed (F7)", () => {
    setFakeUiModel({
      "steps.name": { label: "Step name from model" },
      "steps.description": { label: "Step description from model" },
    });
    mount(
      <>
        <TableArrayField
          fieldPath="steps"
          minItems={1}
          columns={[{ field: "name" }, { field: "description" }]}
        />
        <ValueProbe path="steps" />
      </>
    );
    expect(container.textContent).toContain("Step name from model");
    expect(container.textContent).toContain("Step description from model");
    // the cell input's aria-label uses the same resolved label
    expect(input("Step name from model")).not.toBeNull();
  });

  it("popup mode: no helptext under the table; columns with model help show a header icon", () => {
    setFakeUiModel({
      "steps.name": { helpText: "The name of the step" },
      "steps.description": { helpText: "What is done in this step" },
    });
    mount(
      <HelpModeProvider mode="popup">
        <TableArrayField
          fieldPath="steps"
          label="Preparation protocol"
          minItems={1}
          columns={PROTOCOL_COLUMNS}
        />
        <ValueProbe path="steps" />
      </HelpModeProvider>
    );
    // nothing renders help under the table
    expect(container.querySelector("label.helptext")).toBeNull();
    // one icon per column with model help, sitting in the header cells
    const icons = container.querySelectorAll('[aria-label^="Help"]');
    expect(icons.length).toBe(2);
    icons.forEach((icon) => {
      expect(icon.closest("th")).not.toBeNull();
    });
  });

  it("shows cell errors as red inputs with a pointing label (C1: from initialErrors)", () => {
    mount(protocol(), {
      initialValues: { steps: [{ name: "", description: "ok" }] },
      initialErrors: { steps: [{ name: "Missing data for required field." }] },
    });
    // SUI puts the .error class on the input's wrapper div
    expect(input("Name").closest(".ui.input").className).toContain("error");
    expect(
      container.querySelector(".ui.pointing.prompt.label").textContent
    ).toBe("Missing data for required field.");
  });

  it("keeps a cell error shown after editing another cell (C1: formik clears `errors`)", async () => {
    mount(protocol(), {
      initialValues: {
        steps: [
          { name: "", description: "ok" },
          { name: "second", description: "" },
        ],
      },
      initialErrors: { steps: [{ name: "Missing data for required field." }] },
    });
    // any setFieldValue clears `errors` in this formik setup; the label must
    // survive via the initialErrors fallback
    await type(inputs("Name")[1], "edited");
    const labels = [...container.querySelectorAll(".ui.pointing.prompt.label")];
    expect(labels.map((l) => l.textContent)).toContain(
      "Missing data for required field."
    );
  });

  it("shows a list-level error as a pointing prompt label under the table (F8)", () => {
    mount(protocol(), {
      initialValues: { steps: [{ name: "" }] },
      initialErrors: { steps: "Missing data for required field." },
    });
    const labels = [...container.querySelectorAll(".ui.pointing.prompt.label")];
    expect(labels.map((l) => l.textContent)).toContain(
      "Missing data for required field."
    );
  });

  it("shows a string error of a serialize-table item in the row (F8), not as a list label", () => {
    mount(databases(), {
      initialValues: { dbs: ["xyz:1"] },
      initialErrors: { dbs: ["Unknown database prefix."] },
    });
    const rowLabels = [
      ...container.querySelectorAll(".ui.pointing.prompt.label"),
    ].map((l) => l.textContent);
    expect(rowLabels).toEqual(["Unknown database prefix."]);
    // exactly one label (the row one); nothing duplicated at list level
    expect(rowLabels).toHaveLength(1);
  });

  it("supports an expandable editable row, auto-opened on errors (F2)", () => {
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
        <ValueProbe path="mods" />
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

  it("opens a row when NEW initialErrors arrive on the same mounted form (F2)", () => {
    const mods = (initialErrors) =>
      tree(
        <TableArrayField
          fieldPath="mods"
          columns={[{ field: "position", label: "Position", type: "number" }]}
          expandToggle={(row) => `${(row.steps ?? []).length} steps`}
          renderExpanded={(itemPath) => (
            <div data-testid={`expanded-${itemPath}`}>EXPANDED</div>
          )}
        />,
        {
          initialValues: { mods: [{ position: 3, steps: [{ name: "s" }] }] },
          initialErrors,
          enableReinitialize: true,
        }
      );
    mount(<div />); // just creates `container`
    render(mods({}));
    expect(byTestId(container)).toBeNull();
    // a failed save reinitializes the SAME mounted Formik with new errors
    render(mods({ mods: [{ steps: [{ name: "Required." }] }] }));
    expect(byTestId(container)).not.toBeNull();
  });

  it("an explicit toggle overrides the error auto-open", async () => {
    mount(
      <TableArrayField
        fieldPath="mods"
        columns={[{ field: "position", label: "Position", type: "number" }]}
        renderExpanded={(itemPath) => (
          <div data-testid={`expanded-${itemPath}`}>EXPANDED</div>
        )}
      />,
      {
        initialValues: { mods: [{ position: 3, steps: [{ name: "s" }] }] },
        initialErrors: { mods: [{ steps: [{ name: "Required." }] }] },
      }
    );
    expect(byTestId(container)).not.toBeNull(); // auto-opened by the error
    await click(buttons().find((b) => b.textContent.includes("Details")));
    expect(byTestId(container)).toBeNull(); // user closed it anyway
  });
});
