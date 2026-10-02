import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext, getIn } from "formik";
import {
  TextField,
  SelectField,
  ArrayField,
  TextAreaField,
} from "mbdb-react-invenio-forms";
import { HelpModeProvider } from "mbdb-semantic-ui-react";

// kept local: needs a StringArrayField stub the shared fake does not have,
// plus a constant model label/help with `required` keyed to a "req" prefix.
jest.mock("@js/oarepo_ui/forms", () => ({
  // fields.jsx wraps oarepo's StringArrayField; a passthrough stub is
  // enough here (no test renders it — the real one cannot load under Jest)
  StringArrayField: () => null,
  useFieldData: () => ({
    getFieldData: ({ fieldPath }) => ({
      label: "Model label",
      helpText: "Model help",
      required: fieldPath.startsWith("req"),
    }),
  }),
}));

// Shared harness helpers for the Formik-level error tests (the local `render`
// above has no unrelated-field/spy options). These use only Formik + ReactDOM,
// so they work under this file's own useFieldData mock too.
const { renderInForm, unmountForm, editUnrelatedField, typeInto } =
  jest.requireActual("@js/mbdb/forms/building-blocks/testUtils");

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

// Renders the form values as JSON so tests can assert the stored shape
// (that empty objects are pruned, numbers are numbers, …).
const ValuesProbe = () => {
  const { values } = useFormikContext();
  return <span data-testid="probe">{JSON.stringify(values)}</span>;
};

const render = (ui, { initialValues = {}, initialErrors = {} } = {}) => {
  act(() => {
    ReactDOM.render(
      <Formik
        initialValues={initialValues}
        initialErrors={initialErrors}
        onSubmit={() => {}}
      >
        <>
          {ui}
          <ValuesProbe />
        </>
      </Formik>,
      container
    );
  });
};

const helptexts = () => [...container.querySelectorAll("label.helptext")];

describe("wrapped fields", () => {
  it("TextField renders model label and exactly one help via FieldHelp", () => {
    render(<TextField fieldPath="name" />, { initialValues: { name: "abc" } });
    expect(container.querySelector("input").value).toBe("abc");
    expect(container.querySelector("label").textContent).toContain(
      "Model label"
    );
    expect(helptexts().length).toBe(1);
    expect(helptexts()[0].textContent).toBe("Model help");
  });

  it("explicit label/help win over the model", () => {
    render(<TextField fieldPath="name" label="Short" help="Short help" />);
    expect(container.querySelector("label").textContent).toContain("Short");
    expect(helptexts()[0].textContent).toBe("Short help");
  });

  it("TextField with neither model nor prop help renders no helptext", () => {
    render(<TextField fieldPath="name" help={null} />);
    expect(helptexts().length).toBe(0);
  });

  it("marks the field required when the model says so", () => {
    render(<TextField fieldPath="req.name" />);
    expect(container.querySelector(".field.required")).not.toBeNull();
  });

  it("removes the TextField key from the form data when cleared", () => {
    const Probe = () => {
      const { values } = useFormikContext();
      return (
        <span data-testid="probe">
          {getIn(values, "name") === undefined ? "absent" : "present"}
        </span>
      );
    };
    render(
      <>
        <TextField fieldPath="name" />
        <Probe />
      </>,
      { initialValues: { name: "abc" } }
    );
    const input = container.querySelector("input");
    input.value = "";
    act(() => {
      Simulate.change(input);
    });
    expect(container.querySelector('[data-testid="probe"]').textContent).toBe(
      "absent"
    );
  });

  it("SelectField selects an option and shows model help once", () => {
    // Note: options arrive already as Semantic option objects; string
    // expansion happens one layer up (the SelectField building block).
    render(
      <SelectField
        fieldPath="kind"
        options={[
          { key: "a", value: "a", text: "a" },
          { key: "b", value: "b", text: "b" },
        ]}
      />
    );
    const item = [...container.querySelectorAll(".menu .item")].find(
      (el) => el.textContent.trim() === "b"
    );
    act(() => {
      Simulate.click(item);
    });
    expect(container.querySelector(".dropdown .text").textContent).toContain(
      "b"
    );
    expect(helptexts().length).toBe(1);
  });

  it("ArrayField renders children per item and adds a row via its button", () => {
    render(
      <ArrayField fieldPath="items" label="Items" defaultNewValue={{}}>
        {({ arrayPath, indexPath }) => (
          <TextField fieldPath={`${arrayPath}.${indexPath}.name`} />
        )}
      </ArrayField>,
      { initialValues: { items: [{ name: "first" }] } }
    );
    expect(container.querySelectorAll("input").length).toBe(1);
    const add = [...container.querySelectorAll("button")].find((b) =>
      b.textContent.includes("Add new row")
    );
    act(() => {
      Simulate.click(add);
    });
    expect(container.querySelectorAll("input").length).toBe(2);
  });

  it("ArrayField renders the model help inside its field, not below Add", () => {
    render(
      <ArrayField fieldPath="items" label="Items" defaultNewValue={{}}>
        {({ arrayPath, indexPath }) => (
          <TextField fieldPath={`${arrayPath}.${indexPath}.name`} help={null} />
        )}
      </ArrayField>,
      { initialValues: { items: [{ name: "first" }] } }
    );
    // exactly one helptext: the array's own (child help suppressed)
    expect(helptexts().length).toBe(1);
    const helptext = helptexts()[0];
    expect(helptext.textContent).toBe("Model help");
    const add = [...container.querySelectorAll("button")].find((b) =>
      b.textContent.includes("Add new row")
    );
    // help renders inside the array's field, above the Add button
    expect(helptext.closest(".field").contains(add)).toBe(true);
    expect(
      helptext.compareDocumentPosition(add) & Node.DOCUMENT_POSITION_FOLLOWING
    ).toBeTruthy();
  });

  it("TextAreaField renders value, label and help", () => {
    render(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL" },
    });
    expect(container.querySelector("textarea").value).toBe("MKAL");
    expect(container.querySelector("label").textContent).toContain(
      "Model label"
    );
    expect(helptexts().length).toBe(1);
  });

  it("TextAreaField shows the error from initialErrors and keeps it after an unrelated edit", async () => {
    // the shared harness's unrelated field + edit: an edit elsewhere resets
    // formik `errors`, but the initialErrors fallback keeps the message while
    // the value at `seq` is unchanged (mergedErrorNode semantics)
    const local = renderInForm(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL", unrelatedTestField: "" },
      initialErrors: { seq: "Not a valid sequence." },
      withUnrelatedField: true,
    });
    try {
      expect(local.textContent).toContain("Not a valid sequence.");
      await editUnrelatedField(local);
      expect(local.textContent).toContain("Not a valid sequence.");
    } finally {
      unmountForm(local);
    }
  });

  it("TextAreaField error disappears once the textarea itself is edited", async () => {
    // a change at the error's own path makes the server error no longer apply
    const local = renderInForm(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL" },
      initialErrors: { seq: "Not a valid sequence." },
      withUnrelatedField: true,
    });
    try {
      expect(local.textContent).toContain("Not a valid sequence.");
      await typeInto(local.querySelector("textarea"), "MKALS");
      expect(local.textContent).not.toContain("Not a valid sequence.");
    } finally {
      unmountForm(local);
    }
  });

  it("TextField in popup mode shows no helptext, only the label icon", () => {
    render(
      <HelpModeProvider mode="popup">
        <TextField fieldPath="name" />
      </HelpModeProvider>
    );
    expect(container.querySelectorAll("label.helptext").length).toBe(0);
    expect(container.querySelectorAll('[aria-label^="Help"]').length).toBe(1);
  });

  it("a stray helpText prop cannot leak through to RIF (popup mode, prop order)", () => {
    // Regression: a caller that still passes the old prop name put helpText
    // into uiProps, which overrode the wrapper's suppression and made RIF
    // draw its own helptext label under the input, outside HelpMode.
    render(
      <HelpModeProvider mode="popup">
        <TextField fieldPath="name" helpText="stray old-prop help" />
      </HelpModeProvider>
    );
    expect(container.querySelectorAll("label.helptext").length).toBe(0);
    expect(container.textContent).not.toContain("stray old-prop help");
  });

  it("a stray helpText prop does not reach the DOM textarea", () => {
    render(<TextAreaField fieldPath="seq" helpText="stray old-prop help" />);
    const textarea = container.querySelector("textarea");
    expect(textarea.getAttribute("helptext")).toBeNull();
    expect(container.textContent).not.toContain("stray old-prop help");
  });

  it("clearing the last field of an inline object removes the object key (C15)", () => {
    const initialValues = {
      entity: { name: "x", location: { altitude: 250 } },
    };
    render(<TextField fieldPath="entity.location.altitude" />, {
      initialValues,
    });
    expect(container.querySelector("input").value).toBe("250");
    const input = container.querySelector("input");
    input.value = "";
    act(() => {
      Simulate.change(input);
    });
    // the object key `location` must be gone, not left as an empty {}
    const probe = container.querySelector('[data-testid="probe"]');
    expect(JSON.parse(probe.textContent)).toEqual({
      entity: { name: "x" },
    });
  });
});
