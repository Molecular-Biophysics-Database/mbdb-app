import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { getIn, useFormikContext } from "formik";
import { StoryFrame } from "./StoryFrame";

// Plain react-dom test utils: @testing-library/dom in the assets project fails
// to load (pretty-format mismatch).

const PATH = "metadata.general_parameters.entities_of_interest.0.name";

const Probe = () => {
  const { values, errors, initialErrors } = useFormikContext();
  return (
    <div>
      <span data-testid="value">{getIn(values, PATH) || "-"}</span>
      <span data-testid="error">
        {getIn(errors, PATH) || getIn(initialErrors, PATH) || "-"}
      </span>
    </div>
  );
};

const story = {
  title: "Probe",
  scenarios: [
    { name: "Empty", initialValues: {}, render: Probe },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: { entities_of_interest: [{ name: "Serum" }] },
        },
      },
      render: Probe,
    },
  ],
};

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
  act(() => {
    ReactDOM.render(<StoryFrame story={story} />, container);
  });
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);
const byText = (text) =>
  [...container.querySelectorAll("a, button, div.title")].find(
    (el) => el.textContent.trim() === text
  );
const click = (text) => act(() => Simulate.click(byText(text)));

describe("StoryFrame", () => {
  it("switches scenarios and shows the live values", () => {
    expect(byTestId("value").textContent).toBe("-");

    click("Filled");
    expect(byTestId("value").textContent).toBe("Serum");
    expect(container.querySelector("pre").textContent).toContain(
      '"name": "Serum"'
    );
  });

  it("maps injected server errors to their field and clears them", () => {
    click("Filled");
    click("Server errors (inject)");

    const textarea = container.querySelector("textarea");
    textarea.value = JSON.stringify([
      { field: PATH, messages: ["Too short."] },
    ]);
    act(() => Simulate.change(textarea));
    click("Apply errors");
    expect(byTestId("error").textContent).toBe("Too short.");
    expect(byTestId("value").textContent).toBe("Serum");

    click("Clear");
    expect(byTestId("error").textContent).toBe("-");
  });
});
