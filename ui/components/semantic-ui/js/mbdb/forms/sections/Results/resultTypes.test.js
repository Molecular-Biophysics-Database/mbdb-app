import { yamlEnum } from "@js/mbdb/forms/building-blocks/testUtils";
import {
  CONCENTRATION_UNITS,
  ENERGY_UNITS,
} from "@js/mbdb/forms/shared/units";
import { RESULT_UNITS, SIZE_TYPES, resultSeed } from "./resultTypes";

jest.mock("@js/oarepo_ui/forms", () => ({}));

describe("result types match the model", () => {
  it("types and shared units", () => {
    expect(Object.keys(RESULT_UNITS).sort()).toEqual(
      yamlEnum("Result_base", "type").sort()
    );
    expect(CONCENTRATION_UNITS).toEqual(yamlEnum("CONCENTRATION_UNITS"));
    expect(ENERGY_UNITS).toEqual(yamlEnum("ENERGY_UNITS"));
    expect(SIZE_TYPES).toEqual(
      yamlEnum("Size_spherical_representation", "size_type")
    );
  });

  it.each([
    ["Constant of association KA", "Result_KA"],
    ["Constant of dissociation KD", "Result_KD"],
    ["Association rate kOn", "Result_kOn"],
    ["Dissociation rate kOff", "Result_kOff"],
    ["Change in entropy deltaS", "Result_deltaS"],
    ["Hill coefficient", "Result_hill_coeff"],
    ["Correction of active concentration", "Active_concentration_correction"],
  ])("%s units", (type, yamlType) => {
    expect(RESULT_UNITS[type]).toEqual(yamlEnum(yamlType, "unit"));
  });

  it("seeds the unit only when there is one choice", () => {
    expect(resultSeed("Hill coefficient")).toEqual({ unit: "unitless" });
    expect(resultSeed("Concentration")).toEqual({});
    expect(resultSeed("Stoichiometry")).toEqual({});
  });
});
