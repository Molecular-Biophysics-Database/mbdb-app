import React from "react";
import { ReviewModeProvider } from "mbdb-semantic-ui-react";
import { EntityDetails } from "./EntityDetails";
import {
  realUiModel,
  renderInForm,
  setFakeVocabulary,
  setStructuredUiModel,
  unmountForm,
} from "@js/mbdb/forms/building-blocks/testUtils";

// EntityDetails pulls entityTypes -> every entity Fields set, whose chain
// reaches the ESM-only sanitize-html / oarepo modules Jest cannot load; the
// canonical fakes break it. The real ui_model drives the variant-aware labels.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fakes (§8)
jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
);
jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyField()
);
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyTitles()
);
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const ENTITY = "metadata.general_parameters.entities_of_interest.0";

const values = (entity) => ({
  metadata: { general_parameters: { entities_of_interest: [entity] } },
});

let container;

const mount = (entity) => {
  container = renderInForm(
    <ReviewModeProvider review>
      <EntityDetails fieldPath={ENTITY} />
    </ReviewModeProvider>,
    { initialValues: values(entity) }
  );
};

beforeEach(() => {
  setFakeVocabulary();
  setStructuredUiModel(realUiModel());
});

afterEach(() => {
  setStructuredUiModel();
  unmountForm(container);
  container = null;
});

const TYPES = [
  "Polymer",
  "Chemical",
  "Molecular assembly",
  "Complex substance of biological origin",
  "Complex substance of environmental origin",
  "Complex substance of chemical origin",
  "Complex substance of industrial origin",
];

describe("EntityDetails", () => {
  TYPES.forEach((type) => {
    it(`renders a heading and the details table for ${type}`, () => {
      mount({ id: "e1", type, name: "Water" });
      // the "<name> · <type>" heading
      expect(container.textContent).toContain(`Water · ${type}`);
      // the details (a DetailView) rendered its definition table
      expect(container.querySelector("table.mbdb-detail-table")).not.toBeNull();
    });
  });

  it("does not repeat the row's own columns (id, type, name)", () => {
    mount({
      id: "e1",
      type: "Chemical",
      name: "Water",
      basic_information: { id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" },
    });
    // the details show the Chemical's field(s), never the excluded columns
    expect(container.textContent).toContain("Basic information");
    const labels = [...container.querySelectorAll("td")].map((td) =>
      td.textContent.trim()
    );
    expect(labels).not.toContain("Name");
    expect(labels).not.toContain("Type");
    expect(labels).not.toContain("Id");
  });
});
