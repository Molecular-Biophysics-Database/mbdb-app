import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext } from "formik";
import { DetailView } from "./DetailView";
import { setFakeVocabulary } from "@js/mbdb/forms/building-blocks/testUtils";

// @js/oarepo_ui/forms/index pulls in react-searchkit (d3, ESM) and
// sanitize-html (postcss, ESM), which Jest cannot load — same class of
// problem as the @js/mbdb/forms index. The mock provides the two providers
// and the subset of getFieldData the blocks use ("text" representation).
// kept local: it reproduces oarepo's real toModelPath traversal (nested
// children.X.children, array child.children) reading a nested ui_model — the
// DetailView label tests depend on that resolution, which testUtils' flat
// per-path map deliberately does not re-implement.
// eslint-disable-next-line no-restricted-syntax -- kept local: reproduces oarepo's real toModelPath traversal over a nested ui_model (see comment above)
jest.mock("@js/oarepo_ui/forms", () => {
  const R = jest.requireActual("react");
  const get = jest.requireActual("lodash/get");
  const Ctx = R.createContext();
  const toModelPath = (path) =>
    path
      .split(".")
      .map((part, i, parts) => {
        if (i === 0) return `children.${part}.children`;
        if (i === parts.length - 1) return part;
        if (!Number.isNaN(Number.parseInt(part))) return "child.children";
        return Number.isNaN(Number.parseInt(parts[i + 1]))
          ? `${part}.children`
          : part;
      })
      .join(".");
  const getFieldData =
    (uiModel) =>
    ({ fieldPath }) => {
      const path = toModelPath(fieldPath);
      const data = get(uiModel, path) || {};
      return {
        label: data.label?.en ?? path,
        helpText: data.help?.en ?? null,
        placeholder: data.hint?.en ?? null,
        required: data.required,
      };
    };
  // eslint-disable-next-line react/prop-types -- inline test mock
  const FormConfigProvider = ({ children, value }) => (
    <Ctx.Provider value={{ ...value, getFieldData }}>{children}</Ctx.Provider>
  );
  return {
    FormConfigProvider,
    FieldDataProvider: ({ children }) => children,
    useFieldData: () => ({
      getFieldData: R.useContext(Ctx).getFieldData(
        R.useContext(Ctx).config.ui_model
      ),
    }),
  };
});
// Vocabulary titles are resolved by group-declared entries ({ field,
// vocabulary }); the shared synchronous cache is seeded with the
// title the tests expect.
jest.mock("@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockVocabularyTitles()
);

beforeEach(() => {
  setFakeVocabulary({
    "organisms/bacillus": { title: "Bacillus subtilis" },
  });
});

afterEach(() => {
  setFakeVocabulary();
});

const { FormConfigProvider, FieldDataProvider } = jest.requireMock(
  "@js/oarepo_ui/forms"
);

const uiModel = {
  children: {
    o: {
      children: {
        name: { label: { en: "Name" } },
        polymer_type: { label: { en: "Polymer type" } },
        homogenized: { label: { en: "Homogenized" } },
        molecular_weight: { label: { en: "Molecular weight" } },
        sequence: { label: { en: "Sequence" } },
        source_organism: { label: { en: "Source organism" } },
        specifications: { label: { en: "Specifications" } },
        location: {
          label: { en: "Location" },
          children: {
            latitude: { label: { en: "Latitude" } },
            longitude: { label: { en: "Longitude" } },
          },
        },
        storage: {
          label: { en: "Storage" },
          children: {
            temperature: { label: { en: "Temperature" } },
            duration: { label: { en: "Duration" } },
          },
        },
        components: {
          label: { en: "Components" },
          child: {
            children: {
              name: { label: { en: "Name" } },
              copy_number: { label: { en: "Copy number" } },
            },
          },
        },
      },
    },
  },
};

const GROUPS = [
  {
    title: "Identification",
    fields: ["name", "polymer_type", "homogenized"],
  },
  { title: "Sequence", fields: ["sequence"] },
  { title: "Origin", fields: ["source_organism"] },
];

let container;

const mount = (ui, { initialValues = {}, initialErrors = {} } = {}) => {
  container = document.createElement("div");
  document.body.appendChild(container);
  act(() => {
    ReactDOM.render(
      <FormConfigProvider value={{ config: { ui_model: uiModel } }}>
        <FieldDataProvider>
          <Formik
            initialValues={initialValues}
            initialErrors={initialErrors}
            onSubmit={() => {}}
          >
            {ui}
          </Formik>
        </FieldDataProvider>
      </FormConfigProvider>,
      container
    );
  });
};

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const text = () => container.textContent;

const FILLED = {
  o: {
    name: "Lysozyme",
    polymer_type: "polypeptide(L)",
    homogenized: true,
    molecular_weight: { value: 14.3, unit: "kDa" },
    sequence:
      "MIEIEKPKIETVEISDDAKFGKFVVEPLERGYGTTLGNSLRRAAGKNTVTLAEQMKRIDELSQG",
    source_organism: { id: "bacillus" },
    specifications: ["RNase-free", "desalted"],
  },
};

describe("DetailView", () => {
  it("renders nothing for an absent value", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: {},
    });
    expect(container.querySelector("table")).toBeNull();
    expect(text()).not.toContain("Nothing filled in yet");
  });

  it("shows 'Nothing filled in yet' for an object without data", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: { o: {} },
    });
    expect(text()).toContain("Nothing filled in yet");
  });

  it("renders grouped rows with model labels and formatted values", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: FILLED,
    });
    expect(text()).toContain("Identification");
    expect(text()).toContain("Polymer type");
    expect(text()).toContain("polypeptide(L)");
    expect(text()).toContain("Homogenized");
    expect(text()).toContain("Yes");
    expect(text()).toContain("Molecular weight");
    expect(text()).toContain("14.3 kDa");
    expect(text()).toContain("Identification");
  });

  it("formats a sequence monospace with the residue count", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: FILLED,
    });
    const code = container.querySelector("code");
    expect(code).not.toBeNull();
    expect(code.textContent).toHaveLength(60);
    expect(text()).toContain(`(${FILLED.o.sequence.length} residues)`);
  });

  it("resolves a declared { field, vocabulary } entry through the shared title cache", () => {
    // group spec with a vocabulary declaration; `useVocabularyTitle` is
    // mocked at the top of the file to return the cached title synchronously
    mount(
      <DetailView
        fieldPath="o"
        groups={[
          { title: "Identification", fields: ["name"] },
          {
            title: "Origin",
            fields: [{ field: "source_organism", vocabulary: "organisms" }],
          },
        ]}
      />,
      { initialValues: FILLED }
    );
    expect(text()).toContain("Bacillus subtilis");
    // specifications is in no group: listed under "Other"
    expect(text()).toContain("Other");
    expect(text()).toContain("RNase-free, desalted");
    expect(text()).toContain("Molecular weight");
  });

  it("shows the raw id (no crash) while the title is still loading", () => {
    setFakeVocabulary();
    mount(
      <DetailView
        fieldPath="o"
        groups={[
          {
            title: "Origin",
            fields: [{ field: "source_organism", vocabulary: "organisms" }],
          },
        ]}
      />,
      { initialValues: FILLED }
    );
    expect(text()).toContain("bacillus");
  });

  it("marks a manual chemical title (i18n dict) with a Manual entry hint", () => {
    mount(
      <DetailView
        fieldPath="o"
        groups={[{ title: "Chemical", fields: ["basic_information"] }]}
      />,
      {
        initialValues: {
          o: { basic_information: { title: { en: "my lipid mix" } } },
        },
      }
    );
    expect(text()).toContain("my lipid mix");
    expect(text()).toContain("Manual entry");
  });

  it("hides empty fields and omits all-empty groups", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: { o: { name: "X", polymer_type: "" } },
    });
    expect(text()).toContain("Name");
    expect(text()).toContain("X");
    expect(text()).not.toContain("Polymer type");
    expect(text()).not.toContain("Sequence"); // all-empty group left out
  });

  it("marks required-but-absent fields as red Missing", () => {
    mount(
      <DetailView fieldPath="o" groups={GROUPS} requiredPaths={["name"]} />,
      { initialValues: { o: { polymer_type: "polypeptide(L)" } } }
    );
    expect(text()).toContain("Name");
    expect(text()).toContain("Missing");
    expect(container.querySelector(".ui.red.label").textContent).toBe(
      "Missing"
    );
  });

  it("shows the field error under the value in red", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: { o: { name: "" } },
      initialErrors: { o: { name: "Missing data for required field." } },
    });
    expect(container.querySelector(".mbdb-error-text").textContent).toBe(
      "Missing data for required field."
    );
  });

  it("flattens nested objects one indent level under a sub-heading", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: {
          storage: {
            temperature: { value: -80, unit: "°C" },
            duration: { value: 3, unit: "months" },
          },
        },
      },
    });
    // the sub-heading uses the model label, not the raw key
    expect(text()).toContain("Storage"); // sub-heading (model label)
    expect(text()).toContain("Temperature");
    expect(text()).toContain("-80 °C");
    const indent = container.querySelectorAll("td.mbdb-details-indent");
    expect(indent.length).toBe(2); // both leaf rows indented one level
  });

  it("excludes summary fields listed in exclude", () => {
    mount(<DetailView fieldPath="o" groups={GROUPS} exclude={["name"]} />, {
      initialValues: FILLED,
    });
    expect(text()).not.toContain("Lysozyme");
    expect(text()).toContain("polypeptide(L)");
  });

  it("shows an array of complex objects as a mini table with its own toggle", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: {
          components: [
            { name: "Water", copy_number: 2 },
            { name: "NaCl", copy_number: 1 },
          ],
        },
      },
    });
    expect(text()).toContain("Water");
    expect(text()).toContain("NaCl");
    // the mini table has a header row with the model labels
    const head = container.querySelector("table table thead");
    expect(head).not.toBeNull();
    expect(head.textContent).toContain("Name");
    expect(head.textContent).toContain("Copy number");
    // expanding a mini row renders its details inline
    const toggles = container.querySelectorAll(
      'button[aria-label^="Show details of item"]'
    );
    expect(toggles).toHaveLength(2);
    act(() => Simulate.click(toggles[0]));
    expect(text()).toContain("Copy number");
  });
});

// A Formik-connected input for an unrelated field, so Simulate.change drives
// Formik's setFieldValue (and its async errors reset) — used by the errors-after-edit test.
const UnrelatedInput = () => {
  const { values, setFieldValue } = useFormikContext();
  return (
    <input
      data-testid="other"
      value={values.other ?? ""}
      onChange={(e) => setFieldValue("other", e.target.value)}
    />
  );
};

describe("DetailView — review findings", () => {
  it("keeps the error text after an unrelated edit clears Formik's errors (F1)", async () => {
    mount(
      <>
        <DetailView fieldPath="o" groups={GROUPS} />
        <UnrelatedInput />
      </>,
      {
        initialValues: { o: { name: "" }, other: "" },
        initialErrors: { o: { name: "Missing data for required field." } },
      }
    );
    expect(container.querySelector(".mbdb-error-text").textContent).toBe(
      "Missing data for required field."
    );

    const other = container.querySelector('[data-testid="other"]');
    other.value = "changed";
    await act(async () => Simulate.change(other));
    expect(container.querySelector(".mbdb-error-text").textContent).toBe(
      "Missing data for required field."
    );
  });

  it("renders an Edit button and a clickable error message when onEdit is given (F2)", () => {
    const onEdit = jest.fn();
    mount(
      <DetailView
        fieldPath="o"
        groups={GROUPS}
        onEdit={onEdit}
        itemName="Storage"
      />,
      {
        initialValues: { o: { name: "" } },
        initialErrors: { o: { name: "Missing data for required field." } },
      }
    );
    const editBtn = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "Edit Storage"
    );
    expect(editBtn).not.toBeUndefined();
    expect(editBtn.getAttribute("type")).toBe("button");

    // the error note is clickable and routes to onEdit
    const errNote = container.querySelector("button.mbdb-error-text");
    expect(errNote).not.toBeNull();
    act(() => Simulate.click(errNote));
    expect(onEdit).toHaveBeenCalledTimes(1);
  });

  it("renders steps as a numbered list name — description (F4a)", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: {
          protocol: [
            { name: "Centrifugation", description: "10 min at 4000 g" },
            { name: "Filtration", description: "0.22 µm filter" },
          ],
        },
      },
    });
    expect(text()).toContain("1. Centrifugation — 10 min at 4000 g");
    expect(text()).toContain("2. Filtration — 0.22 µm filter");
    // a numbered list, not a mini table
    expect(container.querySelector("table table")).toBeNull();
  });

  it("renders a string array of more than 5 items as a bulleted list (F4b)", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: { specifications: ["a", "b", "c", "d", "e", "f"] },
      },
    });
    const items = container.querySelectorAll("ul li");
    expect(items.length).toBe(6);
  });

  it("renders a short string array comma-separated, not bulleted (F4b)", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: { o: { specifications: ["a", "b"] } },
    });
    expect(container.querySelectorAll("ul li").length).toBe(0);
    expect(text()).toContain("a, b");
  });

  it("renders an assessed object as Yes — facts on one line (F4c)", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: {
          purity: { assessed: "Yes", method: "SDS-PAGE", percentage: ">95 %" },
          identity: { assessed: "No" },
        },
      },
    });
    expect(text()).toContain("Yes — SDS-PAGE, >95 %");
    expect(text()).toContain("No");
  });

  // S4 (2026-10-03): nested objects inside an assessed value
  it("expands nested objects of an assessed value one level", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: {
          identity: {
            assessed: "Yes",
            by_intact_mass: {
              method: "Mass spectrometry",
              deviation_from_expected_mass: { value: 0.5, unit: "Da" },
            },
            by_sequencing: { method: "Sanger sequencing", percentage: 98 },
          },
        },
      },
    });
    expect(text()).toContain(
      "Yes — by intact mass: Mass spectrometry, 0.5 Da; by sequencing: Sanger sequencing, 98"
    );
  });

  it("renders an assessed value whose nested facts are all empty as plain Yes", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: { identity: { assessed: "Yes", by_fingerprinting: {} } },
      },
    });
    expect(text()).toContain("Yes");
    expect(text()).not.toContain("Yes —");
  });

  it("expands a long sequence with the Show all toggle (F4d)", () => {
    const seq = FILLED.o.sequence.repeat(3); // 192 residues > 60
    mount(<DetailView fieldPath="o" groups={GROUPS} />, {
      initialValues: { o: { sequence: seq } },
    });
    const toggle = [...container.querySelectorAll("button")].find(
      (b) => b.textContent === "[Show all]"
    );
    expect(toggle).not.toBeUndefined();
    act(() => Simulate.click(toggle));
    const code = container.querySelector("code");
    expect(code.textContent.replace(/\n/g, "")).toBe(seq);
  });

  it("falls back to the record's own title and shows a saved rank in grey (F8)", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: {
          source_organism: {
            id: "taxid:1423",
            rank: "SPECIES",
            title: { en: "Bacillus subtilis" },
          },
        },
      },
    });
    expect(text()).toContain("Bacillus subtilis");
    expect(text()).toContain("(SPECIES)");
    expect(container.querySelector(".mbdb-muted-text").textContent).toContain(
      "SPECIES"
    );
  });
});

describe("DetailView formatters", () => {
  it("external_databases: a known prefix becomes a link, an unknown one stays text", () => {
    mount(
      <DetailView
        fieldPath="o"
        groups={[{ title: "Refs", fields: ["external_databases"] }]}
      />,
      {
        initialValues: {
          o: {
            external_databases: ["pdb:1GWD", "weird:1", "Uniprot:P00698"],
          },
        },
      }
    );
    expect(
      [...container.querySelectorAll("a")].map((a) => a.getAttribute("href"))
    ).toEqual([
      "https://www.rcsb.org/structure/1GWD",
      "https://www.uniprot.org/uniprotkb/P00698",
    ]);
    // the unknown prefix is not hidden: it stays as plain text
    expect(text()).toContain("weird:1");
  });

  it("location: one line of coordinates plus the map link", () => {
    mount(
      <DetailView
        fieldPath="o"
        groups={[{ title: "Where", fields: ["location"] }]}
      />,
      {
        initialValues: {
          o: {
            location: { latitude: 49.1951, longitude: 16.6068, altitude: 237 },
          },
        },
      }
    );
    expect(text()).toContain("49.1951, 16.6068, 237 m");
    expect(container.querySelector("a").getAttribute("href")).toBe(
      "https://www.openstreetmap.org/?mlat=49.1951&mlon=16.6068#map=10/49.1951/16.6068"
    );
  });

  it("basic_information: the title plus the cached formula, weight and id", () => {
    setFakeVocabulary({
      "chemicals/inchikey:WATER": {
        title: "Water",
        customFields: {
          chemical_formula: "H2O",
          molecular_weight: { value: 18.02, unit: "g/mol" },
        },
      },
    });
    mount(
      <DetailView
        fieldPath="o"
        groups={[{ title: "Chemical", fields: ["basic_information"] }]}
      />,
      { initialValues: { o: { basic_information: { id: "inchikey:WATER" } } } }
    );
    expect(text()).toContain("Water");
    // formula, molecular weight and the InChIKey id are shown, not hidden
    expect(text()).toContain("H2O · 18.02 g/mol · inchikey:WATER");
  });

  it("basic_information: a manual chemical shows its typed title and the hint", () => {
    mount(
      <DetailView
        fieldPath="o"
        groups={[{ title: "Chemical", fields: ["basic_information"] }]}
      />,
      {
        initialValues: {
          o: { basic_information: { title: { en: "my lipid mix" } } },
        },
      }
    );
    expect(text()).toContain("my lipid mix");
    expect(text()).toContain("Manual entry");
  });
});
