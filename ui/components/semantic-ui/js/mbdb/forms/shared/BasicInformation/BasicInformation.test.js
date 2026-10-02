import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  editUnrelatedField,
  renderInForm,
  unmountForm,
  setFakeUiModel,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { BasicInformation } from "./BasicInformation";
import { MANUAL_CHEMICALS_ENABLED } from "./chemical";

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

// the picker's meta line uses the item cache; keep the network out of
// tests. remembered is the fake cache: the fake picker's pick writes into
// it (like rememberItem would seed the real one) and the hook reads it.
let mockRemembered = {};
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () => ({
  useVocabularyItem: jest.fn(
    (type, id) =>
      mockRemembered[`${type}/${id}`] ?? {
        title: undefined,
        customFields: undefined,
      }
  ),
  rememberItem: jest.fn((type, id, item) => {
    mockRemembered[`${type}/${id}`] = item;
  }),
}));

// The Water suggestion the serializeVocabularySuggestions shape has for a
// chemicals pick: the custom_fields ride along, so the item cache never
// needs a GET for a picked term.
const WATER = {
  id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N",
  title: "Water",
  customFields: {
    chemical_formula: "H2O",
    molecular_weight: { value: 18.02, unit: "g/mol" },
  },
};

jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { useFormikContext } = jest.requireActual("formik");
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const {
    rememberItem,
  } = require("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles");
  // The fake stands for what the block needs from the real wrapper: the
  // label slot, a pick that remembers the item and writes { id } the way
  // the real onValueChange does, and (when the flag is on) the "Enter
  // manually" trigger (onAddition).
  const FakeMbdbVocabularyField = ({ fieldPath, label, onAddition }) => {
    const formik = useFormikContext();
    return R.createElement(
      "div",
      { "data-testid": "picker", "data-path": fieldPath },
      R.createElement("span", { "data-testid": "picker-label" }, label),
      R.createElement("button", {
        type: "button",
        "data-testid": "pick",
        onClick: () => {
          rememberItem("chemicals", WATER.id, {
            title: WATER.title,
            customFields: WATER.customFields,
          });
          formik.setFieldValue(fieldPath, { id: WATER.id });
        },
      }),
      onAddition &&
        R.createElement("button", {
          type: "button",
          "data-testid": "enter-manually",
          onClick: () => onAddition("my custom lipid mix"),
        })
    );
  };
  FakeMbdbVocabularyField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
    label: PropTypesActual.node,
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
  mockRemembered = {};
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

  it("a value with id renders the picker, never the manual form", () => {
    render({ id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" });
    expect(pickerShown()).toBe(true);
    expect(manualShown()).toBe(false);
  });

  it("a manual { title } value renders the manual form (manual entry enabled)", () => {
    // the P2-F1 flip landed (chemical.js): manual values go to ManualChemical
    expect(MANUAL_CHEMICALS_ENABLED).toBe(true);
    render({ title: { en: "my custom lipid mix" } });
    expect(manualShown()).toBe(true);
    expect(pickerShown()).toBe(false);
  });

  it("a picked chemical shows the facts · id meta line and the label-slot links", async () => {
    render(undefined);
    await click("pick");
    // the fake pick seeds the item cache and writes { id }, like the real
    // wrapper's onValueChange — the meta line and links then come from the
    // remembered item
    expect(value()).toBe(`{"id":"${WATER.id}"}`);
    // facts and id, no title (the dropdown shows that)
    expect(container.querySelector(".ui.small.grey.text").textContent).toBe(
      `H2O · 18.02 g/mol · ${WATER.id}`
    );
    const label = container.querySelector('[data-testid="picker-label"]');
    const links = [...label.querySelectorAll("a")].map((a) => a.textContent);
    expect(links).toEqual(["PubChem ↗", "ChEMBL ↗"]);
    // anchors, so no type attribute
    label.querySelectorAll("a").forEach((a) => {
      expect(a.getAttribute("type")).toBeNull();
    });
  });

  it("an object-level error is left to the picker's dropdown error label", () => {
    // no duplicated message under the header: MbdbVocabularyField already
    // shows the object-level error as the dropdown's error label, so the
    // picker renders no error block of its own. The fake renders no error;
    // the real error label including the survives-an-unrelated-edit
    // behaviour is covered in MbdbVocabularyField.test.js.
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
    expect(container.textContent).not.toContain(
      "Missing data for required field."
    );
  });

  // The server drops manual chemicals on save (chemical.js), so these run
  // only once MANUAL_CHEMICALS_ENABLED flips on (plan 2R "Manual chemicals").
  (MANUAL_CHEMICALS_ENABLED ? describe : describe.skip)("manual mode", () => {
    it("picking Enter manually writes { title: { en } } and shows the manual form", async () => {
      render(undefined);
      await click("enter-manually");
      expect(value()).toBe('{"title":{"en":"my custom lipid mix"}}');
      expect(pickerShown()).toBe(false);
      expect(manualShown()).toBe(true);
      expect(container.textContent).toContain("Manual entry");
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
          withUnrelatedField: true,
          initialErrors: {
            metadata: {
              general_parameters: {
                entities_of_interest: [
                  {
                    basic_information: { title: "Only ASCII letters allowed." },
                  },
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
      await editUnrelatedField(container);
      expect(container.textContent).toContain("Only ASCII letters allowed.");
    });

    it("the manual name input is labelled Name and required", () => {
      // `title` is an i18ndict; the `en` leaf has no model label ("En")
      render({ title: { en: "my custom lipid mix" } });
      const name = container.querySelector(`input[name="${PATH}.title.en"]`);
      expect(name).not.toBeNull();
      const field = name.closest(".field");
      expect(field.textContent).toContain("Name");
      expect(field.textContent).not.toContain(" En ");
    });
  });
});
