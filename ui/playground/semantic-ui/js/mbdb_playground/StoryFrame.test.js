import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { getIn, useFormikContext } from "formik";
import { useDisclosureDefault } from "mbdb-semantic-ui-react";
import { StoryFrame } from "./StoryFrame";

// StoryFrame imports EntityDetails (its module chain reaches sanitize-html, an
// ESM package Jest cannot load); the story's `review: "entity"` path is
// covered by EntityDetails.test.js, so stub it here.
// eslint-disable-next-line no-restricted-syntax -- the shared-chain fake (§8)
jest.mock("@js/mbdb/forms/sections/EntitiesOfInterest/EntityDetails", () => {
  const React = jest.requireActual("react");
  return {
    // eslint-disable-next-line react/prop-types
    EntityDetails: ({ fieldPath }) =>
      React.createElement(
        "div",
        { "data-testid": "entity-details" },
        fieldPath
      ),
  };
});

// Plain react-dom test utils: @testing-library/dom in the assets project fails
// to load (pretty-format mismatch).

const PATH = "metadata.general_parameters.entities_of_interest.0.name";

// eslint-disable-next-line no-restricted-syntax -- reads values + live + initial errors together (an errors probe, not a one-path JSON value probe)
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

// A story that reads the one-shot disclosure default and lets the test type
// into Formik, so a remount that keeps the values can be proven.
const DisclosureStory = () => {
  const disclosure = useDisclosureDefault();
  const { values, setFieldValue } = useFormikContext();
  return (
    <>
      <span data-testid="disclosure">{disclosure ?? "none"}</span>
      <input
        data-testid="name"
        value={getIn(values, PATH) ?? ""}
        onChange={(e) => setFieldValue(PATH, e.target.value)}
      />
    </>
  );
};

const disclosureStory = {
  title: "Disclosure",
  scenarios: [
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: { entities_of_interest: [{ name: "Serum" }] },
        },
      },
      render: DisclosureStory,
    },
  ],
};

describe("StoryFrame Expand all / Collapse all default", () => {
  const renderFrame = (el) => {
    act(() => {
      ReactDOM.render(el, container);
    });
  };

  it("re-reads the disclosure default on remount and keeps the Formik values", () => {
    renderFrame(
      <StoryFrame story={disclosureStory} disclosure="closed" epoch={0} />
    );
    expect(byTestId("disclosure").textContent).toBe("closed");

    // type a value that differs from the initial values
    const input = byTestId("name");
    input.value = "Typed";
    act(() => Simulate.change(input));
    expect(byTestId("name").value).toBe("Typed");

    // "Expand all": the default changes and the epoch bumps, so the story
    // content remounts and re-reads the default — Formik is not remounted
    renderFrame(
      <StoryFrame story={disclosureStory} disclosure="open" epoch={1} />
    );
    expect(byTestId("disclosure").textContent).toBe("open");
    expect(byTestId("name").value).toBe("Typed");
  });

  it("has no default when used without the buttons (disclosure undefined)", () => {
    renderFrame(<StoryFrame story={disclosureStory} />);
    expect(byTestId("disclosure").textContent).toBe("none");
  });
});
