import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext } from "formik";
import {
  countErrors,
  hasError,
  errorMessages,
  isEmptyValue,
  hasData,
  useFieldErrors,
} from "./errors";

describe("errors helpers", () => {
  const errors = {
    metadata: {
      name: "Missing data for required field.",
      list: [
        { id: "Not a valid identifier.", title: "" },
        null,
        { nested: { deep: ["Too short.", "Too short."] } },
      ],
      server: { message: "Invalid value.", severity: "error" },
      serverList: [{ message: "Server says no." }, { plain: true }],
      info: { message: "Just info.", severity: "info" },
      warning: { message: "Careful.", severity: "warning" },
    },
  };

  it("counts leaf error strings under a path", () => {
    expect(countErrors(errors, "metadata.name")).toBe(1);
    // F16: duplicates count (two "Too short." = 2)
    expect(countErrors(errors, "metadata.list")).toBe(3);
  });

  it("returns 0 for missing paths and empty structures", () => {
    expect(countErrors(errors, "metadata.absent")).toBe(0);
    expect(countErrors(errors, "nowhere.at.all")).toBe(0);
    expect(countErrors({}, "metadata")).toBe(0);
  });

  it("treats a {message, severity} object as one error, also inside arrays", () => {
    expect(countErrors(errors, "metadata.server")).toBe(1);
    expect(hasError(errors, "metadata.server")).toBe(true);
    expect(hasError(errors, "metadata.absent")).toBe(false);
    // F16: {message} objects inside arrays count via their message; an object
    // without a message contributes nothing
    expect(countErrors(errors, "metadata.serverList")).toBe(1);
    expect(errorMessages(errors, "metadata.serverList")).toEqual([
      "Server says no.",
    ]);
  });

  it("ignores info/warning severities (F15)", () => {
    expect(countErrors(errors, "metadata.info")).toBe(0);
    expect(countErrors(errors, "metadata.warning")).toBe(0);
    expect(hasError(errors, "metadata.info")).toBe(false);
    expect(errorMessages(errors, "metadata.info")).toEqual([]);
    // a {message} object without severity counts as an error
    expect(countErrors({ a: [{ message: "No severity." }] }, "a")).toBe(1);
  });

  it("joins unique messages (F16: display is deduped)", () => {
    expect(errorMessages(errors, "metadata.list")).toEqual([
      "Not a valid identifier.",
      "Too short.",
    ]);
    expect(errorMessages(errors, "metadata.absent")).toEqual([]);
  });

  it("counts every leaf for the badge but keeps severity filtering", () => {
    // name(1) + list(3) + server(1) + serverList(1); info/warning excluded
    expect(countErrors(errors, "metadata")).toBe(6);
  });

  it("detects user data (0 and false count as data)", () => {
    expect(isEmptyValue(undefined)).toBe(true);
    expect(isEmptyValue("")).toBe(true);
    expect(isEmptyValue([])).toBe(true);
    expect(isEmptyValue({ a: "", b: [] })).toBe(true);
    expect(hasData(0)).toBe(true);
    expect(hasData(false)).toBe(true);
    expect(hasData({ a: "x" })).toBe(true);
    expect(hasData([{ id: null }])).toBe(false);
  });
});

// ---- useFieldErrors (C1: errors, else initialErrors while unchanged) -------

const Probe = ({ path }) => {
  const { count, messages, hasError } = useFieldErrors(path);
  return (
    <span data-testid={`probe-${path}`}>
      {JSON.stringify({ count, messages, hasError })}
    </span>
  );
};
Probe.propTypes = { path: PropTypes.string.isRequired };

const SetButton = ({ path, value, testId }) => {
  const { setFieldValue } = useFormikContext();
  return (
    <button
      type="button"
      data-testid={testId}
      onClick={() => setFieldValue(path, value)}
    />
  );
};
SetButton.propTypes = {
  path: PropTypes.string.isRequired,
  value: PropTypes.any,
  testId: PropTypes.string.isRequired,
};

const ErrorButton = ({ path, value, testId }) => {
  const { setFieldError } = useFormikContext();
  return (
    <button
      type="button"
      data-testid={testId}
      onClick={() => setFieldError(path, value)}
    />
  );
};
ErrorButton.propTypes = {
  path: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  testId: PropTypes.string.isRequired,
};

let container;

const mount = (ui, { initialValues = {}, initialErrors = {} } = {}) => {
  container = document.createElement("div");
  document.body.appendChild(container);
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

afterEach(() => {
  if (!container) return;
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
  container = null;
});

const probe = (path) =>
  JSON.parse(
    container.querySelector(`[data-testid="probe-${path}"]`).textContent
  );
// formik's SET_ERRORS lands in a promise: flush it before asserting
const click = async (testId) => {
  await act(async () => {
    Simulate.click(container.querySelector(`[data-testid="${testId}"]`));
  });
};

describe("useFieldErrors", () => {
  it("shows initialErrors while the value is unchanged", () => {
    mount(<Probe path="steps.0.name" />, {
      initialValues: { steps: [{ name: "" }] },
      initialErrors: { steps: [{ name: "Missing data for required field." }] },
    });
    expect(probe("steps.0.name")).toEqual({
      count: 1,
      messages: ["Missing data for required field."],
      hasError: true,
    });
  });

  it("keeps the initial error after an unrelated edit clears `errors` (C1)", async () => {
    // Empirical premise of C1 (verified against formik 2.4.9 here): with no
    // validate function, any setFieldValue runs validateFormWithHighPriority,
    // which dispatches SET_ERRORS {} — bare `errors` lose everything; only
    // `initialErrors` survive.
    mount(
      <>
        <Probe path="steps.0.name" />
        <SetButton path="other" value="x" testId="edit-other" />
      </>,
      {
        initialValues: { steps: [{ name: "" }], other: "" },
        initialErrors: {
          steps: [{ name: "Missing data for required field." }],
        },
      }
    );
    await click("edit-other");
    expect(probe("steps.0.name")).toEqual({
      count: 1,
      messages: ["Missing data for required field."],
      hasError: true,
    });
  });

  it("drops the initial fallback once its own value is edited", async () => {
    mount(
      <>
        <Probe path="steps.0.name" />
        <SetButton path="steps.0.name" value="edited" testId="edit-name" />
      </>,
      {
        initialValues: { steps: [{ name: "" }] },
        initialErrors: {
          steps: [{ name: "Missing data for required field." }],
        },
      }
    );
    await click("edit-name");
    expect(probe("steps.0.name")).toEqual({
      count: 0,
      messages: [],
      hasError: false,
    });
  });

  it("keeps the fallback for a sibling path when another path is edited", async () => {
    mount(
      <>
        <Probe path="steps.1.name" />
        <SetButton path="steps.0.name" value="edited" testId="edit-first" />
      </>,
      {
        initialValues: { steps: [{ name: "a" }, { name: "b" }] },
        initialErrors: {
          steps: [{ name: "First is bad." }, { name: "Second is bad." }],
        },
      }
    );
    await click("edit-first");
    expect(probe("steps.1.name")).toEqual({
      count: 1,
      messages: ["Second is bad."],
      hasError: true,
    });
  });

  it("prefers live errors over initialErrors when both exist", async () => {
    mount(
      <>
        <Probe path="steps" />
        <ErrorButton path="steps" value="Live error wins." testId="set-error" />
      </>,
      {
        initialValues: { steps: [{ name: "a" }] },
        initialErrors: { steps: "Shorter than minimum length 1." },
      }
    );
    await click("set-error");
    expect(probe("steps")).toEqual({
      count: 1,
      messages: ["Live error wins."],
      hasError: true,
    });
  });
});
