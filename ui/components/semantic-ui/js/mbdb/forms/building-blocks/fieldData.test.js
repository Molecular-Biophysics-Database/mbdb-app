import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { useModelFieldData } from "./fieldData";

// The real "@js/oarepo_ui/forms" index cannot load under Jest
// (sanitize-html -> postcss is ESM), and in the real app it reads the
// model from a context; here the model data is mocked directly.
// The special "missing" prefix simulates oarepo's getFieldData fallback:
// no ui_model entry, so the raw toModelPath string comes back as label
// (and helpText is null).
// kept local: this tests useModelFieldData AGAINST a fake that mimics oarepo's
// real no-entry fallback (and throws on an undefined path), behaviour the
// shared testUtils fake intentionally does not model — it is the subject
// under test, not just a dependency.
jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: ({ fieldPath }) => {
      // Mirrors oarepo's real behaviour: toModelPath does path.split, so an
      // undefined path throws. useModelFieldData must never call it then.
      if (fieldPath == null) throw new Error("path.split of undefined");
      return fieldPath.startsWith("missing")
        ? {
            label: `children.${fieldPath.split(".").join(".children.")}`,
            helpText: null,
            required: undefined,
          }
        : {
            label: "Model label",
            helpText: "Model help",
            required: true,
          };
    },
  }),
}));

const Probe = ({ path, overrides }) => {
  const data = useModelFieldData(path, overrides);
  return (
    <div>
      <span data-testid="label">{String(data.label)}</span>
      <span data-testid="helpText">{String(data.helpText)}</span>
      <span data-testid="required">{String(data.required)}</span>
    </div>
  );
};

Probe.propTypes = {
  path: PropTypes.string,
  overrides: PropTypes.object,
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

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);

describe("useModelFieldData", () => {
  it("uses no model lookup when fieldPath is undefined (FieldGroup without a path)", () => {
    // Regression: oarepo's getFieldData crashes on an undefined path
    // (toModelPath does path.split). The hook must not call it.
    act(() => {
      ReactDOM.render(
        <Probe path={undefined} overrides={{ label: "Plain" }} />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Plain");
    expect(byTestId("helpText").textContent).toBe("undefined");
  });

  it("returns model data when no overrides given", () => {
    act(() => {
      ReactDOM.render(<Probe path="a.path" />, container);
    });
    expect(byTestId("label").textContent).toBe("Model label");
    expect(byTestId("helpText").textContent).toBe("Model help");
    expect(byTestId("required").textContent).toBe("true");
  });

  it("explicit props win over model data", () => {
    act(() => {
      ReactDOM.render(
        <Probe
          path="a.path"
          overrides={{ label: "Short", helpText: "", required: false }}
        />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Short");
    expect(byTestId("helpText").textContent).toBe("");
    expect(byTestId("required").textContent).toBe("false");
  });

  it("keeps only the keys it knows", () => {
    act(() => {
      ReactDOM.render(
        <Probe path="a.path" overrides={{ placeholder: "ignored" }} />,
        container
      );
    });
    // no crash, unknown keys are not spread into the result
    expect(byTestId("label").textContent).toBe("Model label");
  });

  it("replaces a raw ui_model path label with a readable leaf", () => {
    act(() => {
      ReactDOM.render(
        <Probe path="missing.entities_of_interest.0.chemical_formula" />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Chemical formula");
    // helpText of a missing entry stays null
    expect(byTestId("helpText").textContent).toBe("null");
  });

  it("an explicit label wins over the fallback leaf", () => {
    act(() => {
      ReactDOM.render(
        <Probe
          path="missing.entities_of_interest.0.name"
          overrides={{ label: "Name" }}
        />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Name");
  });
});
