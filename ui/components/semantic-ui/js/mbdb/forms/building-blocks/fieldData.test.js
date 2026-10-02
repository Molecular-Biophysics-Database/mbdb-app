import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { Formik } from "formik";
import { useModelFieldData } from "./fieldData";

// The real "@js/oarepo_ui/forms" index cannot load under Jest
// (sanitize-html -> postcss is ESM), and in the real app it reads the
// model from a context; here the model data is mocked directly.
// The special "missing" prefix simulates oarepo's getFieldData fallback:
// no ui_model entry, so the raw toModelPath string comes back as label
// (and helpText is null).
// kept local: this tests useModelFieldData AGAINST a fake that mimics oarepo's
// real no-entry fallback (and throws on an undefined path), behaviour the
// shared testUtils fake intentionally does not model — it is the subject
// under test, not just a dependency.
jest.mock("@js/oarepo_ui/forms", () => ({
  useFieldData: () => ({
    getFieldData: ({ fieldPath }) => {
      // Mirrors oarepo's real behaviour: toModelPath does path.split, so an
      // undefined path throws. useModelFieldData must never call it then.
      if (fieldPath == null) throw new Error("path.split of undefined");
      return fieldPath.startsWith("missing")
        ? {
            label: `children.${fieldPath.split(".").join(".children.")}`,
            helpText: null,
            required: undefined,
          }
        : {
            label: "Model label",
            helpText: "Model help",
            required: true,
          };
    },
  }),
  // reads the per-test ui_model (`testUiModel` below) the same way the real
  // form config does; undefined means "no polymorphic ui_model loaded"
  useFormConfig: () => ({ config: { ui_model: mockUiModel } }),
}));

// A small hand-written ui_model in the polymorphic shape of guide §6: the
// entities_of_interest `child` is a polymorphic node whose `children` are the
// UNION of all variants' fields; `variants[type]` carries only the fields
// that differ. The biological-origin variant is itself polymorphic
// (derived_from) with a nested variant entry.
export const TEST_UI_MODEL = {
  children: {
    metadata: {
      children: {
        general_parameters: {
          children: {
            entities_of_interest: {
              label: { en: "Entities of interest" },
              input: "array",
              children: {
                child: {
                  input: "polymorphic",
                  discriminator: "type",
                  children: {
                    id: { label: { en: "Id" }, required: true },
                    name: { label: { en: "Name" }, required: true },
                    type: { label: { en: "Type" }, required: true },
                    molecular_weight: {
                      label: { en: "Molecular weight" },
                      help: { en: "The molecular weight of the polymer" },
                      children: {
                        value: { label: { en: "Value" }, required: true },
                        unit: { label: { en: "Unit" }, required: true },
                      },
                    },
                  },
                  variants: {
                    Polymer: {},
                    "Molecular assembly": {
                      children: {
                        molecular_weight: {
                          label: { en: "Molecular weight" },
                          help: { en: "The molecular weight of the assembly" },
                        },
                      },
                    },
                    "Complex substance of biological origin": {
                      discriminator: "derived_from",
                      variants: {
                        "Solid tissue sample": {
                          children: {
                            organ: { label: { en: "Organ" }, required: true },
                          },
                        },
                        "Cell fraction": {
                          children: {
                            organ: { label: { en: "Organ" } },
                          },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
        },
      },
    },
  },
};

let mockUiModel;

const Probe = ({ path, overrides }) => {
  const data = useModelFieldData(path, overrides);
  return (
    <div>
      <span data-testid="label">{String(data.label)}</span>
      <span data-testid="helpText">{String(data.helpText)}</span>
      <span data-testid="required">{String(data.required)}</span>
    </div>
  );
};

Probe.propTypes = {
  path: PropTypes.string,
  overrides: PropTypes.object,
};

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
  mockUiModel = undefined;
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const byTestId = (id) => container.querySelector(`[data-testid="${id}"]`);

describe("useModelFieldData", () => {
  it("uses no model lookup when fieldPath is undefined (FieldGroup without a path)", () => {
    // Regression: oarepo's getFieldData crashes on an undefined path
    // (toModelPath does path.split). The hook must not call it.
    act(() => {
      ReactDOM.render(
        <Probe path={undefined} overrides={{ label: "Plain" }} />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Plain");
    expect(byTestId("helpText").textContent).toBe("undefined");
  });

  it("returns model data when no overrides given", () => {
    act(() => {
      ReactDOM.render(<Probe path="a.path" />, container);
    });
    expect(byTestId("label").textContent).toBe("Model label");
    expect(byTestId("helpText").textContent).toBe("Model help");
    expect(byTestId("required").textContent).toBe("true");
  });

  it("explicit props win over model data", () => {
    act(() => {
      ReactDOM.render(
        <Probe
          path="a.path"
          overrides={{ label: "Short", helpText: "", required: false }}
        />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Short");
    expect(byTestId("helpText").textContent).toBe("");
    expect(byTestId("required").textContent).toBe("false");
  });

  it("keeps only the keys it knows", () => {
    act(() => {
      ReactDOM.render(
        <Probe path="a.path" overrides={{ placeholder: "ignored" }} />,
        container
      );
    });
    // no crash, unknown keys are not spread into the result
    expect(byTestId("label").textContent).toBe("Model label");
  });

  it("replaces a raw ui_model path label with a readable leaf", () => {
    act(() => {
      ReactDOM.render(
        <Probe path="missing.entities_of_interest.0.chemical_formula" />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Chemical formula");
    // helpText of a missing entry stays null
    expect(byTestId("helpText").textContent).toBe("null");
  });

  it("an explicit label wins over the fallback leaf", () => {
    act(() => {
      ReactDOM.render(
        <Probe
          path="missing.entities_of_interest.0.name"
          overrides={{ label: "Name" }}
        />,
        container
      );
    });
    expect(byTestId("label").textContent).toBe("Name");
  });
});

// D7: variant-aware ui_model resolution (polymorphic union + variants). The
// hand-written TEST_UI_MODEL mimics the shape of guide §6; values at the
// entity path drive the discriminator lookups.
const FormikProbe = ({ initialValues }) => (
  <Formik initialValues={initialValues} enableReinitialize onSubmit={() => {}}>
    <Probe path="metadata.general_parameters.entities_of_interest.0.molecular_weight" />
  </Formik>
);
FormikProbe.propTypes = { initialValues: PropTypes.object };

const mountFormik = (initialValues) => {
  act(() => {
    ReactDOM.render(<FormikProbe initialValues={initialValues} />, container);
  });
};

describe("useModelFieldData with the polymorphic ui_model (D7)", () => {
  beforeEach(() => {
    mockUiModel = TEST_UI_MODEL;
  });

  it("no discriminator value → the union's node", () => {
    mountFormik({});
    expect(byTestId("helpText").textContent).toBe(
      "The molecular weight of the polymer"
    );
  });

  it("a matching variant entry wins: Molecular assembly's help", () => {
    mountFormik({
      metadata: {
        general_parameters: {
          entities_of_interest: [{ type: "Molecular assembly" }],
        },
      },
    });
    expect(byTestId("helpText").textContent).toBe(
      "The molecular weight of the assembly"
    );
  });

  it("an empty variant entry (`Polymer: {}`) → the union's node", () => {
    mountFormik({
      metadata: {
        general_parameters: {
          entities_of_interest: [{ type: "Polymer" }],
        },
      },
    });
    expect(byTestId("helpText").textContent).toBe(
      "The molecular weight of the polymer"
    );
  });

  it("nested variants resolve through two discriminators", () => {
    const withBio = (derivedFrom) => ({
      metadata: {
        general_parameters: {
          entities_of_interest: [
            {
              type: "Complex substance of biological origin",
              derived_from: derivedFrom,
            },
          ],
        },
      },
    });
    // Solid tissue sample's nested variant has organ required → union's organ
    // path resolves through the nested variant entry (its `required: true` is
    // visible at the Organ node)
    const organProbe = (values) => {
      const c = document.createElement("div");
      document.body.appendChild(c);
      act(() => {
        ReactDOM.render(
          <Formik initialValues={values} onSubmit={() => {}}>
            <Probe path="metadata.general_parameters.entities_of_interest.0.organ" />
          </Formik>,
          c
        );
      });
      const out = c.querySelector('[data-testid="required"]').textContent;
      ReactDOM.unmountComponentAtNode(c);
      c.remove();
      return out;
    };
    expect(organProbe(withBio("Solid tissue sample"))).toBe("true");
    expect(organProbe(withBio("Cell fraction"))).toBe("undefined");
  });

  it("changing the entity type in the form changes the returned help", () => {
    const values = (type) => ({
      metadata: { general_parameters: { entities_of_interest: [{ type }] } },
    });
    mountFormik(values("Molecular assembly"));
    expect(byTestId("helpText").textContent).toBe(
      "The molecular weight of the assembly"
    );
    act(() => {
      ReactDOM.render(
        <FormikProbe initialValues={values("Polymer")} />,
        container
      );
    });
    expect(byTestId("helpText").textContent).toBe(
      "The molecular weight of the polymer"
    );
  });
});
