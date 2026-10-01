import React from "react";
import { act } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { MbdbVocabularyField } from "./MbdbVocabularyField";
import { rememberTitle, useVocabularyTitle } from "./vocabularyTitles";

// The shared fake with one addition: the real FieldDataContext. oarepoFake's
// useFieldData ignores context, but this block nests a FieldDataContext.
// Provider to strip helpText for the inner VocabularyField, and the test
// asserts exactly that override. Spread, not copy: labels/help still come
// from setFakeUiModel.
jest.mock("@js/oarepo_ui/forms", () => {
  const R = jest.requireActual("react");
  const base = jest.requireActual(
    "@js/mbdb/forms/building-blocks/testUtils"
  ).oarepoFake;
  const FieldDataContext = R.createContext();
  return {
    ...base,
    FieldDataContext,
    useFieldData: () => R.useContext(FieldDataContext) ?? base.useFieldData(),
  };
});

jest.mock("./vocabularyTitles", () => ({
  useVocabularyTitle: jest.fn(() => undefined),
  rememberTitle: jest.fn(),
}));

// Fake VocabularyField: exposes the props the wrapper passes (no network),
// and simulates pick/clear/addition by calling onValueChange exactly the way
// RemoteSelectField does: ({ e, data, formikProps }, selectedSuggestions).
// No JSX / no top-level imports in the factory (jest hoisting); the mock
// useFieldData comes from the mocked @js/oarepo_ui/forms via require.
jest.mock("@js/oarepo_vocabularies/form/components/VocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { useFormikContext } = jest.requireActual("formik");
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const { useFieldData } = require("@js/oarepo_ui/forms");
  const FakeVocabularyField = (props) => {
    const formik = useFormikContext();
    const {
      label,
      helpText,
      clearable,
      initialSuggestions,
      filterFunction,
      onValueChange,
      error,
      required,
    } = props;
    // What VocabularyField's own getFieldData call sees: the nested
    // provider's value (the wrapper strips helpText there).
    const { getFieldData } = useFieldData();
    const innerData = getFieldData({ fieldPath: props.fieldPath });
    const described = filterFunction([{ id: "x", props: { rank: "species" } }]);
    const emit = (value, suggestions) =>
      onValueChange(
        { e: null, data: { value }, formikProps: { form: formik } },
        suggestions
      );
    const span = (testid, children) =>
      R.createElement("span", { "data-testid": testid }, children);
    return R.createElement(
      "div",
      { "data-testid": "vf" },
      span("label", label),
      span("helpText", String(helpText)),
      span("inner-helpText", String(innerData.helpText)),
      span("inner-label", String(innerData.label)),
      span("clearable", String(clearable)),
      span("required", String(required)),
      span("error", error ?? ""),
      span("suggestions", JSON.stringify(initialSuggestions)),
      span("described", String(described[0].description)),
      R.createElement("button", {
        type: "button",
        "data-testid": "pick",
        onClick: () =>
          emit("taxid:1423", [
            { id: "taxid:1423", title_l10n: "Bacillus subtilis" },
          ]),
      }),
      R.createElement("button", {
        type: "button",
        "data-testid": "clear",
        onClick: () => emit("", []),
      }),
      R.createElement("button", {
        type: "button",
        "data-testid": "addition",
        onClick: () =>
          emit("typed text", [
            {
              text: "typed text",
              value: "typed text",
              key: "typed text",
              name: "typed text",
              id: "typed text",
              mbdbAddition: true,
            },
          ]),
      })
    );
  };
  FakeVocabularyField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
    label: PropTypesActual.node,
    helpText: PropTypesActual.node,
    clearable: PropTypesActual.bool,
    initialSuggestions: PropTypesActual.array,
    filterFunction: PropTypesActual.func,
    onValueChange: PropTypesActual.func,
    error: PropTypesActual.node,
    required: PropTypesActual.bool,
  };
  return { VocabularyField: FakeVocabularyField };
});

const PATH =
  "metadata.general_parameters.entities_of_interest.0.source_organism";

const UI_MODEL = {
  [PATH]: {
    label: "Source organism",
    helpText: "Identification of the organism",
    required: true,
  },
};

const ValueProbe = () => {
  const { values } = useFormikContext();
  const v = getIn(values, PATH);
  return (
    <span data-testid="value">
      {v === undefined ? "null" : JSON.stringify(v)}
    </span>
  );
};

let container;

beforeEach(() => {
  setFakeUiModel(UI_MODEL);
  // no title known unless the test says so (mockReturnValue does not
  // survive clearMocks leaking between tests, so re-pin the default here)
  useVocabularyTitle.mockImplementation(() => undefined);
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const render = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

const click = async (testid) => {
  // async act: formik's post-setFieldValue dispatch happens off a promise
  await act(async () => {
    container
      .querySelector(`[data-testid="${testid}"]`)
      .dispatchEvent(new MouseEvent("click", { bubbles: true }));
  });
};

const text = (testid) =>
  container.querySelector(`[data-testid="${testid}"]`).textContent;

const FILLED = {
  initialValues: {
    metadata: {
      general_parameters: {
        entities_of_interest: [{ source_organism: { id: "taxid:12374" } }],
      },
    },
  },
};

describe("MbdbVocabularyField", () => {
  it("selecting an option writes { id } and remembers the title", async () => {
    render(
      <>
        <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />
        <ValueProbe />
      </>
    );
    await click("pick");
    expect(text("value")).toBe('{"id":"taxid:1423"}');
    expect(rememberTitle).toHaveBeenCalledWith(
      "organisms",
      "taxid:1423",
      "Bacillus subtilis"
    );
  });

  it('clearing removes the value (undefined, never "")', async () => {
    render(
      <>
        <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />
        <ValueProbe />
      </>,
      FILLED
    );
    await click("clear");
    expect(text("value")).toBe("null");
  });

  it("VocabularyField sees no helpText; FieldHelp renders it in invenio mode", () => {
    render(<MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />);
    expect(text("helpText")).toBe("undefined");
    expect(text("inner-helpText")).toBe("undefined");
    // the help renders exactly once, in the FieldHelp slot after the field
    const helptexts = container.querySelectorAll(
      "label.helptext.mbdb-field-help"
    );
    expect(helptexts).toHaveLength(1);
    expect(helptexts[0].textContent).toBe("Identification of the organism");
  });

  it("the label carries the ? icon in popup mode", () => {
    render(
      <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />,
      {
        helpMode: "popup",
      }
    );
    expect(text("inner-label")).toBe("Source organism");
    expect(text("label")).toContain("Source organism");
    expect(
      container.querySelector('[data-testid="label"] [aria-label^="Help"]')
    ).not.toBeNull();
    expect(
      container.querySelectorAll("label.helptext.mbdb-field-help")
    ).toHaveLength(0);
  });

  it("initialSuggestions carry the title from useVocabularyTitle", () => {
    useVocabularyTitle.mockReturnValue("Bacillus subtilis");
    render(
      <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />,
      FILLED
    );
    expect(text("suggestions")).toBe(
      '[{"id":"taxid:12374","title_l10n":"Bacillus subtilis"}]'
    );
  });

  it("while the title is unknown the suggestion shows the id", () => {
    render(
      <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />,
      FILLED
    );
    expect(text("suggestions")).toBe('[{"id":"taxid:12374"}]');
  });

  it("a stored title wins over the fetched one", () => {
    useVocabularyTitle.mockReturnValue("Fetched title");
    render(
      <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />,
      {
        initialValues: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                {
                  source_organism: {
                    id: "taxid:12374",
                    title: { en: "Stored title" },
                  },
                },
              ],
            },
          },
        },
      }
    );
    expect(text("suggestions")).toBe(
      '[{"id":"taxid:12374","title_l10n":"Stored title"}]'
    );
  });

  it("filterFunction sets description from describe; undefined without it", () => {
    render(
      <MbdbVocabularyField
        fieldPath={PATH}
        vocabularyName="organisms"
        describe={(option) => option.props?.rank}
      />
    );
    expect(text("described")).toBe("species");

    unmountForm(container);
    render(<MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />);
    expect(text("described")).toBe("undefined");
  });

  it("clearable follows the model's required flag", () => {
    render(<MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />);
    expect(text("clearable")).toBe("false");
    expect(text("required")).toBe("true");

    unmountForm(container);
    setFakeUiModel({
      [PATH]: { label: "Source organism", required: false },
    });
    render(<MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />);
    expect(text("clearable")).toBe("true");
  });

  it("explicit label/help/required props win over the model", () => {
    render(
      <MbdbVocabularyField
        fieldPath={PATH}
        vocabularyName="organisms"
        label="Organism"
        help="Pick one"
        required={false}
      />
    );
    expect(text("inner-label")).toBe("Organism");
    expect(text("label")).toContain("Organism");
    expect(text("clearable")).toBe("true");
    expect(container.querySelector("label.helptext").textContent).toBe(
      "Pick one"
    );
  });

  it("onAddition fires for a typed addition and nothing is written", async () => {
    const onAddition = jest.fn();
    render(
      <>
        <MbdbVocabularyField
          fieldPath={PATH}
          vocabularyName="chemicals"
          onAddition={onAddition}
        />
        <ValueProbe />
      </>
    );
    await click("addition");
    expect(onAddition).toHaveBeenCalledWith("typed text");
    expect(text("value")).toBe("null");
  });

  it("without onAddition an addition writes nothing either", async () => {
    render(
      <>
        <MbdbVocabularyField fieldPath={PATH} vocabularyName="chemicals" />
        <ValueProbe />
      </>
    );
    await click("addition");
    expect(text("value")).toBe("null");
  });

  it("shows the server error from initialErrors", () => {
    render(
      <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />,
      {
        initialErrors: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                { source_organism: "Missing data for required field." },
              ],
            },
          },
        },
      }
    );
    expect(text("error")).toBe("Missing data for required field.");
  });

  it("shows a nested { id } error the same way (Invalid vocabulary item)", () => {
    render(
      <MbdbVocabularyField fieldPath={PATH} vocabularyName="organisms" />,
      {
        initialErrors: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                { source_organism: { id: "Invalid vocabulary item" } },
              ],
            },
          },
        },
      }
    );
    expect(text("error")).toBe("Invalid vocabulary item");
  });
});
