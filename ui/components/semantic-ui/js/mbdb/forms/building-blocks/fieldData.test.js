import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { useModelFieldData } from "./fieldData";

// The real "@js/oarepo_ui/forms" index cannot load under Jest
// (sanitize-html -> postcss is ESM), and in the real app it reads the
// model from a context; here the model data is mocked directly.
jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: () => ({
      label: "Model label",
      helpText: "Model help",
      required: true,
    }),
  }),
}));

const Probe = ({ overrides }) => {
  const data = useModelFieldData("a.path", overrides);
  return (
    <div>
      <span data-testid="label">{String(data.label)}</span>
      <span data-testid="helpText">{String(data.helpText)}</span>
      <span data-testid="required">{String(data.required)}</span>
    </div>
  );
};

Probe.propTypes = {
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
  it("returns model data when no overrides given", () => {
    act(() => {
      ReactDOM.render(<Probe />, container);
    });
    expect(byTestId("label").textContent).toBe("Model label");
    expect(byTestId("helpText").textContent).toBe("Model help");
    expect(byTestId("required").textContent).toBe("true");
  });

  it("explicit props win over model data", () => {
    act(() => {
      ReactDOM.render(
        <Probe overrides={{ label: "Short", helpText: "", required: false }} />,
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
        <Probe overrides={{ placeholder: "ignored" }} />,
        container
      );
    });
    // no crash, unknown keys are not spread into the result
    expect(byTestId("label").textContent).toBe("Model label");
  });
});
