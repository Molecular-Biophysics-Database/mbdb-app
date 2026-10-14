import {
  applyEntityId,
  ensureEntityIds,
  newEntitySeed,
} from "./DefaultsAndIds";

// jsdom has no WebCrypto in insecure contexts; the app needs only https/localhost.
// Fixed stub: assertions compare the exact mock value (the real format is
// covered by randomUUID.test.js).
jest.mock("./randomUUID", () => ({
  randomUUID: () => "uuid-from-mock",
}));

describe("DefaultsAndIds", () => {
  it("applyEntityId adds a fresh id and keeps the rest", () => {
    const item = { name: "A" };
    const withId = applyEntityId(item);
    expect(withId).toEqual({ name: "A", id: "uuid-from-mock" });
    // no mutation of the input
    expect(item).toEqual({ name: "A" });
  });

  it("seeds a new entity with a uuid and the given type", () => {
    expect(newEntitySeed("Polymer")).toEqual({
      type: "Polymer",
      id: "uuid-from-mock",
    });
  });

  it("seeds id-only when no type is given", () => {
    expect(newEntitySeed()).toEqual({ id: "uuid-from-mock" });
  });

  it("assigns ids only to entities that have none", () => {
    const withId = { id: "keep-me", name: "A" };
    const [a, b, c] = ensureEntityIds([withId, { name: "B" }, undefined]);
    expect(a).toBe(withId);
    expect(b).toEqual({ name: "B", id: "uuid-from-mock" });
    expect(c).toBe(undefined);
  });

  it("returns non-arrays unchanged (undefined stays undefined, never [])", () => {
    expect(ensureEntityIds(undefined)).toBeUndefined();
    expect(ensureEntityIds(null)).toBeNull();
  });

  it("returns the same reference when nothing changed", () => {
    const done = [{ id: "e1", name: "A" }];
    expect(ensureEntityIds(done)).toBe(done);
  });
});
