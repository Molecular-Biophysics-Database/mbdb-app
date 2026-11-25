import { KNOWN_DATABASES, parseRef, formatRef, refUrl } from "./refs";

describe("parseRef", () => {
  test.each([
    ["Uniprot:P69905", { database: "uniprot", id: "P69905" }],
    ["PDB:1GWD", { database: "pdb", id: "1GWD" }], // known prefix lower-cased on read
    ["pdb:1ABC:A", { database: "pdb", id: "1ABC:A" }], // split at first colon only
    ["chembl:CHEMBL25", { database: "chembl", id: "CHEMBL25" }],
    ["EMDB:EMD-1", { database: "EMDB", id: "EMD-1" }], // unknown: kept as typed
    ["pdb:", { database: "pdb", id: "" }], // half row: database only
    [":P69905", { database: "", id: "P69905" }], // half row: id only
    ["", { database: "", id: "" }],
    [undefined, { database: "", id: "" }],
    [null, { database: "", id: "" }],
    // a reference with no colon at all: treat the whole string as the id — the
    // database is unknown/empty, and the user sees it in the ID cell rather
    // than vanishing into an unparseable prefix
    ["P69905", { database: "", id: "P69905" }],
  ])("%j -> %j", (input, expected) => {
    expect(parseRef(input)).toEqual(expected);
  });
});

describe("formatRef", () => {
  test.each([
    [{ database: "", id: "" }, ""],
    [{}, ""], // never write ":" via defaults
    [undefined, ""],
    [{ database: "pdb" }, "pdb:"], // one side only
    [{ id: "P69905" }, ":P69905"], // the server decides; no typing is lost
    [{ database: "pdb", id: "1GWD" }, "pdb:1GWD"],
    [{ database: "chembl", id: "CHEMBL25" }, "chembl:CHEMBL25"],
  ])("%j -> %j", (input, expected) => {
    expect(formatRef(input)).toBe(expected);
  });
});

describe("refUrl", () => {
  it("builds URLs for both known prefixes", () => {
    expect(refUrl({ database: "pdb", id: "1GWD" })).toBe(
      "https://www.rcsb.org/structure/1GWD"
    );
    expect(refUrl({ database: "uniprot", id: "P69905" })).toBe(
      "https://www.uniprot.org/uniprotkb/P69905"
    );
  });

  it("returns null for an unknown prefix or a missing id", () => {
    expect(refUrl({ database: "chembl", id: "CHEMBL25" })).toBeNull();
    expect(refUrl({ database: "pdb", id: "" })).toBeNull();
    expect(refUrl({ database: "", id: "" })).toBeNull();
  });

  it("URL-encodes the id", () => {
    const make = KNOWN_DATABASES.pdb;
    expect(make("1/A")).toBe("https://www.rcsb.org/structure/1%2FA");
  });
});

describe("parseRef→formatRef round-trip", () => {
  // %# (index): this jest's %j crashes on the `:`/`mixed-case` row names
  // Canonical (lower-case known prefix or unknown) strings round-trip to
  // themselves — the story fixtures all do except the mixed-case one. Stored
  // values stay byte-identical when untouched because the table never
  // serializes a row back except on a cell edit (component test).
  test.each([["pdb:2HCO"], ["chembl:CHEMBL25"], ["pdb:1ABC:A"]])(
    "%# stays identity",
    (stored) => {
      expect(formatRef(parseRef(stored))).toBe(stored);
    }
  );

  it("a mixed-case known prefix is written in lower case on the first edit", () => {
    // design Stored data: load "Uniprot:P69905", edit the ID → "uniprot:…"
    expect(formatRef(parseRef("Uniprot:P69905"))).toBe("uniprot:P69905");
  });
});
