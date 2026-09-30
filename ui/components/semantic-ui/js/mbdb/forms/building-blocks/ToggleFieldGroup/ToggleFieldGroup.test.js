import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { ToggleFieldGroup } from "./ToggleFieldGroup";

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
const checkbox = () => container.querySelector('input[type="checkbox"]');
// SUI Checkbox reads the native checked flag on change
const toggle = () => {
  checkbox().checked = !checkbox().checked;
  act(() => Simulate.change(checkbox()));
};
const group = (props = {}) => (
  <>
    <ToggleFieldGroup
      fieldPath="identity.by_intact_mass"
      label="By intact mass"
      initialValue={{ method: "Mass spectrometry" }}
      {...props}
    >
      <span data-testid="body">FIELDS</span>
    </ToggleFieldGroup>
    <Probe path="identity" />
  </>
);

describe("ToggleFieldGroup", () => {
  it("is unchecked when the value is undefined and hides the body", () => {
    mount(group());
    expect(checkbox().checked).toBe(false);
    expect(container.querySelector('[data-testid="body"]')).toBeNull();
    expect(container.textContent).toContain("By intact mass");
  });

  it("checking writes initialValue and shows the indented body", () => {
    mount(group());
    toggle();
    expect(probe()).toEqual({
      by_intact_mass: { method: "Mass spectrometry" },
    });
    const body = container.querySelector('[data-testid="body"]');
    expect(body).not.toBeNull();
    expect(body.closest(".mbdb-indent")).not.toBeNull();
  });

  it("is checked when a value exists", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: { deviation: "0.5" } } },
    });
    expect(checkbox().checked).toBe(true);
    expect(container.querySelector('[data-testid="body"]')).not.toBeNull();
  });

  it("unchecking an empty object removes it without confirmation", () => {
    mount(group(), { initialValues: { identity: { by_intact_mass: {} } } });
    toggle();
    expect(probe()).toEqual({});
    expect(document.body.querySelector(".ui.modal")).toBeNull();
  });

  it("unchecking with data asks for confirmation, then removes", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: { deviation: "0.5" } } },
    });
    toggle();
    const modal = document.body.querySelector(".ui.modal");
    expect(modal).not.toBeNull();
    expect(modal.textContent).toContain("Remove By intact mass?");
    expect(probe()).toEqual({ by_intact_mass: { deviation: "0.5" } }); // still there

    const cancelBtn = [...modal.querySelectorAll("button")].find(
      (b) => b.textContent === "Cancel"
    );
    act(() => Simulate.click(cancelBtn));
    expect(probe()).toEqual({ by_intact_mass: { deviation: "0.5" } });

    toggle();
    const removeBtn = [
      ...document.body.querySelector(".ui.modal").querySelectorAll("button"),
    ].find((b) => b.textContent === "Remove");
    act(() => Simulate.click(removeBtn));
    expect(probe()).toEqual({});
  });

  it("marks the header on errors under fieldPath", () => {
    mount(group(), {
      initialValues: { identity: { by_intact_mass: {} } },
      initialErrors: { identity: { by_intact_mass: { method: "Required." } } },
    });
    expect(container.querySelector(".field.error")).not.toBeNull();
  });
});
