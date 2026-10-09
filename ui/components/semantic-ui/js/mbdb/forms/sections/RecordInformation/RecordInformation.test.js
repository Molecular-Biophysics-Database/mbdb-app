import React from "react";
import {
  renderInForm,
  unmountForm,
  clickOn,
  typeInto,
  ValueProbe,
  readProbe,
  setFakeUiModel,
  setFakeVocabulary,
  setFakeVocabularyPicks,
  yamlEnum,
  yamlProperties,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { RecordInformationSectionComponent } from "./RecordInformation";
import { PUBLICATION_TYPES, DEGREE_TYPES } from "./AssociatedPublicationForm";
import { PERSON_GROUPS } from "./PersonForm";

// buildUID lives in react-searchkit, whose d3 dependency (ESM) Jest cannot
// load. The section is the one module that imports it, so it is mocked here.
jest.mock("react-searchkit", () => ({
  buildUID: (prefix, id) => `${prefix}.${id}`,
}));

// The section composes vocabulary pickers (affiliations, funders, awards), so
// the same one-fake-per-layer setup as the entity tests is needed.
// eslint-disable-next-line no-restricted-syntax -- the shared mockOarepoForms() factory
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

// Client-only row keys (jsdom has no WebCrypto).
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const GP = "metadata.general_parameters";
const TITLE_PATH = `${GP}.record_information.title`;
const PUBLICATION_PATH = `${GP}.associated_publication`;
const DEPOSITORS_PATH = `${GP}.depositors`;
const FUNDING_REFERENCES_PATH = `${GP}.funding_references`;

let container;

beforeEach(() => {
  setFakeUiModel({});
  setFakeVocabulary({});
  setFakeVocabularyPicks();
});

afterEach(() => {
  unmountForm(container);
  container = null;
});

const section = () => (
  <RecordInformationSectionComponent
    formConfig={{ overridableIdPrefix: "mbdb" }}
  />
);

const record = (recordInformation, publication) => ({
  metadata: {
    general_parameters: {
      ...(recordInformation !== undefined
        ? { record_information: recordInformation }
        : {}),
      ...(publication !== undefined
        ? { associated_publication: publication }
        : {}),
    },
  },
});

const render = (initialValues, opts = {}, probePath = PUBLICATION_PATH) =>
  renderInForm(
    <>
      {section()}
      <ValueProbe path={probePath} />
    </>,
    { initialValues, ...opts }
  );

const addBtn = () =>
  [...container.querySelectorAll("button")].find((b) =>
    b.textContent.includes("Add Associated publication")
  );

// A button by its exact text (e.g. "Add contributor", "Add funding reference").
const addTextBtn = (label) =>
  [...container.querySelectorAll("button")].find(
    (b) => b.textContent === label
  );

const editBtn = () =>
  [...container.querySelectorAll("button")].find(
    (b) => b.textContent === "Edit"
  );

const modal = () => document.body.querySelector(".ui.modal");

// An input by its fieldPath (the blocks render id={fieldPath}; dots are not
// selector-safe, so getElementById).
const field = (name) => document.getElementById(`${PUBLICATION_PATH}.${name}`);

const modalButton = (label) =>
  [...modal().querySelectorAll("button")].find((b) => b.textContent === label);

// Pick a type from the modal's Type dropdown (the first .ui.dropdown).
const pickType = async (type) => {
  const typeDropdown = modal().querySelector(".ui.dropdown");
  await clickOn(typeDropdown);
  const item = [...typeDropdown.querySelectorAll(".menu .item")].find(
    (el) => el.textContent.trim() === type
  );
  await clickOn(item);
};

describe("RecordInformationSection", () => {
  it("renders the record Title field, required, with its help", () => {
    container = render(record({ title: "MST of hemoglobin" }));
    const input = document.getElementById(TITLE_PATH);
    expect(input).not.toBeNull();
    expect(input.value).toBe("MST of hemoglobin");
    expect(container.textContent).toContain("Title");
    expect(container.textContent).toContain(
      "Short descriptive title of the record"
    );
  });

  it("shows the Add button when the publication is absent", () => {
    container = render(undefined);
    expect(addBtn()).toBeDefined();
    expect(editBtn()).toBeUndefined();
  });

  it("Add seeds Article, opens the modal with Pid, Title and Journal", async () => {
    container = render(undefined);
    await clickOn(addBtn());
    expect(readProbe(container)).toEqual({ type: "Article" });
    expect(modal()).not.toBeNull();
    // the base fields and the Article-specific Journal are in the modal
    expect(field("pid")).not.toBeNull();
    expect(field("title")).not.toBeNull();
    expect(field("journal")).not.toBeNull();
    expect(modal().textContent).toContain("Pid");
    expect(modal().textContent).toContain("Journal");
  });

  it("writes the typed Pid and Journal through Done", async () => {
    container = render(undefined);
    await clickOn(addBtn());
    await typeInto(field("pid"), "doi:10.1038/s41592");
    await typeInto(field("journal"), "Nature Methods");
    await clickOn(modalButton("Done"));
    expect(modal()).toBeNull();
    expect(readProbe(container)).toEqual({
      type: "Article",
      pid: "doi:10.1038/s41592",
      journal: "Nature Methods",
    });
  });

  it("Cancel restores the snapshot taken on Edit", async () => {
    container = render(
      record(undefined, {
        type: "Article",
        pid: "doi:10.1038/s41592",
        journal: "Nature Methods",
      })
    );
    await clickOn(editBtn());
    await typeInto(field("pid"), "x");
    await clickOn(modalButton("Cancel"));
    expect(readProbe(container)).toEqual({
      type: "Article",
      pid: "doi:10.1038/s41592",
      journal: "Nature Methods",
    });
  });

  it("shows the summary row (pid, title, type) when present", () => {
    container = render(
      record(undefined, {
        type: "Article",
        pid: "doi:10.1038/s41592",
        title: "Hemoglobin by MST",
      })
    );
    const row = container.querySelector("tbody tr");
    const cells = [...row.querySelectorAll("td")].map((td) =>
      td.textContent.trim()
    );
    expect(cells).toContain("doi:10.1038/s41592");
    expect(cells).toContain("Hemoglobin by MST");
    expect(cells).toContain("Article");
  });
});

describe("AssociatedPublication type-specific fields", () => {
  it.each([
    ["Article", { type: "Article" }, "journal", "publisher"],
    ["Book", { type: "Book" }, "publisher", "journal"],
  ])(
    "%s shows its own field and not the other's",
    async (_, pub, own, other) => {
      container = render(record(undefined, pub));
      await clickOn(editBtn());
      expect(field(own)).not.toBeNull();
      expect(field(other)).toBeNull();
    }
  );

  it("Thesis shows the degree type dropdown", async () => {
    container = render(record(undefined, { type: "Thesis" }));
    await clickOn(editBtn());
    expect(field("degree_type")).not.toBeNull();
    expect(modal().textContent).toContain("Degree type");
  });

  it("a type change asks for confirmation, keeps pid and title, drops the rest", async () => {
    container = render(
      record(undefined, {
        type: "Article",
        pid: "doi:10.1038/s41592",
        title: "Hemoglobin by MST",
        journal: "Nature Methods",
      })
    );
    await clickOn(editBtn());
    await pickType("Book");
    const confirm = [...document.body.querySelectorAll(".ui.modal")].find((m) =>
      m.textContent.includes("will be removed")
    );
    expect(confirm).toBeDefined();
    // not applied until confirmed
    expect(readProbe(container).type).toBe("Article");
    await clickOn(
      [...confirm.querySelectorAll("button")].find(
        (b) => b.textContent === "Change"
      )
    );
    expect(readProbe(container)).toEqual({
      type: "Book",
      pid: "doi:10.1038/s41592",
      title: "Hemoglobin by MST",
    });
  });
});

describe("model agreement", () => {
  it("PUBLICATION_TYPES equals the model's Publication_base.type enum", () => {
    expect(PUBLICATION_TYPES).toEqual(yamlEnum("Publication_base", "type"));
  });

  it("DEGREE_TYPES equals the model's Thesis.degree_type enum", () => {
    expect(DEGREE_TYPES).toEqual(yamlEnum("Thesis", "degree_type"));
  });

  it("PERSON_GROUPS covers every property of the model's Person", () => {
    const covered = PERSON_GROUPS.flatMap((g) => g.fields).map((entry) =>
      typeof entry === "string" ? entry : entry.field
    );
    expect(covered).toEqual(yamlProperties("Person"));
  });
});

describe("Depositors", () => {
  const depositorInput = (person, name) =>
    document.getElementById(`${DEPOSITORS_PATH}.${person}.${name}`);

  it("renders the Depositor and Principal contact groups with the person fields", () => {
    container = render(undefined);
    expect(container.textContent).toContain("Depositor");
    expect(container.textContent).toContain("Principal contact");
    expect(depositorInput("depositor", "given_name")).not.toBeNull();
    expect(depositorInput("depositor", "family_name")).not.toBeNull();
    expect(depositorInput("principal_contact", "given_name")).not.toBeNull();
    // the ORCID boxes and the affiliations plus button
    expect(container.querySelectorAll(".mbdb-orcid-box")).toHaveLength(32);
    expect(container.textContent).toContain("Identifiers");
    expect(addTextBtn("Add affiliation")).toBeDefined();
  });

  it("writes the typed depositor and principal contact names", async () => {
    container = render(undefined, {}, DEPOSITORS_PATH);
    await typeInto(depositorInput("depositor", "given_name"), "Max");
    await typeInto(depositorInput("depositor", "family_name"), "Mustermann");
    await typeInto(depositorInput("principal_contact", "given_name"), "Josiah");
    expect(readProbe(container)).toEqual({
      depositor: { given_name: "Max", family_name: "Mustermann" },
      principal_contact: { given_name: "Josiah" },
    });
  });

  describe("ORCID prefill", () => {
    const DEPOSITOR_ORCID = "0000-0002-1825-0097";

    const orcidBoxes = () =>
      [...container.querySelectorAll(".mbdb-orcid-box input")].slice(0, 16);
    const prefillBtn = () =>
      [...container.querySelectorAll("button")].find((b) =>
        b.textContent.includes("Prefill from ORCID")
      );
    const removeBtn = () =>
      [...container.querySelectorAll("button")].find(
        (b) => b.textContent === "Remove"
      );

    const typeOrcid = async (digits) => {
      const boxes = orcidBoxes();
      for (let i = 0; i < digits.length; i += 1) {
        // eslint-disable-next-line no-await-in-loop -- one box per tick
        await typeInto(boxes[i], digits[i]);
      }
    };

    const orcidResponse = (body, ok = true, status = 200) => ({
      ok,
      status,
      json: () => Promise.resolve(body),
    });

    const carberry = {
      person: {
        name: {
          "given-names": { value: "Josiah" },
          "family-name": { value: "Carberry" },
        },
      },
    };

    afterEach(() => {
      delete global.fetch;
    });

    it("shows no Prefill button until all 16 digits are typed", async () => {
      container = render(undefined, {}, `${DEPOSITORS_PATH}.depositor`);
      await typeOrcid("000000021825009");
      expect(prefillBtn()).toBeUndefined();
      await typeInto(orcidBoxes()[15], "7");
      expect(prefillBtn()).toBeDefined();
    });

    it("Prefill fetches the ORCID API and fills the names and identifier", async () => {
      global.fetch = jest.fn().mockResolvedValue(orcidResponse(carberry));
      container = render(undefined, {}, `${DEPOSITORS_PATH}.depositor`);
      await typeOrcid(DEPOSITOR_ORCID.replace(/-/g, ""));
      await clickOn(prefillBtn());
      expect(global.fetch).toHaveBeenCalledWith(
        `https://pub.orcid.org/v3.0/${DEPOSITOR_ORCID}`,
        { headers: { Accept: "application/json" } }
      );
      expect(readProbe(container)).toEqual({
        given_name: "Josiah",
        family_name: "Carberry",
        identifiers: [`orcid:${DEPOSITOR_ORCID}`],
      });
    });

    it("a failed lookup shows the error and writes nothing", async () => {
      global.fetch = jest.fn().mockResolvedValue(orcidResponse({}, false, 404));
      container = render(undefined, {}, `${DEPOSITORS_PATH}.depositor`);
      await typeOrcid(DEPOSITOR_ORCID.replace(/-/g, ""));
      await clickOn(prefillBtn());
      expect(container.textContent).toContain(
        `No ORCID record for ${DEPOSITOR_ORCID}`
      );
      expect(readProbe(container)).toBeNull();
    });

    it("a stored ORCID fills the boxes and Remove clears the prefill", async () => {
      container = render(
        {
          metadata: {
            general_parameters: {
              depositors: {
                depositor: {
                  given_name: "Josiah",
                  family_name: "Carberry",
                  identifiers: [`orcid:${DEPOSITOR_ORCID}`],
                },
              },
            },
          },
        },
        {},
        `${DEPOSITORS_PATH}.depositor`
      );
      expect(
        orcidBoxes()
          .map((b) => b.value)
          .join("")
      ).toBe(DEPOSITOR_ORCID.replace(/-/g, ""));
      await clickOn(removeBtn());
      expect(readProbe(container)).toBeNull();
      expect(orcidBoxes().every((b) => b.value === "")).toBe(true);
    });
  });

  it("Add contributor opens the person modal and Done writes the row", async () => {
    container = render(
      {
        metadata: {
          general_parameters: {
            depositors: { depositor: { given_name: "Max" } },
          },
        },
      },
      {},
      `${DEPOSITORS_PATH}.contributors`
    );
    await clickOn(addTextBtn("Add contributor"));
    await typeInto(
      document.getElementById(`${DEPOSITORS_PATH}.contributors.0.given_name`),
      "Jane"
    );
    await typeInto(
      document.getElementById(`${DEPOSITORS_PATH}.contributors.0.family_name`),
      "Doe"
    );
    await clickOn(modalButton("Done"));
    expect(modal()).toBeNull();
    expect(readProbe(container)).toEqual([
      { given_name: "Jane", family_name: "Doe" },
    ]);
    // the summary row shows both name columns
    const cells = [
      ...container.querySelector("tbody tr").querySelectorAll("td"),
    ].map((td) => td.textContent.trim());
    expect(cells).toContain("Jane");
    expect(cells).toContain("Doe");
  });

  it("a stored contributor shows its names and edits through the modal", async () => {
    container = render(
      {
        metadata: {
          general_parameters: {
            depositors: {
              contributors: [{ given_name: "Jane", family_name: "Doe" }],
            },
          },
        },
      },
      {},
      `${DEPOSITORS_PATH}.contributors`
    );
    const cells = [
      ...container.querySelector("tbody tr").querySelectorAll("td"),
    ].map((td) => td.textContent.trim());
    expect(cells).toContain("Jane");
    expect(cells).toContain("Doe");
    await clickOn(editBtn());
    await typeInto(
      document.getElementById(`${DEPOSITORS_PATH}.contributors.0.given_name`),
      "Janet"
    );
    await clickOn(modalButton("Done"));
    expect(readProbe(container)).toEqual([
      { given_name: "Janet", family_name: "Doe" },
    ]);
  });

  it("an affiliation pick inside the person modal writes { id }", async () => {
    setFakeVocabularyPicks({
      affiliations: { id: "02hpadn98", title_l10n: "Masaryk University" },
    });
    container = render(
      undefined,
      {},
      `${DEPOSITORS_PATH}.depositor.affiliations`
    );
    await clickOn(addTextBtn("Add affiliation"));
    expect(modal().textContent).toContain("Affiliation");
    await clickOn(modal().querySelector('[data-testid="pick"]'));
    await clickOn(modalButton("Done"));
    expect(readProbe(container)).toEqual([{ id: "02hpadn98" }]);
  });

  it("a stored affiliation shows its title in the summary row", () => {
    setFakeVocabulary({
      "affiliations/02hpadn98": { title: "Masaryk University" },
    });
    container = render({
      metadata: {
        general_parameters: {
          depositors: {
            depositor: { affiliations: [{ id: "02hpadn98" }] },
          },
        },
      },
    });
    expect(container.textContent).toContain("Masaryk University");
  });
});

describe("FundingReferences", () => {
  it("Add funding reference opens the modal with the Funder and Award pickers", async () => {
    setFakeVocabularyPicks({
      funders: { id: "05k73zm37", title_l10n: "Academy of Finland" },
      awards: { id: "05k73zm37::213912", title_l10n: "PLTP" },
    });
    container = render(undefined, {}, FUNDING_REFERENCES_PATH);
    await clickOn(addTextBtn("Add funding reference"));
    const picks = [...modal().querySelectorAll('[data-testid="pick"]')];
    expect(picks).toHaveLength(2);
    await clickOn(picks[0]);
    await clickOn([...modal().querySelectorAll('[data-testid="pick"]')][1]);
    await clickOn(modalButton("Done"));
    expect(readProbe(container)).toEqual([
      {
        funder: { id: "05k73zm37" },
        award: { id: "05k73zm37::213912" },
      },
    ]);
  });

  it("a stored funding reference shows the funder and award titles", () => {
    setFakeVocabulary({
      "funders/05k73zm37": { title: "Academy of Finland" },
      "awards/05k73zm37::213912": { title: "PLTP" },
    });
    container = render({
      metadata: {
        general_parameters: {
          funding_references: [
            {
              funder: { id: "05k73zm37" },
              award: { id: "05k73zm37::213912" },
            },
          ],
        },
      },
    });
    expect(container.textContent).toContain("Academy of Finland");
    expect(container.textContent).toContain("PLTP");
  });
});
