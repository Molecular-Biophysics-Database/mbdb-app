import { ensureEntityIds, newEntitySeed } from "./DefaultsAndIds";

// jsdom has no WebCrypto in insecure contexts; the app needs only https/localhost.
jest.mock("./randomUUID", () => ({
  randomUUID: () => "12345678-1234-1234-1234-123456789012",
}));

const UUID_RE =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/;

describe("DefaultsAndIds", () => {
  it("seeds a new entity with a uuid and the given type", () => {
    const seed = newEntitySeed("Polymer");
    expect(seed.type).toBe("Polymer");
    expect(seed.id).toMatch(UUID_RE);
  });

  it("seeds id-only when no type is given", () => {
    expect(Object.keys(newEntitySeed())).toEqual(["id"]);
  });

  it("assigns ids only to entities that have none", () => {
    const withId = { id: "keep-me", name: "A" };
    const [a, b, c] = ensureEntityIds([withId, { name: "B" }, undefined]);
    expect(a).toBe(withId);
    expect(b.id).toMatch(UUID_RE);
    expect(b.name).toBe("B");
    expect(c).toBe(undefined);
  });

  it("returns an empty array for missing lists", () => {
    expect(ensureEntityIds(undefined)).toEqual([]);
  });
});
