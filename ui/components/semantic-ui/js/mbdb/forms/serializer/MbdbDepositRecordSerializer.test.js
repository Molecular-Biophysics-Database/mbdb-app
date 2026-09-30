import { MbdbDepositRecordSerializer } from "./MbdbDepositRecordSerializer";

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
});
