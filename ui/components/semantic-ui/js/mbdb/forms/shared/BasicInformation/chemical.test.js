import { isManualChemical, describeChemical, chemicalLinks } from "./chemical";

describe("isManualChemical", () => {
  it("is false for an absent value", () => {
    expect(isManualChemical(undefined)).toBe(false);
    expect(isManualChemical(null)).toBe(false);
  });

  it("is false for a picked term (has an id)", () => {
    expect(
      isManualChemical({ id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" })
    ).toBe(false);
  });

  it("is true for a manual value (data, no id)", () => {
    expect(isManualChemical({ title: { en: "my lipid mix" } })).toBe(true);
    expect(
      isManualChemical({
        title: { en: "my lipid mix" },
        chemical_formula: "C42H82NO8P",
      })
    ).toBe(true);
  });

  it("is false for an empty object (no data yet)", () => {
    expect(isManualChemical({})).toBe(false);
  });
});

describe("describeChemical", () => {
  it("joins formula and molecular weight with ·", () => {
    expect(
      describeChemical({
        custom_fields: {
          chemical_formula: "KH2PO4",
          molecular_weight: { value: 136.086, unit: "g/mol" },
        },
      })
    ).toBe("KH2PO4 · 136.086 g/mol");
  });

  it("skips missing parts without dangling separators", () => {
    expect(
      describeChemical({ custom_fields: { chemical_formula: "H2O" } })
    ).toBe("H2O");
    expect(
      describeChemical({
        custom_fields: { molecular_weight: { value: 18.02, unit: "g/mol" } },
      })
    ).toBe("18.02 g/mol");
    expect(
      describeChemical({
        custom_fields: { molecular_weight: { value: 18.02 } },
      })
    ).toBe("18.02");
  });

  it("returns undefined with no facts at all", () => {
    expect(describeChemical({ custom_fields: {} })).toBeUndefined();
    expect(describeChemical({})).toBeUndefined();
    expect(describeChemical(undefined)).toBeUndefined();
  });
});

describe("chemicalLinks", () => {
  it("builds PubChem and ChEMBL hash-query links from the title", () => {
    const links = chemicalLinks({ title: { en: "Sodium Chloride" } });
    expect(links).toHaveLength(2);
    expect(links[0].href).toBe(
      "https://pubchem.ncbi.nlm.nih.gov/#query=Sodium%20Chloride"
    );
    expect(links[1].href).toBe(
      "https://www.ebi.ac.uk/chembl/g/#search_results/all/query=Sodium%20Chloride"
    );
    expect(links.map((l) => l.label)).toEqual(["PubChem ↗", "ChEMBL ↗"]);
  });

  it("falls back to the id when there is no title", () => {
    const links = chemicalLinks({ id: "inchikey:ABC" });
    expect(links[0].href).toContain("#query=inchikey%3AABC");
  });

  it("returns no links for a value with neither title nor id", () => {
    expect(chemicalLinks({ chemical_formula: "H2O" })).toEqual([]);
    expect(chemicalLinks(undefined)).toEqual([]);
  });
});
