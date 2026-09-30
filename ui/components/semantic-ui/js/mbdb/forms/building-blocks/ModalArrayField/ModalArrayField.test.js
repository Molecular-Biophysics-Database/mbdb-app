import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { Input } from "mbdb-semantic-ui-react";
import { ModalArrayField } from "./ModalArrayField";

jest.mock("@js/oarepo_ui/forms", () => ({
  FormConfigProvider: ({ children }) => children,
  FieldDataProvider: ({ children }) => children,
  useFieldData: () => ({
    getFieldData: ({ fieldPath }) => ({ label: fieldPath, helpText: null }),
  }),
}));

// jsdom has no WebCrypto in insecure contexts; the app needs only https/localhost.
let mockUUID = "uuid-1";
jest.mock("../randomUUID", () => ({ randomUUID: () => mockUUID }));
const { FormConfigProvider, FieldDataProvider } = jest.requireMock(
  "@js/oarepo_ui/forms"
);

let container;

const ENTITIES = "entities";
const COLUMNS = [
  { title: "Name", value: (v) => v.name },
  { title: "Type", value: (v) => v.type },
];

// modal body: an input bound to the item's name through setFieldValue
const NameForm = ({ itemPath }) => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <Input
      aria-label="Entity name"
      value={getIn(values, `${itemPath}.name`) ?? ""}
      onChange={(e) => setFieldValue(`${itemPath}.name`, e.target.value)}
    />
  );
};
NameForm.propTypes = {
  itemPath: PropTypes.string.isRequired,
};

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
  document
    .querySelectorAll(".ui.modals, .ui.dimmer")
    .forEach((el) => el.remove());
});

const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);
const modal = () => document.body.querySelector(".ui.modal");
const modalButton = (label) =>
  [...modal().querySelectorAll("button")].find((b) => b.textContent === label);
const entities = (props = {}) => (
  <>
    <ModalArrayField
      fieldPath={ENTITIES}
      label="Entities of interest"
      required
      minItems={1}
      itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
      columns={COLUMNS}
      newItemOptions={[
        { label: "Polymer", value: { type: "Polymer" } },
        { label: "Chemical", value: { type: "Chemical" } },
      ]}
      renderForm={(itemPath) => <NameForm itemPath={itemPath} />}
      {...props}
    />
    <Probe path={ENTITIES} />
  </>
);

describe("ModalArrayField", () => {
  it("shows the empty state with the add control", () => {
    mount(entities());
    expect(container.textContent).toContain("No items yet");
    expect(container.textContent).toContain("Entities of interest");
    // several options: a dropdown button, not a plain one
    expect(container.querySelector(".ui.dropdown.button")).not.toBeNull();
  });

  it("renders a summary row per item with column values", () => {
    mount(entities(), {
      initialValues: {
        entities: [
          { id: "e1", type: "Polymer", name: "Lysozyme" },
          { id: "e2", type: "Chemical", name: "NaCl" },
        ],
      },
    });
    expect(container.textContent).toContain("Lysozyme");
    expect(container.textContent).toContain("Polymer");
    expect(container.textContent).toContain("NaCl");
    // minItems=1: first row has no remove button
    expect(
      container.querySelector('button[aria-label="Remove entity: Lysozyme"]')
    ).toBeNull();
    expect(
      container.querySelector('button[aria-label="Remove entity: NaCl"]')
    ).not.toBeNull();
  });

  it("adds an item through the dropdown, seeds it, gives it an id with withIds, and opens its modal", () => {
    mockUUID = "uuid-1";
    mount(entities({ withIds: true }));
    const dropdown = container.querySelector(".ui.dropdown");
    act(() => Simulate.click(dropdown));
    const item = [...document.querySelectorAll(".menu .item")].find(
      (el) => el.textContent === "Polymer"
    );
    act(() => Simulate.click(item));

    const added = probe()[0];
    expect(added.type).toBe("Polymer");
    expect(added.id).toBe("uuid-1");
    expect(modal()).not.toBeNull();
    expect(modal().textContent).toContain("Edit entity: new");
  });

  it("Cancel on a just-added item removes it", () => {
    mount(
      entities({
        newItemOptions: [{ label: null, value: { type: "Polymer" } }],
      })
    );
    // single option: plain add button
    const add = [...container.querySelectorAll("button")].find((b) =>
      b.textContent.includes("Add")
    );
    act(() => Simulate.click(add));
    expect(probe()).toEqual([{ type: "Polymer" }]);
    expect(modal()).not.toBeNull();

    act(() => Simulate.click(modalButton("Cancel")));
    expect(modal()).toBeNull();
    expect(probe()).toEqual([]); // empty array; the serializer drops it
  });

  it("Cancel on an existing item restores the snapshot; Done keeps the edits", () => {
    mount(entities(), {
      initialValues: { entities: [{ type: "Polymer", name: "Lysozyme" }] },
    });
    const editBtn = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "Edit"
    );
    act(() => Simulate.click(editBtn));
    expect(modal().textContent).toContain("Edit entity: Lysozyme");

    const input = modal().querySelector('input[aria-label="Entity name"]');
    input.value = "Changed";
    act(() => Simulate.change(input));
    expect(probe()).toEqual([{ type: "Polymer", name: "Changed" }]);

    act(() => Simulate.click(modalButton("Cancel")));
    expect(probe()).toEqual([{ type: "Polymer", name: "Lysozyme" }]);

    // edit again, this time Done keeps the change
    act(() =>
      Simulate.click(
        [...container.querySelectorAll("button")].find(
          (b) => b.textContent === "Edit"
        )
      )
    );
    const input2 = modal().querySelector('input[aria-label="Entity name"]');
    input2.value = "Kept";
    act(() => Simulate.change(input2));
    act(() => Simulate.click(modalButton("Done")));
    expect(modal()).toBeNull();
    expect(probe()).toEqual([{ type: "Polymer", name: "Kept" }]);
  });

  it("opens the modal from the error badge", () => {
    mount(entities({ minItems: 0 }), {
      initialValues: { entities: [{ type: "Chemical" }] },
      initialErrors: {
        entities: [{ name: "Missing data for required field." }],
      },
    });
    const badge = container.querySelector(".ui.red.label");
    expect(badge.textContent).toBe("1 error");
    act(() => Simulate.click(badge));
    expect(modal()).not.toBeNull();
  });

  it("shows the detail view when detailGroups are given", () => {
    mount(
      entities({
        detailGroups: [{ title: "Origin", fields: ["source_organism"] }],
        minItems: 0,
      }),
      {
        initialValues: {
          entities: [
            { type: "Polymer", name: "Lysozyme", source_organism: "ecoli" },
          ],
        },
      }
    );
    const toggle = container.querySelector(
      'button[aria-label^="Show details of entity"]'
    );
    expect(toggle).not.toBeNull();
    act(() => Simulate.click(toggle));
    expect(container.textContent).toContain("ecoli");
    expect(container.querySelector("tr.mbdb-details")).not.toBeNull();
  });
});
