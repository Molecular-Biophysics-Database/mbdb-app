import {
  countErrors,
  hasError,
  errorMessages,
  isEmptyValue,
  hasData,
} from "./errors";

describe("errors helpers", () => {
  const errors = {
    metadata: {
      name: "Missing data for required field.",
      list: [
        { id: "Not a valid identifier.", title: "" },
        null,
        { nested: { deep: ["Too short.", "Too short."] } },
      ],
      server: { message: "Invalid value.", severity: "error" },
    },
  };

  it("counts leaf error strings under a path", () => {
    expect(countErrors(errors, "metadata.name")).toBe(1);
    expect(countErrors(errors, "metadata.list")).toBe(3);
    expect(countErrors(errors, "metadata")).toBe(5);
  });

  it("returns 0 for missing paths and empty structures", () => {
    expect(countErrors(errors, "metadata.absent")).toBe(0);
    expect(countErrors(errors, "nowhere.at.all")).toBe(0);
    expect(countErrors({}, "metadata")).toBe(0);
  });

  it("treats a {message, severity} object as one error", () => {
    expect(countErrors(errors, "metadata.server")).toBe(1);
    expect(hasError(errors, "metadata.server")).toBe(true);
    expect(hasError(errors, "metadata.absent")).toBe(false);
  });

  it("joins unique messages", () => {
    expect(errorMessages(errors, "metadata.list")).toEqual([
      "Not a valid identifier.",
      "Too short.",
    ]);
    expect(errorMessages(errors, "metadata.absent")).toEqual([]);
  });

  it("detects user data (0 and false count as data)", () => {
    expect(isEmptyValue(undefined)).toBe(true);
    expect(isEmptyValue("")).toBe(true);
    expect(isEmptyValue([])).toBe(true);
    expect(isEmptyValue({ a: "", b: [] })).toBe(true);
    expect(hasData(0)).toBe(true);
    expect(hasData(false)).toBe(true);
    expect(hasData({ a: "x" })).toBe(true);
    expect(hasData([{ id: null }])).toBe(false);
  });
});
