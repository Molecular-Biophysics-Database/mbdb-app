import React from "react";
import {
  renderInForm,
  unmountForm,
  setFakeUiModel,
  clickOn,
  typeInto,
  ValueProbe,
  readProbe,
  yamlEnum,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { Components, COMPONENT_TYPES } from "./index";

// One fake per layer: the picker needs the network, oarepo's StringArrayField
// needs a context the mbdb wrapper does not pass here. The real leaves
// (PolymerFields, ChemicalFields, Modifications, QualityControls, the modal
// blocks) stay real. `useFormConfig` feeds the D7 variant test.
// eslint-disable-next-line no-restricted-syntax -- kept local: oarepo fake + a StringArrayField stand-in + a ui_model for the D7 variant (see comment)
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
    return R.createElement(
      "div",
      { "data-testid": "specs", "data-path": fieldPath },
      items.join(", ")
    );
  };
  StringArrayField.propTypes = { fieldPath: PropTypesActual.string.isRequired };
  return {
    ...base,
    StringArrayField,
    useFormConfig: () => ({ config: { ui_model: mockUiModel } }),
  };
});

// The real wrapper shows the field's merged error under the dropdown; the fake
// does the same through the shared helper, so an object-level error at
// `basic_information` still surfaces in the modal.
jest.mock("@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField", () => {
  const R = jest.requireActual("react");
  const PropTypesActual = jest.requireActual("prop-types");
  const { getIn, useFormikContext } = jest.requireActual("formik");
  const { useFieldErrors } = jest.requireActual(
    "@js/mbdb/forms/building-blocks/errors"
  );
  const FakeMbdbVocabularyField = ({ fieldPath }) => {
    const { values } = useFormikContext();
    const { messages } = useFieldErrors(fieldPath);
    const v = getIn(values, fieldPath);
    return R.createElement(
      "div",
      { "data-testid": "picker", "data-path": fieldPath },
      R.createElement(
        "span",
        { "data-testid": "picker-value" },
        v?.id ?? v?.title?.en ?? ""
      ),
      messages.length > 0 &&
        R.createElement(
          "span",
          { "data-testid": "picker-error" },
          messages.join(" ")
        )
    );
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

let mockUiModel;

const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const PATH = `${ENTITY}.components`;

let container;

beforeEach(() => {
  mockTitles = {};
  mockUiModel = undefined;
  setFakeUiModel({});
});

afterEach(() => {
  setFakeUiModel({});
  unmountForm(container);
  container = null;
});

const assembly = (components) => ({
  metadata: {
    general_parameters: {
      entities_of_interest: [
        {
          type: "Molecular assembly",
          name: "RNA polymerase",
          ...(components === undefined ? {} : { components }),
        },
      ],
    },
  },
});

const render = (opts) => {
  container = renderInForm(
    <>
      <Components fieldPath={PATH} />
      <ValueProbe path={PATH} />
    </>,
    opts
  );
  return container;
};

const probe = () => readProbe(container);

// portals stack in creation order: [outer, inner, ...]
const modals = () => [...document.body.querySelectorAll(".ui.modal")];
const modal = () => modals()[0] ?? null;
const modalButtonIn = (m, label) =>
  [...m.querySelectorAll("button")].find((b) => b.textContent === label);
const modalButton = (label) => modalButtonIn(modal(), label);

const buttonIn = (root, label) =>
  [...root.querySelectorAll("button")].find((b) => b.textContent === label);

const addOption = async (label) => {
  await clickOn(container.querySelector(".ui.dropdown"));
  const item = [...container.querySelectorAll(".menu .item")].find(
    (el) => el.textContent === label
  );
  await clickOn(item);
};

describe("COMPONENT_TYPES", () => {
  it("equals the model enum", () => {
    expect(COMPONENT_TYPES).toEqual(
      yamlEnum("Assembly_component_base", "type")
    );
  });
});

describe("Components", () => {
  it("Add → Polymer writes { type: 'Polymer' } (no id) and opens the modal with the polymer fields", async () => {
    render({ initialValues: assembly(undefined) });
    await addOption("Polymer");
    expect(probe()).toEqual([{ type: "Polymer" }]);
    expect(modal()).not.toBeNull();
    // the polymer field set is mounted inside the component modal
    expect(modal().textContent).toContain("Polymer type");
  });

  it("Add → Chemical opens the modal with the chemical fields", async () => {
    render({ initialValues: assembly(undefined) });
    await addOption("Chemical");
    expect(probe()).toEqual([{ type: "Chemical" }]);
    const picker = modal().querySelector('[data-testid="picker"]');
    expect(picker.dataset.path).toBe(`${PATH}.0.basic_information`);
  });

  it("Cancel on a new component removes it and the key (never [])", async () => {
    render({ initialValues: assembly(undefined) });
    await addOption("Polymer");
    expect(probe()).toEqual([{ type: "Polymer" }]);
    await clickOn(modalButton("Cancel"));
    expect(modal()).toBeNull();
    expect(probe()).toBeNull();
    expect(container.textContent).toContain("No items yet");
  });

  it("renders the summary row; a copy number of -1 shows 'unknown'", () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "RNA polymerase alpha subunit",
          copy_number: 2,
        },
        { type: "Chemical", name: "Zn2+", copy_number: -1 },
      ]),
    });
    expect(container.textContent).toContain("RNA polymerase alpha subunit");
    expect(container.textContent).toContain("Polymer");
    expect(container.textContent).toContain("unknown");
  });

  it("a type change keeps name and copy number and drops only the variant data", async () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "Mg2+ cofactor",
          copy_number: 2,
          polymer_type: "polypeptide(L)",
        },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    await clickOn(buttonIn(modal(), "Chemical"));
    const confirm = modals().find((m) =>
      m.textContent.includes("The type-specific data will be removed.")
    );
    expect(confirm).not.toBeNull();
    await clickOn(modalButtonIn(confirm, "Change"));
    expect(probe()).toEqual([
      { type: "Chemical", name: "Mg2+ cofactor", copy_number: 2 },
    ]);
  });

  it("▸ on a polymer row shows the polymer groups without Name/Type/Copy number", async () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "RNA polymerase alpha subunit",
          copy_number: 2,
          polymer_type: "polypeptide(L)",
          expression_source_type: "Recombinantly",
        },
      ]),
    });
    const toggle = container.querySelector(
      'button[aria-label^="Show details of"]'
    );
    expect(toggle).not.toBeNull();
    await clickOn(toggle);
    const details = container.querySelector("tr.mbdb-details");
    expect(details).not.toBeNull();
    expect(details.textContent).toContain("polypeptide(L)");
    // Name/Type/Copy number are already in the row (detailProps.exclude)
    expect(details.textContent).not.toContain("RNA polymerase alpha subunit");
  });

  it("shows the row error badge and the message at Basic information", async () => {
    render({
      initialValues: assembly([
        { type: "Polymer", name: "alpha", copy_number: 1 },
        { type: "Polymer", name: "beta", copy_number: 1 },
        { type: "Chemical", name: "Zn2+", copy_number: -1 },
      ]),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                components: [
                  {},
                  {},
                  { basic_information: "Missing data for required field." },
                ],
              },
            ],
          },
        },
      },
    });
    expect(container.textContent).toContain("1 error");
    const badge = [...container.querySelectorAll(".ui.red.label")].find((l) =>
      l.textContent.includes("error")
    );
    await clickOn(badge);
    expect(modal().textContent).toContain("Missing data for required field.");
  });

  it("renders a polymer component's Modifications and QualityControls inline (no third modal)", async () => {
    render({
      initialValues: assembly([
        {
          type: "Polymer",
          name: "alpha",
          copy_number: 1,
          modifications: {
            chemical: [{ type: "Phosphorylation", position: "S10" }],
          },
          quality_controls: { purity: { assessed: "No" } },
        },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    expect(modals()).toHaveLength(1);
    const text = modal().textContent;
    expect(text).toContain("Modifications");
    expect(text).toContain("Quality controls");
  });

  it("reuses PolymerFields at the component path: typing a variant writes there", async () => {
    render({
      initialValues: assembly([
        { type: "Polymer", name: "alpha", copy_number: 1 },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    await typeInto(
      modal().querySelector(`input[name="${PATH}.0.variant"]`),
      "V2A"
    );
    expect(probe()[0].variant).toBe("V2A");
  });

  it("depth 2: Cancel on a component restores only that component", async () => {
    container = renderInForm(
      <>
        <ModalArrayField
          fieldPath="entities"
          label="Entities"
          itemLabel={(v) => `entity: ${v?.name ?? "new"}`}
          columns={[{ label: "Name", value: (v) => v.name }]}
          renderForm={(p) => <Components fieldPath={`${p}.components`} />}
        />
        <ValueProbe path="entities" />
      </>,
      {
        initialValues: {
          entities: [
            {
              type: "Molecular assembly",
              name: "RNA polymerase",
              components: [{ type: "Polymer", name: "alpha", copy_number: 1 }],
            },
          ],
        },
      }
    );
    await clickOn(buttonIn(container, "Edit"));
    expect(modal().textContent).toContain("Edit entity: RNA polymerase");
    await clickOn(buttonIn(modal(), "Edit"));
    expect(modals()).toHaveLength(2);
    const inner = () => modals()[1];
    await typeInto(
      inner().querySelector('input[name="entities.0.components.0.name"]'),
      "renamed"
    );
    expect(readProbe(container)[0].components[0].name).toBe("renamed");
    await clickOn(modalButtonIn(inner(), "Cancel"));
    expect(modals()).toHaveLength(1);
    expect(readProbe(container)[0].components[0].name).toBe("alpha");
  });

  it("uses the Assembly_component name help, not the entity's (D7)", async () => {
    mockUiModel = {
      children: {
        metadata: {
          children: {
            general_parameters: {
              children: {
                entities_of_interest: {
                  children: {
                    child: {
                      children: {
                        components: {
                          children: {
                            child: {
                              children: {
                                name: {
                                  label: { en: "Name" },
                                  help: { en: "Union component name help" },
                                },
                              },
                              discriminator: "type",
                              variants: {
                                Polymer: {
                                  children: {
                                    name: {
                                      label: { en: "Name" },
                                      help: {
                                        en: "The name must be unique within a record",
                                      },
                                    },
                                  },
                                },
                              },
                            },
                          },
                        },
                      },
                      discriminator: "type",
                      variants: { "Molecular assembly": { children: {} } },
                    },
                  },
                },
              },
            },
          },
        },
      },
    };
    render({
      initialValues: assembly([
        { type: "Polymer", name: "alpha", copy_number: 1 },
      ]),
    });
    await clickOn(buttonIn(container, "Edit"));
    const text = modal().textContent;
    expect(text).toContain("The name must be unique within a record");
    expect(text).not.toContain("Union component name help");
  });
});
