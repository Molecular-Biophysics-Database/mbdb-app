import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { Input } from "mbdb-semantic-ui-react";
import { ModalObjectField } from "./ModalObjectField";

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

const TemperatureForm = ({ fieldPath }) => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <Input
      aria-label="Temperature"
      value={getIn(values, `${fieldPath}.temperature`) ?? ""}
      onChange={(e) =>
        setFieldValue(`${fieldPath}.temperature`, e.target.value)
      }
    />
  );
};
TemperatureForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
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
const btn = (label) =>
  [...container.querySelectorAll("button")].find((b) =>
    b.textContent.includes(label)
  );

const storage = (props = {}) => (
  <>
    <ModalObjectField
      fieldPath="storage"
      label="Storage"
      summary={(v) => [v.temperature, v.duration].filter(Boolean).join(", ")}
      initialValue={{ temperature: "4 °C" }}
      renderForm={(p) => <TemperatureForm fieldPath={p} />}
      {...props}
    />
    <Probe path="storage" />
  </>
);

describe("ModalObjectField", () => {
  it("shows the Add button when absent and no summary", () => {
    mount(storage());
    expect(container.textContent).toContain("Storage");
    expect(container.textContent).toContain("Add Storage");
    expect(container.textContent).not.toContain("Edit");
  });

  it("Add sets the initial value, opens the modal; Cancel resets to undefined", () => {
    mount(storage());
    act(() => Simulate.click(btn("Add Storage")));
    expect(probe()).toEqual({ temperature: "4 °C" });
    expect(modal()).not.toBeNull();

    const input = modal().querySelector('input[aria-label="Temperature"]');
    input.value = "−80 °C";
    act(() => Simulate.change(input));
    act(() => Simulate.click(modalButton("Cancel")));
    expect(modal()).toBeNull();
    expect(probe()).toEqual(null);
  });

  it("shows the summary row when present and Edits through the modal", () => {
    mount(storage(), {
      initialValues: { storage: { temperature: "4 °C", duration: "3 days" } },
    });
    expect(container.textContent).toContain("4 °C, 3 days");

    act(() => Simulate.click(btn("Edit")));
    const input = modal().querySelector('input[aria-label="Temperature"]');
    input.value = "−20 °C";
    act(() => Simulate.change(input));
    act(() => Simulate.click(modalButton("Done")));
    expect(probe()).toEqual({ temperature: "−20 °C", duration: "3 days" });
  });

  it("removes after confirmation when data is present; no confirm for empty", () => {
    mount(storage(), { initialValues: { storage: {} } });
    // empty object: no confirm, removed immediately
    act(() =>
      Simulate.click(
        container.querySelector('button[aria-label="Remove Storage"]')
      )
    );
    expect(probe()).toEqual(null);

    // with data: confirm first
    mount(storage(), {
      initialValues: { storage: { temperature: "4 °C" } },
    });
    act(() =>
      Simulate.click(
        container.querySelector('button[aria-label="Remove Storage"]')
      )
    );
    const confirmModal = modal();
    expect(confirmModal).not.toBeNull();
    expect(confirmModal.textContent).toContain("Remove Storage?");
    const confirmBtn = [...confirmModal.querySelectorAll("button")].find(
      (b) => b.textContent === "Remove"
    );
    act(() => Simulate.click(confirmBtn));
    expect(probe()).toEqual(null);
  });

  it("required + absent shows 'Not filled in' and no remove button", () => {
    mount(storage({ required: true }));
    expect(container.textContent).toContain("Not filled in");

    // present + required: no remove
    mount(storage({ required: true }), {
      initialValues: { storage: { temperature: "4 °C" } },
    });
    expect(
      container.querySelector('button[aria-label="Remove Storage"]')
    ).toBeNull();
  });
});
