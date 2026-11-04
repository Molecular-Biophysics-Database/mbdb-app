import { yamlEnum, modelYamlPath } from "./testUtils";

// The enum tests read the real model YAML (no copied list), so a model change
// breaks them instead of silently passing. Verified once here; block tests
// then reuse yamlEnum directly.
describe("yamlEnum", () => {
  it("modelYamlPath finds the repository's models/ folder", () => {
    expect(modelYamlPath()).toMatch(
      /models\/general_parameters-definitions-rdm\.yaml$/
    );
  });

  it("reads a top-level enum (LENGTH_UNITS), including the μ code point", () => {
    const units = yamlEnum("LENGTH_UNITS");
    expect(units).toEqual(["Å", "nm", "μm", "mm", "cm", "m"]);
    // Å is U+00C5 and μ in μm is U+03BC — the exact code points, written with
    // escapes so the source file stays plain ASCII.
    expect(units[0]).toBe("Å");
    expect(units[2]).toBe("μm");
    expect(units[2].charCodeAt(0)).toBe(0x03bc);
  });

  it("reads an enum of a property of a top-level type (Size.type)", () => {
    expect(yamlEnum("Size", "type")).toEqual([
      "radius",
      "diameter",
      "path length",
    ]);
  });

  it("throws for a type that does not exist", () => {
    expect(() => yamlEnum("DoesNotExist")).toThrow(/DoesNotExist/);
  });
});
