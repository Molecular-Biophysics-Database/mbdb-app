import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  ValueProbe,
  readProbe,
  typeInto,
  pickDropdown,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { HomogeneityFields } from "./index";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

const PATH = "homogeneity";

let container;

beforeEach(() => {
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const fields = () => (
  <>
    <HomogeneityFields fieldPath={PATH} />
    <ValueProbe path={PATH} />
  </>
);

const probe = () => readProbe(container);

const NOTE = "More species observed than expected.";

describe("HomogeneityFields", () => {
  it("shows the note when observed > expected, else not", async () => {
    container = renderInForm(fields(), {
      initialValues: {
        [PATH]: {
          assessed: "Yes",
          method: "Mass photometry",
          expected_number_of_species: 1,
          number_of_species_observed: 2,
        },
      },
    });
    expect(container.textContent).toContain(NOTE);
    await typeInto(
      document.getElementById(`${PATH}.number_of_species_observed`),
      "1"
    );
    expect(container.textContent).not.toContain(NOTE);
    // and not when one is empty
    await typeInto(
      document.getElementById(`${PATH}.expected_number_of_species`),
      ""
    );
    expect(container.textContent).not.toContain(NOTE);
  });

  it("writes the picked method and both species as numbers; clearing removes the key", async () => {
    container = renderInForm(fields(), {
      initialValues: { [PATH]: { assessed: "Yes" } },
    });
    await pickDropdown(`${PATH}.method`, "Mass photometry");
    await typeInto(
      document.getElementById(`${PATH}.expected_number_of_species`),
      "1"
    );
    await typeInto(
      document.getElementById(`${PATH}.number_of_species_observed`),
      "2"
    );
    const stored = probe();
    expect(stored).toEqual({
      assessed: "Yes",
      method: "Mass photometry",
      expected_number_of_species: 1,
      number_of_species_observed: 2,
    });
    expect(typeof stored.expected_number_of_species).toBe("number");
    expect(typeof stored.number_of_species_observed).toBe("number");
    // clearing a number removes its key
    await typeInto(
      document.getElementById(`${PATH}.number_of_species_observed`),
      ""
    );
    expect(probe()).toEqual({
      assessed: "Yes",
      method: "Mass photometry",
      expected_number_of_species: 1,
    });
  });
});
