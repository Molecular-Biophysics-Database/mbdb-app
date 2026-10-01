import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { BasicInformation } from "./BasicInformation";

// The picker is faked: the real one queries the vocabulary API. The fake
// stands for what the block needs from it — an "Enter manually" trigger
// (onAddition) and visible proof of which mode is mounted. oarepo's
// StringArrayField is faked too (the shared mock has none): it renders its
// label, which is all the manual form needs to be recognisable.
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// the picker's meta line uses the title cache; keep the network out of tests
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () => ({
  useVocabularyTitle: () => undefined,
  rememberTitle: jest.fn(),
}));

jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const FakeMbdbVocabularyField = ({ fieldPath, onAddition }) =>
    R.createElement(
      "div",
      { "data-testid": "picker", "data-path": fieldPath },
      R.createElement("button", {
        type: "button",
        "data-testid": "enter-manually",
        onClick: () => onAddition("my custom lipid mix"),
      })
    );
  FakeMbdbVocabularyField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
    onAddition: PropTypesActual.func,
  };
  return { MbdbVocabularyField: FakeMbdbVocabularyField };
});

jest.mock("mbdb-react-invenio-forms", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const actual = jest.requireActual("mbdb-react-invenio-forms");
  const StringArrayField = ({ fieldPath, label }) =>
    R.createElement(
      "div",
      { "data-testid": "additional-identifiers", "data-path": fieldPath },
      label
    );
  StringArrayField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
    label: PropTypesActual.node,
  };
  return { ...actual, StringArrayField };
});

const PATH =
  "metadata.general_parameters.entities_of_interest.0.basic_information";

const ValueProbe = () => {
  const { values } = useFormikContext();
  const v = getIn(values, PATH);
  return (
    <span data-testid="value">
      {v === undefined ? "absent" : JSON.stringify(v)}
    </span>
  );
};

let container;

beforeEach(() => {
  setFakeUiModel({
    [PATH]: { label: "Basic information", required: true },
  });
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const seed = (basicInformation) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Chemical",
          ...(basicInformation && { basic_information: basicInformation }),
        },
      ],
    },
  },
});

const render = (basicInformation, opts = {}) => {
  container = renderInForm(
    <>
      <BasicInformation fieldPath={PATH} />
      <ValueProbe />
    </>,
    { initialValues: seed(basicInformation), ...opts }
  );
};

const click = async (testid) => {
  await act(async () => {
    Simulate.click(container.querySelector(`[data-testid="${testid}"]`));
  });
};

const value = () =>
  container.querySelector('[data-testid="value"]').textContent;
const pickerShown = () =>
  container.querySelector('[data-testid="picker"]') !== null;
const manualShown = () =>
  container.querySelector('[data-testid="additional-identifiers"]') !== null;

describe("BasicInformation", () => {
  it("no value renders the PubChem picker", () => {
    render(undefined);
    expect(pickerShown()).toBe(true);
    expect(manualShown()).toBe(false);
    expect(container.querySelector('[data-testid="picker"]').dataset.path).toBe(
      PATH
    );
  });

  it("picking Enter manually writes { title: { en } } and shows the manual form", async () => {
    render(undefined);
    await click("enter-manually");
    expect(value()).toBe('{"title":{"en":"my custom lipid mix"}}');
    expect(pickerShown()).toBe(false);
    expect(manualShown()).toBe(true);
    expect(container.textContent).toContain("Manual entry");
  });

  it("a value with id renders the picker, never the manual form", () => {
    render({ id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" });
    expect(pickerShown()).toBe(true);
    expect(manualShown()).toBe(false);
  });

  it("Search PubChem instead → confirm: key removed, picker shown again", async () => {
    render({
      title: { en: "my custom lipid mix" },
      chemical_formula: "C42H82NO8P",
    });
    expect(manualShown()).toBe(true);

    await act(async () => {
      Simulate.click(
        [...container.querySelectorAll("button")].find(
          (b) => b.textContent === "Search PubChem instead"
        )
      );
    });
    const confirm = [
      ...document.querySelectorAll(".ui.modal .actions .button"),
    ].find((b) => b.textContent === "Remove and search");
    expect(confirm).toBeDefined();
    await act(async () => {
      Simulate.click(confirm);
    });
    expect(value()).toBe("absent");
    expect(pickerShown()).toBe(true);
    expect(manualShown()).toBe(false);
  });

  it("a title error shows in manual mode and survives an unrelated edit", async () => {
    render(
      { title: { en: "my custom lipid mix" } },
      {
        initialErrors: {
          metadata: {
            general_parameters: {
              entities_of_interest: [
                { basic_information: { title: "Only ASCII letters allowed." } },
              ],
            },
          },
        },
      }
    );
    expect(manualShown()).toBe(true);
    expect(container.textContent).toContain("Only ASCII letters allowed.");

    // formik clears `errors` on the first edit anywhere (no validate); the
    // title error must keep showing from initialErrors.
    const formula = container.querySelector(
      `input[name="${PATH}.chemical_formula"]`
    );
    expect(formula).not.toBeNull();
    formula.value = "C42H82NO8P";
    await act(async () => {
      Simulate.change(formula);
    });
    expect(container.textContent).toContain("Only ASCII letters allowed.");
  });

  it("an object-level error shows under the dropdown header", async () => {
    render(undefined, {
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { basic_information: "Missing data for required field." },
            ],
          },
        },
      },
    });
    expect(pickerShown()).toBe(true);
    expect(container.textContent).toContain("Missing data for required field.");
  });
});
