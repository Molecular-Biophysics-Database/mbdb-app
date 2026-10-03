import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn } from "formik";
import {
  editUnrelatedField,
  renderInForm,
  unmountForm,
  setFakeUiModel,
  setFakeVocabulary,
  setFakeVocabularyPicks,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { BasicInformation } from "./BasicInformation";
import { MANUAL_CHEMICALS_ENABLED } from "./chemical";

// The picker is faked: the real one queries the vocabulary API. The fake
// stands for what the block needs from it — an "Enter manually" trigger
// (onAddition) and visible proof of which mode is mounted. oarepo's
// StringArrayField is faked too (the shared mock has none): it renders its
// label, which is all the manual form needs to be recognisable.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// The picker's meta line uses the item cache; the shared synchronous cache
// (plan 3R X6) keeps the network out of tests.
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyTitles()
);

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

jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyField()
);

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
  setFakeVocabulary();
  setFakeVocabularyPicks({ chemicals: { id: WATER.id } });
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
    // the cache holds the picked item (the real pick remembers it; here the
    // suite seeds it), so the meta line and links come from it
    setFakeVocabulary({
      [`chemicals/${WATER.id}`]: {
        title: WATER.title,
        customFields: WATER.customFields,
      },
    });
    render(undefined);
    await click("pick");
    expect(value()).toBe(`{"id":"${WATER.id}"}`);
    // facts and id, no title (the dropdown shows that)
    expect(container.querySelector(".mbdb-muted-text").textContent).toBe(
      `H2O · 18.02 g/mol · ${WATER.id}`
    );
    const label = container.querySelector('[data-testid="picker-label"]');
    // ExternalLink appends a space + icon; trim to compare the label texts
    const links = [...label.querySelectorAll("a")].map((a) =>
      a.textContent.trim()
    );
    expect(links).toEqual(["PubChem ↗", "ChEMBL ↗"]);
    // anchors, so no type attribute
    label.querySelectorAll("a").forEach((a) => {
      expect(a.getAttribute("type")).toBeNull();
    });
  });

  it("an object-level error is shown once, by the picker's dropdown label", () => {
    // MbdbVocabularyField already shows the object-level error as the
    // dropdown's error label, so BasicInformation adds no error block of its
    // own. The fake renders that one error (data-testid=picker-error); the
    // message must not be duplicated.
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
    expect(
      container.querySelectorAll('[data-testid="picker-error"]')
    ).toHaveLength(1);
    const occurrences =
      container.textContent.split("Missing data for required field.").length -
      1;
    expect(occurrences).toBe(1);
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
