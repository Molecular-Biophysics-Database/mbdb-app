import { describeOrganism } from "./describers";

describe("describeOrganism", () => {
  it("returns the rank the API puts on the item", () => {
    expect(describeOrganism({ props: { rank: "species" } })).toBe("species");
  });

  it("returns undefined without props or rank", () => {
    expect(describeOrganism({})).toBeUndefined();
    expect(describeOrganism({ props: {} })).toBeUndefined();
    expect(describeOrganism(undefined)).toBeUndefined();
  });
});
