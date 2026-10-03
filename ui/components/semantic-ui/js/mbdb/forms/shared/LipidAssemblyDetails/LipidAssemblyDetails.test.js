import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  typeInto,
  editUnrelatedField,
  ValueProbe,
  readProbe,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { LipidAssemblyDetails, ASSEMBLY_TYPES } from "./index";

// One fake per layer: the picker needs the network, oarepo's StringArrayField
// needs a context the mbdb wrapper does not pass here. Size and Components
// stay real.
// eslint-disable-next-line no-restricted-syntax -- kept local: oarepo fake + a StringArrayField stand-in (see comment)
jest.mock("@js/oarepo_ui/forms", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const base = jest.requireActual(
    "@js/mbdb/forms/building-blocks/testUtils"
  ).oarepoFake;
  const StringArrayField = ({ fieldPath }) => {
    const { values } = useFormikContext();
    const items = getIn(values, fieldPath) ?? [];
    return R.createElement("div", { "data-testid": "specs" }, items.join(", "));
  };
  StringArrayField.propTypes = { fieldPath: PropTypesActual.string.isRequired };
  return { ...base, StringArrayField };
});

jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const FakeMbdbVocabularyField = ({ fieldPath }) => {
    const { values } = useFormikContext();
    const v = getIn(values, fieldPath);
    return R.createElement("div", {
      "data-testid": "picker",
      "data-path": fieldPath,
      "data-value": v?.id ?? v?.title?.en ?? "",
    });
  };
  FakeMbdbVocabularyField.propTypes = {
    fieldPath: PropTypesActual.string.isRequired,
  };
  return { MbdbVocabularyField: FakeMbdbVocabularyField };
});

let mockTitles = {};
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () => ({
  useVocabularyItem: (type, id) => mockTitles[`${type}/${id}`] ?? {},
  useVocabularyTitle: (type, id) => mockTitles[`${type}/${id}`]?.title,
  rememberItem: () => {},
}));

// jsdom has no WebCrypto; client-only row keys.
let mockKeyN = 0;
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => `key-${++mockKeyN}-uuid`,
}));

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const WATER_ID = "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N";

let container;

beforeEach(() => {
  mockTitles = {};
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const entity = (fields = {}) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Complex substance of chemical origin",
          class: "Lipid assembly",
          ...fields,
        },
      ],
    },
  },
});

const render = (opts) => {
  container = renderInForm(
    <>
      <LipidAssemblyDetails fieldPath={ENTITY} />
      <ValueProbe path={ENTITY} />
    </>,
    opts
  );
  return container;
};

const probe = () => readProbe(container);
const activeButtons = () =>
  [...container.querySelectorAll("button")]
    .filter((b) => b.className.includes("primary"))
    .map((b) => b.textContent);

describe("ASSEMBLY_TYPES", () => {
  it("equals the model enum", () => {
    expect(ASSEMBLY_TYPES).toEqual(yamlEnum("Lipid_assembly", "assembly_type"));
  });
});

describe("LipidAssemblyDetails", () => {
  it("renders the filled fixture at the entity paths", () => {
    render({
      initialValues: entity({
        assembly_type: "Liposome",
        number_of_mono_layers: 2,
        size: {
          type: "diameter",
          unit: "nm",
          mean: 120,
          lower: 90,
          upper: 150,
        },
        components: [
          {
            type: "Chemical",
            name: "Water",
            copy_number: -1,
            basic_information: { id: WATER_ID },
          },
        ],
      }),
    });
    expect(activeButtons()).toContain("Liposome");
    expect(
      document.getElementById(`${ENTITY}.number_of_mono_layers`).value
    ).toBe("2");
    expect(document.getElementById(`${ENTITY}.size.mean`).value).toBe("120");
    expect(container.textContent).toContain("Water");
  });

  it("accepts -1 for the mono layers; clearing removes the key", async () => {
    render({ initialValues: entity({ number_of_mono_layers: -1 }) });
    const input = () =>
      document.getElementById(`${ENTITY}.number_of_mono_layers`);
    expect(input().value).toBe("-1");
    await typeInto(input(), "");
    expect(probe().number_of_mono_layers).toBeUndefined();
  });

  it("writes under the given fieldPath, never a details level", async () => {
    render({ initialValues: entity() });
    await typeInto(
      document.getElementById(`${ENTITY}.number_of_mono_layers`),
      "3"
    );
    expect(probe().number_of_mono_layers).toBe(3);
    expect(probe().details).toBeUndefined();
  });

  it("shows an assembly_type error and keeps it after an unrelated edit", async () => {
    render({
      initialValues: entity({ name: "POPC liposomes" }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { assembly_type: "Missing data for required field." },
            ],
          },
        },
      },
      withUnrelatedField: true,
    });
    const messages = () =>
      [...container.querySelectorAll(".ui.pointing.prompt.label")].map(
        (l) => l.textContent
      );
    expect(messages()).toContain("Missing data for required field.");
    await editUnrelatedField(container);
    expect(messages()).toContain("Missing data for required field.");
  });
});
