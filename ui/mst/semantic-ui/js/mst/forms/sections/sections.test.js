import React from "react";
import fs from "fs";
import path from "path";
import {
  clickOn,
  modelYamlPath,
  renderInForm,
  unmountForm,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ChemicalEnvironmentsSection, ResultsSection } from "@js/mbdb/forms";
import { DataAnalysisSection } from "./DataAnalysis";
import { InstrumentSection, isMstInstrument } from "./Instrument";
import { MeasurementsSection } from "./Measurements";

jest.mock("@js/oarepo_ui/forms", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockOarepoForms()
);
jest.mock("@js/oarepo_ui/api", () => ({
  EmptyDepositRecordSerializer: class {},
  OARepoDepositSerializer: class {},
}));
jest.mock("react-searchkit", () => ({ buildUID: () => "uid" }));
jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyField()
);
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () => ({
  ...jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyTitles(),
  itemLabel: () => "",
}));
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const record = () => {
  const sample = path.join(
    path.dirname(modelYamlPath()),
    "../common/samples/6g5wd-zxy65-converted.json"
  );
  const { metadata } = JSON.parse(fs.readFileSync(sample, "utf8"));
  const gp = metadata.general_parameters;
  gp.results = [
    {
      id: "r0",
      name: "Kd of sigA",
      type: "Constant of dissociation KD",
      value: 1.5,
      unit: "nM",
      entities_involved: [
        { entity: { id: gp.entities_of_interest[0].id }, copy_number: 1 },
      ],
    },
  ];
  metadata.method_specific_parameters.data_analysis = [
    { results: [{ id: "r0" }], data_fitting: { model: "1:1 binding" } },
  ];
  return { metadata };
};

let container;
afterEach(() => unmountForm(container));

const buttons = (label) =>
  [...document.querySelectorAll("button")].filter(
    (b) => b.textContent === label
  );

describe.each([
  [ChemicalEnvironmentsSection, "potassium phosphate buffer pH 7.5", "pH"],
  [MeasurementsSection, "RNA polymerase sigma factor SigA 26000 nM", "Position"],
  [ResultsSection, "1.5 nM", "Entity"],
  [DataAnalysisSection, "Kd of sigA", "Model"],
])("%#", (section, rowText, modalText) => {
  const Section = section.component;

  it(`${section.label}: shows the record and opens its modal`, async () => {
    container = renderInForm(<Section formConfig={{}} />, {
      initialValues: record(),
    });
    expect(container.textContent).toContain(rowText);
    await clickOn(buttons("Edit")[0]);
    expect(document.querySelector(".ui.modal").textContent).toContain(
      modalText
    );
  });
});

it("Instrument renders its fields", () => {
  const Section = InstrumentSection.component;
  container = renderInForm(<Section />, { initialValues: record() });
  expect(container.textContent).toContain("Excitation LED power");
});

it("offers MST instruments and those without a technique", () => {
  expect(isMstInstrument({ props: { technique: "MST" } })).toBe(true);
  expect(isMstInstrument({})).toBe(true);
  expect(isMstInstrument({ props: { technique: "SPR" } })).toBe(false);
});
