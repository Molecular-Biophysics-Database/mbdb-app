import { buildQuery } from "./query";

const fields = [
  { path: "t", kind: "words" },
  { path: "o", kind: "text" },
  { path: "e", kind: "enum" },
  { path: "n", kind: "number" },
];
const row = (path, operator, value, rest = {}) => ({
  join: "AND",
  open: false,
  close: false,
  path,
  operator,
  value,
  value2: "",
  ...rest,
});
const build = (...rows) => buildQuery(rows, fields);

describe("buildQuery", () => {
  it.each([
    [row("t", "contains", "rna"), 't.words:"rna"'],
    [row("t", "is", 'a "b" \\c'), 't:"a \\"b\\" \\\\c"'],
    [row("o", "contains", "coli"), 'o:"coli"'],
    [row("n", "is", "-5"), "n:[-5 TO -5]"],
    [row("n", "from", "20"), "n:[20 TO *]"],
    [row("n", "to", "20"), "n:[* TO 20]"],
    [row("n", "between", "1", { value2: "2" }), "n:[1 TO 2]"],
    [row("e", "is", "x", { join: "AND NOT" }), '(NOT e:"x")'],
  ])("builds one condition", (condition, expected) => {
    expect(build(condition)).toBe(expected);
  });

  it("combines left to right", () => {
    expect(
      build(
        row("e", "is", "a"),
        row("e", "is", "b", { join: "OR" }),
        row("e", "is", "c", { join: "AND NOT" })
      )
    ).toBe('((e:"a" OR e:"b") AND NOT e:"c")');
  });

  it("respects brackets", () => {
    expect(
      build(
        row("e", "is", "a"),
        row("e", "is", "b", { join: "AND NOT", open: true }),
        row("e", "is", "c", { join: "OR", close: true })
      )
    ).toBe('(e:"a" AND NOT (e:"b" OR e:"c"))');
  });

  it.each([
    [[row("e", "is", " ")], /not filled/],
    [[row("", "is", "a")], /not filled/],
    [[row("n", "between", "1")], /not filled/],
    [[row("e", "is", "a", { close: true })], /not open/],
    [[row("e", "is", "a", { open: true })], /not closed/],
  ])("rejects broken conditions", (rows, message) => {
    expect(() => build(...rows)).toThrow(message);
  });
});
