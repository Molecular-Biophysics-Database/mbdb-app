import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useFormikContext, getIn, setIn } from "formik";
import { typeInto } from "@js/mbdb/forms/building-blocks/testUtils";
import { ExternalDatabases } from "./ExternalDatabases";

// One shared harness (guide §10): the fake "@js/oarepo_ui/forms" and the
// Formik render helpers live in testUtils; no per-file copies.
// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);
// crypto.randomUUID needs https/localhost; jest must use the same key
// generator as the building block or TableArrayField cannot mint row keys
let mockKeyN = 0;
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => `key-${++mockKeyN}-uuid`,
}));
const { setFakeUiModel, renderInForm, unmountForm } = jest.requireActual(
  "@js/mbdb/forms/building-blocks/testUtils"
);

const FIELD =
  "metadata.general_parameters.entities_of_interest.0.external_databases";

// Reads the whole formik values out via a callback so tests assert stored
// data, not DOM — renderless, so it cannot be ValueProbe (which renders JSON
// at one path).
// eslint-disable-next-line no-restricted-syntax -- renderless onValues collector, not a one-path JSON probe
const Probe = ({ onValues }) => {
  onValues(useFormikContext().values);
  return null;
};
Probe.propTypes = { onValues: PropTypes.func.isRequired };

let container;
let values;
const collectValues = (v) => {
  values = v;
};

const render = (options) =>
  renderInForm(
    <>
      <ExternalDatabases fieldPath={FIELD} />
      <Probe onValues={collectValues} />
    </>,
    options
  );

beforeEach(() => {
  setFakeUiModel({});
  values = undefined;
});

afterEach(() => {
  unmountForm(container);
});

// setIn({}, FIELD, v) builds the nested fixture Formik actually reads;
// getIn(values, FIELD) then returns it. A literal `{ [FIELD]: v }` key
// would never be found by getIn's path walk (verified by failure).
const withRefs = (refs) => setIn({}, FIELD, refs);
const storedRefs = () => getIn(values, FIELD);
// The id cell is the only td input with aria-label "ID" (the database cell
// is a Semantic Dropdown, whose search input carries no aria-label). Rows
// are scoped to tbody to skip the header row.
const idInput = (rowIndex) =>
  container
    .querySelectorAll("tbody tr")
    [rowIndex]?.querySelector('input[aria-label="ID"]');

describe("ExternalDatabases", () => {
  it("renders one row per stored reference with database and id cells", () => {
    container = render({
      initialValues: withRefs([
        "pdb:2HCO",
        "Uniprot:P69905",
        "chembl:CHEMBL25",
      ]),
    });
    const ids = [
      ...container.querySelectorAll('tbody input[aria-label="ID"]'),
    ].map((i) => i.value);
    expect(ids).toEqual(["2HCO", "P69905", "CHEMBL25"]);
    // The selects are Semantic dropdowns (not <input type="text">): the first
    // shows the typed text of the unknown prefix verbatim.
    expect(container.textContent).toContain("chembl");
  });

  it("loading mixed-case data and doing nothing leaves the values unchanged", () => {
    container = render({
      initialValues: withRefs([
        "pdb:2HCO",
        "Uniprot:P69905",
        "chembl:CHEMBL25",
      ]),
    });
    expect(storedRefs()).toEqual([
      "pdb:2HCO",
      "Uniprot:P69905",
      "chembl:CHEMBL25",
    ]);
  });

  it("editing an id writes the reference back with a lower-case known prefix", () => {
    container = render({
      initialValues: withRefs(["Uniprot:P69905"]),
    });
    const input = idInput(0);
    input.value = "P69905X";
    act(() => {
      Simulate.change(input);
    });
    expect(storedRefs()).toEqual(["uniprot:P69905X"]);
  });

  it("shows the hint Incomplete for a half-filled row", () => {
    container = render({ initialValues: withRefs(["pdb:"]) });
    expect(container.textContent).toContain("Incomplete");
  });

  it("removing the last row leaves the key absent", () => {
    container = render({ initialValues: withRefs(["pdb:2HCO"]) });
    expect(
      container.querySelector('[aria-label="Remove row 1"]')
    ).not.toBeNull();
    act(() => {
      Simulate.click(container.querySelector('[aria-label="Remove row 1"]'));
    });
    expect(storedRefs()).toBeUndefined();
    // guide §7: not an empty array left behind
    expect(getIn(values, FIELD)).toBeUndefined();
  });

  it("the Open link appears only for known prefixes with an id", () => {
    container = render({
      initialValues: withRefs([
        "pdb:2HCO",
        "uniprot:P69905",
        "chembl:CHEMBL25",
        "pdb:",
        ":X1",
      ]),
    });
    const opens = [...container.querySelectorAll('a[rel="noreferrer"]')];
    expect(opens.map((a) => a.getAttribute("href"))).toEqual([
      "https://www.rcsb.org/structure/2HCO",
      "https://www.uniprot.org/uniprotkb/P69905",
    ]);
    expect(opens[0].getAttribute("target")).toBe("_blank");
    // unknown prefix, database-only and id-only rows have no link at all
    expect(container.textContent).not.toContain("https://chembl");
  });

  it("a string error at `<fieldPath>.0` shows on the row; an unrelated edit keeps it, editing the row drops it", async () => {
    container = render({
      initialValues: withRefs(["pdb:", "uniprot:P69905"]),
      // the error node must sit at the same nested path Formik reads
      initialErrors: setIn({}, FIELD, {
        0: "Invalid external database reference.",
      }),
    });
    expect(container.textContent).toContain(
      "Invalid external database reference."
    );
    // an unrelated edit (row 1) resets Formik `errors`, but the error's row (0)
    // is untouched, so the message must still show
    await typeInto(idInput(1), "P69905X");
    expect(container.textContent).toContain(
      "Invalid external database reference."
    );
    // editing the errored row itself makes the server error stop applying
    await typeInto(idInput(0), "2HCO");
    expect(container.textContent).not.toContain(
      "Invalid external database reference."
    );
  });
});
