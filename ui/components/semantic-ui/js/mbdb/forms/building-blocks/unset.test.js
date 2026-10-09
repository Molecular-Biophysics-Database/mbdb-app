import { unsetFieldValue } from "./unset";

describe("unsetFieldValue", () => {
  let calls;
  const setFieldValue = (path, value) => calls.push([path, value]);

  beforeEach(() => {
    calls = [];
  });

  it("keeps a parent chain that still holds data above an emptied object", () => {
    const values = { a: { keep: "x", location: { altitude: 250 } } };
    unsetFieldValue(values, setFieldValue, "a.location.altitude");
    // `location` emptied and is pruned, `a` still holds `keep`
    expect(calls).toEqual([
      ["a.location.altitude", undefined],
      ["a.location", undefined],
    ]);
  });

  it("only clears the leaf when siblings hold data", () => {
    const values = { a: { location: { altitude: 250, area: "lab" } } };
    unsetFieldValue(values, setFieldValue, "a.location.altitude");
    expect(calls).toEqual([["a.location.altitude", undefined]]);
  });

  it("drops every plain-object parent that becomes empty (C15)", () => {
    const values = { a: { location: { altitude: 250 } } };
    unsetFieldValue(values, setFieldValue, "a.location.altitude");
    expect(calls).toEqual([
      ["a.location.altitude", undefined],
      ["a.location", undefined],
      ["a", undefined],
    ]);
  });

  it("walks up several empty plain-object levels", () => {
    const values = { a: { b: { c: { v: 1 } } } };
    unsetFieldValue(values, setFieldValue, "a.b.c.v");
    expect(calls).toEqual([
      ["a.b.c.v", undefined],
      ["a.b.c", undefined],
      ["a.b", undefined],
      ["a", undefined],
    ]);
  });

  it("stops at the form root object", () => {
    const values = { only: { x: 1 } };
    unsetFieldValue(values, setFieldValue, "only.x");
    // `only` becomes {}, gets pruned, but formik's root (no parent path) is left alone
    expect(calls).toEqual([
      ["only.x", undefined],
      ["only", undefined],
    ]);
  });

  it("never drops an item of an array (objects inside arrays are kept)", () => {
    const values = {
      entities: [{ location: { altitude: 250 } }, { name: "other" }],
    };
    unsetFieldValue(values, setFieldValue, "entities.0.location.altitude");
    expect(calls).toEqual([
      ["entities.0.location.altitude", undefined],
      ["entities.0.location", undefined],
      // entities.0 must NOT be pruned even if it happens to be empty
    ]);
    expect(calls.find(([p]) => p === "entities.0")).toBeUndefined();
  });

  it("stops at array-valued parents", () => {
    const values = { list: [{ v: 1 }] };
    unsetFieldValue(values, setFieldValue, "list.0.v");
    expect(calls).toEqual([["list.0.v", undefined]]);
  });

  it("does not treat 0 or false as empty when deciding to prune", () => {
    const values = { a: { location: { altitude: 250, floor: 0 } } };
    unsetFieldValue(values, setFieldValue, "a.location.altitude");
    // only the leaf is removed; the parent still holds 0, which is data
    expect(calls).toEqual([["a.location.altitude", undefined]]);
  });
});
