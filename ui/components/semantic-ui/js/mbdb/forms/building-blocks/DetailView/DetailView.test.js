import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik } from "formik";
import { DetailView } from "./DetailView";

// @js/oarepo_ui/forms/index pulls in react-searchkit (d3, ESM) and
// sanitize-html (postcss, ESM), which Jest cannot load — same class of
// problem as the @js/mbdb/forms index. The mock provides the two providers
// and the subset of getFieldData the blocks use ("text" representation).
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

  it("resolves vocabulary ids through the title map and lists ungrouped keys under Other", () => {
    mount(
      <DetailView
        fieldPath="o"
        groups={GROUPS}
        vocabularyTitles={{ bacillus: "Bacillus subtilis" }}
      />,
      { initialValues: FILLED }
    );
    expect(text()).toContain("Bacillus subtilis");
    // specifications is in no group
    expect(text()).toContain("Other");
    expect(text()).toContain("RNase-free, desalted");
    // molecular_weight is also ungrouped
    expect(text()).toContain("Molecular weight");
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
    expect(container.querySelector(".ui.red.text").textContent).toBe(
      "Missing data for required field."
    );
  });

  it("flattens nested objects one indent level under a sub-heading", () => {
    mount(<DetailView fieldPath="o" groups={[]} />, {
      initialValues: {
        o: { location: { latitude: 49.1, longitude: 16.6 } },
      },
    });
    expect(text()).toContain("location"); // sub-heading
    expect(text()).toContain("Latitude");
    expect(text()).toContain("49.1");
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
    // expanding a mini row renders its details inline
    const toggles = container.querySelectorAll(
      'button[aria-label^="Show details of item"]'
    );
    expect(toggles).toHaveLength(2);
    act(() => Simulate.click(toggles[0]));
    expect(text()).toContain("Copy number");
  });
});
