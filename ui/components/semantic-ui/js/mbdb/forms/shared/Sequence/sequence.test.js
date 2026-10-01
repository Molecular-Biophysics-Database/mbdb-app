import { normalizeSequence, countResidues, blastUrl } from "./sequence";

describe("normalizeSequence", () => {
  // keyed on the design's Stored data table
  test.each([
    ["MIEIEKPKIE", "MIEIEKPKIE"],
    [">sp|P20429\nMIEIEK PKIE\nTVEIS", "MIEIEKPKIETVEIS"],
    // a FASTA header followed by no sequence body normalizes to absent
    [">sp|P20429", undefined],
    ["MAH LTP", "MAHLTP"],
    ["  acdef<Hy p>gh  ", "acdef<Hyp>gh"], // whitespace inside <…> stripped too; case kept
    ["", undefined],
    ["  \n", undefined],
    [undefined, undefined],
    [null, undefined],
    // %# (index) instead of %j: this jest's %j hits `jest-get-type`
    // on strings containing `<` and crashes outside the assertion
  ])("%#", (input, expected) => {
    expect(normalizeSequence(input)).toBe(expected);
  });
});

describe("countResidues", () => {
  test.each([
    ["AC<Hyp>G", 4], // letters outside <…> plus one per group
    ["MIEIEK", 6],
    ["<Hyp>", 1],
    ["<Hyp><Mse>", 2],
    ["maHl", 4], // case does not matter
    ["", 0],
    [undefined, 0],
    [null, 0],
  ])("%#", (input, expected) => {
    expect(countResidues(input)).toBe(expected);
  });
});

describe("blastUrl", () => {
  it("URL-encodes the query", () => {
    expect(blastUrl("AC<L/H>")).toBe(
      "https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins&PROGRAM=blastp&QUERY=AC%3CL%2FH%3E"
    );
  });
});
