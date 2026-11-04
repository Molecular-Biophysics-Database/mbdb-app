import { parseNumberInput } from "./number";

describe("parseNumberInput", () => {
  it.each([
    ["", undefined],
    ["  ", undefined],
    ["12", 12],
    ["12.5", 12.5],
    ["-1", -1],
    ["1e3", 1000],
    ["12abc", undefined],
    ["NaN", undefined],
    ["Infinity", undefined],
    [null, undefined],
    [undefined, undefined],
  ])("parses %j as %j", (raw, expected) => {
    expect(parseNumberInput(raw)).toBe(expected);
  });
});
