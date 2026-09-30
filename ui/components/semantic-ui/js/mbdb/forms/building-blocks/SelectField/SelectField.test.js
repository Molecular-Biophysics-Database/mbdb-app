import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import { SelectField } from "./SelectField";

jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: () => ({
      label: undefined,
      helpText: undefined,
      required: undefined,
    }),
  }),
}));

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const v = getIn(values, path);
  return <span data-testid="value">{v === undefined ? "-" : String(v)}</span>;
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
const clickItem = (text) => {
  const item = [...container.querySelectorAll(".menu .item")].find(
    (el) => el.textContent.trim() === text
  );
  expect(item).toBeDefined();
  act(() => {
    Simulate.click(item);
  });
};

describe("SelectField", () => {
  it("selects a string option and stores the string value", () => {
    render(
      <>
        <SelectField
          fieldPath="pt"
          label="Polymer type"
          options={["polypeptide(L)", "polypeptide(D)"]}
        />
        <Probe path="pt" />
      </>
    );
    clickItem("polypeptide(D)");
    expect(byTestId("value").textContent).toBe("polypeptide(D)");
  });

  it("is clearable when optional and not clearable when required", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "a" },
    });
    expect(container.querySelector(".dropdown i.icon.clear")).not.toBeNull();

    render(<SelectField fieldPath="pt" required options={["a", "b"]} />, {
      initialValues: { pt: "a" },
    });
    expect(container.querySelector(".dropdown i.icon.clear")).toBeNull();
  });

  it("removes the key when cleared via the clear icon", () => {
    render(
      <>
        <SelectField fieldPath="pt" options={["a", "b"]} />
        <Probe path="pt" />
      </>,
      { initialValues: { pt: "a" } }
    );
    const clearIcon = container.querySelector(".dropdown i.icon.clear");
    act(() => {
      Simulate.click(clearIcon);
    });
    expect(byTestId("value").textContent).toBe("-");
  });

  it("keeps an unknown stored value visible and marks it with a label", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "old-value" },
    });
    // RIF ensureSelectedValuesInOptions keeps it displayed
    expect(container.querySelector(".dropdown .text").textContent).toContain(
      "old-value"
    );
    expect(container.textContent).toContain("Unknown value");
  });

  it("lets a known value through without the Unknown value label", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "a" },
    });
    expect(container.textContent).not.toContain("Unknown value");
  });

  it("shows the error from initialErrors", () => {
    render(<SelectField fieldPath="pt" options={["a", "b"]} />, {
      initialValues: { pt: "a" },
      initialErrors: { pt: "Missing data for required field." },
    });
    expect(container.textContent).toContain("Missing data for required field.");
  });
});
