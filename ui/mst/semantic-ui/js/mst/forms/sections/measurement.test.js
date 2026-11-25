import { describeMeasurement, nextMeasurement } from "./measurement";

describe("nextMeasurement", () => {
  it("copies the last measurement without id and position", () => {
    expect(
      nextMeasurement([
        { id: "1", name: "a", position: "1" },
        { id: "2", name: "b", position: "2", sample: { ligands: [] } },
      ])
    ).toEqual({ name: "b", sample: { ligands: [] } });
    expect(nextMeasurement(undefined)).toEqual({});
    expect(nextMeasurement([])).toEqual({});
  });
});

describe("describeMeasurement", () => {
  it("tells replicates with the same name apart", () => {
    expect(describeMeasurement({ name: "a", position: "3" })).toBe(
      "a (position 3)"
    );
    expect(describeMeasurement({ name: "a" })).toBe("a");
  });
});
