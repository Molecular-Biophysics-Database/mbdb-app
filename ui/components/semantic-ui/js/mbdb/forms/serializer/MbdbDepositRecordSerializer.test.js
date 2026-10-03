import { MbdbDepositRecordSerializer } from "./MbdbDepositRecordSerializer";

// jsdom has no WebCrypto; the load-time id pass would otherwise throw.
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => "uuid-test",
}));

describe("MbdbDepositRecordSerializer", () => {
  const serializer = new MbdbDepositRecordSerializer();

  it("drops empty values and internal keys from metadata", () => {
    const record = {
      id: "abc",
      ui: { ignored: true },
      metadata: {
        general_parameters: {
          entities_of_interest: [
            {
              __key: 1,
              id: "e1",
              type: "Polymer",
              name: "Lysozyme",
              variant: "",
              additional_specifications: [],
              external_databases: ["", "pdb:1GWD"],
              modifications: { chemical: [] },
              molecular_weight: { value: 0, unit: "kDa" },
            },
          ],
        },
      },
    };

    expect(serializer.serialize(record)).toEqual({
      id: "abc",
      metadata: {
        general_parameters: {
          entities_of_interest: [
            {
              id: "e1",
              type: "Polymer",
              name: "Lysozyme",
              external_databases: ["pdb:1GWD"],
              molecular_weight: { value: 0, unit: "kDa" },
            },
          ],
        },
      },
    });
  });

  it("keeps false booleans in objects", () => {
    const record = { metadata: { homogenized: false } };
    expect(serializer.serialize(record).metadata).toEqual({
      homogenized: false,
    });
  });

  it("does not mutate the input record", () => {
    const record = { metadata: { a: "", b: [{ __key: 1, c: "x" }] } };
    const copy = JSON.parse(JSON.stringify(record));
    serializer.serialize(record);
    expect(record).toEqual(copy);
  });

  it("deserialize assigns an id to entities without one and keeps existing ids", () => {
    const record = {
      metadata: {
        general_parameters: {
          entities_of_interest: [
            { id: "e1", type: "Polymer", name: "A" },
            { type: "Chemical", name: "B" },
          ],
        },
      },
    };
    const out = serializer.deserialize(record);
    const entities = out.metadata.general_parameters.entities_of_interest;
    expect(entities[0].id).toBe("e1");
    expect(entities[1].id).toBe("uuid-test");
    // the input record is not mutated
    expect(
      record.metadata.general_parameters.entities_of_interest[1].id
    ).toBeUndefined();
  });

  it("deserialize leaves the entities unchanged when every one has an id", () => {
    const record = {
      metadata: {
        general_parameters: { entities_of_interest: [{ id: "e1" }] },
      },
    };
    expect(
      serializer.deserialize(record).metadata.general_parameters
        .entities_of_interest
    ).toEqual([{ id: "e1" }]);
  });

  it("deserialize leaves an absent entities list untouched", () => {
    expect(
      serializer.deserialize({ metadata: { general_parameters: {} } }).metadata
        .general_parameters.entities_of_interest
    ).toBeUndefined();
    expect(serializer.deserialize({}).metadata).toBeUndefined();
  });
});
