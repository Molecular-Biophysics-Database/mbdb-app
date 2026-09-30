import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { DiscriminatorField } from "./DiscriminatorField";

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
  document
    .querySelectorAll(".ui.modals, .ui.dimmer")
    .forEach((el) => el.remove());
});

const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);
const modal = () => document.body.querySelector(".ui.modal");
const button = (label) =>
  [...container.querySelectorAll("button")].find(
    (b) => b.textContent === label
  );
const ENTITY_TYPES = [
  "Polymer",
  "Chemical",
  "Molecular assembly",
  "Complex substance of biological origin",
  "Other",
];

// 5 entity types default to the dropdown variant; buttons tested explicitly
const typeField = (props = {}) => (
  <>
    <DiscriminatorField
      objectPath="o"
      field="type"
      options={ENTITY_TYPES}
      variant="buttons"
      keep={["id"]}
      {...props}
    />
    <Probe path="o" />
  </>
);

describe("DiscriminatorField", () => {
  it("buttons variant: marks the current option primary and changes without confirm when no other data", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
    });
    expect(button("Polymer").className).toContain("primary");
    expect(button("Chemical").className).not.toContain("primary");

    act(() => Simulate.click(button("Chemical")));
    expect(probe()).toEqual({ id: "e1", type: "Chemical" });
    expect(modal()).toBeNull(); // nothing lost, no confirm asked
  });

  it("does nothing when the current option is clicked again", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer" } },
    });
    act(() => Simulate.click(button("Polymer")));
    expect(probe()).toEqual({ id: "e1", type: "Polymer" });
    expect(modal()).toBeNull();
  });

  it("asks before changing when other data would be lost, and keeps only keep keys", () => {
    mount(typeField(), {
      initialValues: {
        o: { id: "e1", type: "Polymer", name: "Lysozyme", sequence: "ABC" },
      },
    });
    act(() => Simulate.click(button("Chemical")));
    const m = modal();
    expect(m).not.toBeNull();
    expect(m.textContent).toContain('Change o.type to "Chemical"?');
    expect(m.textContent).toContain(
      'The data entered for "Polymer" will be removed.'
    );
    expect(probe()).toEqual({
      id: "e1",
      type: "Polymer",
      name: "Lysozyme",
      sequence: "ABC",
    });

    const changeBtn = [...m.querySelectorAll("button")].find(
      (b) => b.textContent === "Change"
    );
    act(() => Simulate.click(changeBtn));
    expect(probe()).toEqual({ id: "e1", type: "Chemical" });
  });

  it("cancel of the confirm leaves the object untouched", () => {
    mount(typeField(), {
      initialValues: { o: { type: "Polymer", name: "Lysozyme" } },
    });
    act(() => Simulate.click(button("Chemical")));
    const cancelBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Cancel"
    );
    act(() => Simulate.click(cancelBtn));
    expect(probe()).toEqual({ type: "Polymer", name: "Lysozyme" });
  });

  it("dropping extra keys beyond keep also guarded: id kept, others dropped", () => {
    mount(typeField(), {
      initialValues: { o: { id: "e1", type: "Polymer", name: "X" } },
    });
    act(() => Simulate.click(button("Other")));
    const changeBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Change"
    );
    act(() => Simulate.click(changeBtn));
    expect(probe()).toEqual({ id: "e1", type: "Other" });
  });

  it("allowUnset adds an unset button that clears the whole object", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="assessed"
          options={["Yes", "No"]}
          allowUnset
          unsetLabel="Not specified"
        />
        <Probe path="o" />
      </>,
      { initialValues: { o: { assessed: "Yes", method: "SDS-PAGE" } } }
    );
    expect(button("Yes").className).toContain("primary");
    act(() => Simulate.click(button("Not specified")));
    expect(modal()).not.toBeNull(); // data present: confirm first
    const removeBtn = [...modal().querySelectorAll("button")].find(
      (b) => b.textContent === "Remove"
    );
    act(() => Simulate.click(removeBtn));
    expect(probe()).toEqual(null);
  });

  it("unset is active when the object is absent", () => {
    mount(
      <>
        <DiscriminatorField
          objectPath="o"
          field="assessed"
          options={["Yes", "No"]}
          allowUnset
          unsetLabel="Not specified"
        />
        <Probe path="o" />
      </>,
      { initialValues: {} }
    );
    expect(button("Not specified").className).toContain("primary");
    expect(button("Yes").className).not.toContain("primary");
    // choosing Yes from unset: no data to lose → no confirm
    act(() => Simulate.click(button("Yes")));
    expect(probe()).toEqual({ assessed: "Yes" });
    expect(modal()).toBeNull();
  });

  it("dropdown variant renders a dropdown and changes value", () => {
    mount(
      typeField({ variant: "dropdown", options: ["Polymer", "Chemical"] }),
      {
        initialValues: { o: { id: "e1", type: "Polymer" } },
      }
    );
    const dropdown = container.querySelector(".ui.dropdown");
    expect(dropdown).not.toBeNull();
    act(() => Simulate.click(dropdown));
    const item = [...dropdown.querySelectorAll(".menu .item")].find(
      (el) => el.textContent === "Chemical"
    );
    act(() => Simulate.click(item));
    expect(probe()).toEqual({ id: "e1", type: "Chemical" });
  });
});
