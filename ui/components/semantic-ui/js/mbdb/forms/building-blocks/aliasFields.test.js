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

  it("explicit label/helpText win over the model", () => {
    render(<TextField fieldPath="name" label="Short" helpText="Short help" />);
    expect(container.querySelector("label").textContent).toContain("Short");
    expect(helptexts()[0].textContent).toBe("Short help");
  });

  it("TextField with neither model nor prop help renders no helptext", () => {
    render(<TextField fieldPath="name" helpText={null} />);
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
          <TextField
            fieldPath={`${arrayPath}.${indexPath}.name`}
            helpText={null}
          />
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

  it("TextAreaField shows the error from initialErrors", () => {
    render(<TextAreaField fieldPath="seq" />, {
      initialValues: { seq: "MKAL" },
      initialErrors: { seq: "Not a valid sequence." },
    });
    expect(container.textContent).toContain("Not a valid sequence.");
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
});
