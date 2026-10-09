import { resolveUiNode } from "@js/mbdb/forms/building-blocks/fieldData";
import { realUiModel } from "@js/mbdb/forms/building-blocks/testUtils";
import { unfilledPaths } from "./unfilled";

// fieldData imports @js/oarepo_ui/forms (its chain reaches sanitize-html, an ESM
// package Jest cannot load); only the pure resolveUiNode is used here.
// eslint-disable-next-line no-restricted-syntax -- the shared-chain fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

// The real deposit ui_model fixture, resolved variant-aware exactly as
// useSections does (design ReviewMode.md).
const ENTITY = "metadata.general_parameters.entities_of_interest.0";
const nodeFor = (value) => {
  const values = {
    metadata: { general_parameters: { entities_of_interest: [value] } },
  };
  return resolveUiNode(realUiModel(), ENTITY, values);
};

const EXCLUDE = ["id", "type", "name"];

describe("unfilledPaths", () => {
  it("lists a Polymer's absent fields when only polymer_type is filled", () => {
    const value = {
      type: "Polymer",
      name: "Lysozyme",
      polymer_type: "polypeptide(L)",
    };
    const paths = unfilledPaths(nodeFor(value), value, { exclude: EXCLUDE });
    expect(paths).toContain("sequence");
    expect(paths).toContain("variant");
    expect(paths).toContain("external_databases");
    // present fields are not listed
    expect(paths).not.toContain("polymer_type");
    // required-and-empty (molecular_weight, expression_source_type) is Missing
    expect(paths).not.toContain("molecular_weight");
    // id and the excluded row columns are never listed
    expect(paths).not.toContain("id");
    expect(paths).not.toContain("type");
    expect(paths).not.toContain("name");
  });

  it("lists a present object's absent nested fields, not the object", () => {
    const value = {
      type: "Complex substance of biological origin",
      name: "Serum",
      derived_from: "Body fluid",
      source_organism: { id: "taxid:9606" },
      fluid: { id: "bf:2" },
      health_status: "Healthy",
      preparation_protocol: [{ name: "Centrifugation", description: "…" }],
      storage: { temperature: { value: -80, unit: "°C" } },
    };
    const paths = unfilledPaths(nodeFor(value), value, { exclude: EXCLUDE });
    expect(paths).toContain("storage.duration");
    expect(paths).toContain("storage.storage_preparation");
    expect(paths).not.toContain("storage");
  });

  it("reports an absent object as the object only", () => {
    const value = {
      type: "Complex substance of biological origin",
      name: "Serum",
      derived_from: "Body fluid",
      source_organism: { id: "taxid:9606" },
      fluid: { id: "bf:2" },
      health_status: "Healthy",
      preparation_protocol: [{ name: "Centrifugation", description: "…" }],
    };
    const paths = unfilledPaths(nodeFor(value), value, { exclude: EXCLUDE });
    expect(paths).toContain("storage");
    expect(paths).not.toContain("storage.duration");
  });

  it("does not list a required-and-empty field (it has its Missing row)", () => {
    const value = {
      type: "Complex substance of biological origin",
      name: "Biopsy",
      derived_from: "Solid tissue sample",
      source_organism: { id: "taxid:9606" },
      health_status: "healthy",
      homogenized: false,
      preparation_protocol: [{ name: "Dissection", description: "…" }],
    };
    const paths = unfilledPaths(nodeFor(value), value, { exclude: EXCLUDE });
    // organ is required for this variant -> "Missing", not "Not filled"
    expect(paths).not.toContain("organ");
  });

  it("does not walk arrays of objects", () => {
    const value = {
      type: "Molecular assembly",
      name: "Assembly",
      molecular_weight: { value: 64.5, unit: "kDa" },
      components: [{ type: "Polymer", name: "alpha", copy_number: 2 }],
    };
    const paths = unfilledPaths(nodeFor(value), value, { exclude: EXCLUDE });
    // the array is present, so nothing under it is listed
    expect(paths.some((p) => p.startsWith("components."))).toBe(false);
  });

  it("a Chemical lists only its own group fields, never the polymorphic union, and no @v", () => {
    const value = {
      type: "Chemical",
      name: "Water",
      basic_information: { id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" },
    };
    const entity = nodeFor(value);
    // collect passes only the group's fields (CHEMICAL_GROUPS), not the union
    const sub = {
      children: {
        basic_information: entity.children.basic_information,
        additional_specifications: entity.children.additional_specifications,
      },
    };
    const paths = unfilledPaths(sub, value, { exclude: EXCLUDE });
    // basic_information is a present {id} vocabulary (a leaf) -> not recursed,
    // so neither its @v/title/formula nor any other type's field is listed
    expect(paths).toEqual(["additional_specifications"]);
  });

  it("does not descend into an assessed object (the identity methods are alternatives)", () => {
    const value = {
      type: "Polymer",
      name: "X",
      polymer_type: "polypeptide(L)",
      quality_controls: {
        purity: {
          assessed: "Yes",
          method: "SDS-PAGE",
          purity_percentage: ">99 %",
        },
        identity: {
          assessed: "Yes",
          by_intact_mass: {
            method: "Mass spectrometry",
            deviation_from_expected_mass: { value: 1, unit: "kDa" },
          },
        },
      },
    };
    const entity = nodeFor(value);
    const sub = {
      children: { quality_controls: entity.children.quality_controls },
    };
    const paths = unfilledPaths(sub, value, { exclude: EXCLUDE });
    // identity is present, so it is not listed ...
    expect(paths).not.toContain("quality_controls.identity");
    // ... and its method fields (by_sequencing, by_fingerprinting) are the
    // alternatives inside it, never listed
    expect(paths.some((p) => p.includes("by_"))).toBe(false);
    // the absent sibling is still listed
    expect(paths).toContain("quality_controls.homogeneity");
  });
});
