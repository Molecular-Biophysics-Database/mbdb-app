import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { ValueUnitField } from "./ValueUnitField";

jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: () => ({
      label: undefined,
      helpText: undefined,
      required: undefined,
    }),
  }),
}));

jest.mock("mbdb-semantic-ui-react", () => ({
  ...jest.requireActual("mbdb-semantic-ui-react"),
  ...jest.requireActual("mbdb-semantic-ui-react/FieldHelp"),
}));

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const v = getIn(values, path);
  return (
    <span data-testid="value">
      {v === undefined ? "null" : JSON.stringify(v)}
    </span>
  );
};

Probe.propTypes = {
  path: PropTypes.string,
};

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const render = (ui, { initialValues = {}, initialErrors = {} } = {}) => {
  act(() => {
    ReactDOM.render(
      <Formik
        initialValues={initialValues}
        initialErrors={initialErrors}
        onSubmit={() => {}}
      >
        {ui}
      </Formik>,
      container
    );
  });
};

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);
const numberInput = () => container.querySelector('input[type="number"]');
const typeValue = (value) => {
  numberInput().value = value;
  act(() => {
    Simulate.change(numberInput());
  });
};
const clickUnit = (text) => {
  const item = [...container.querySelectorAll(".dropdown .menu .item")].find(
    (el) => el.textContent.trim() === text
  );
  expect(item).toBeDefined();
  act(() => {
    Simulate.click(item);
  });
};

const field = (
  <>
    <ValueUnitField
      fieldPath="mw"
      label="Molecular weight"
      units={["Da", "kDa", "MDa"]}
      defaultUnit="kDa"
      helpText="The molecular weight of the polymer"
    />
    <Probe path="mw" />
  </>
);

describe("ValueUnitField", () => {
  it("shows the default unit in the dropdown without writing it", () => {
    render(field);
    expect(container.querySelector(".dropdown .text").textContent).toBe("kDa");
    expect(byTestId("value").textContent).toBe("null");
    expect(container.querySelector("label.helptext").textContent).toBe(
      "The molecular weight of the polymer"
    );
  });

  it("writes value as a number together with the default unit", () => {
    render(field);
    typeValue("14305.5");
    expect(byTestId("value").textContent).toBe(
      '{"value":14305.5,"unit":"kDa"}'
    );
  });

  it("keeps an explicitly picked unit when the value is empty, writes it with the value", () => {
    render(field);
    clickUnit("Da");
    expect(byTestId("value").textContent).toBe('{"unit":"Da"}');
    typeValue("10");
    expect(byTestId("value").textContent).toBe('{"value":10,"unit":"Da"}');
  });

  it("removes the whole object when the value is cleared (default unit)", () => {
    render(field, {
      initialValues: { mw: { value: 14305.5, unit: "kDa" } },
    });
    typeValue("");
    expect(byTestId("value").textContent).toBe("null");
  });

  it("keeps an explicit non-default unit when the value is cleared", () => {
    render(field, {
      initialValues: { mw: { value: 14305.5, unit: "Da" } },
    });
    typeValue("");
    expect(byTestId("value").textContent).toBe('{"unit":"Da"}');
  });

  it("shows errors on value or unit under the control", () => {
    render(field, {
      initialValues: { mw: { unit: "kDa" } },
      initialErrors: { mw: { value: "Missing data for required field." } },
    });
    expect(container.textContent).toContain("Missing data for required field.");
    expect(container.querySelector(".field.error")).not.toBeNull();
  });
});
