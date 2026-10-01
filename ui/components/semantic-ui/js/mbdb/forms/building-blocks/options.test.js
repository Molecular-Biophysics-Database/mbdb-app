import { toOption } from "./options";

describe("toOption", () => {
  it("expands a string to a {key,value,text} option", () => {
    expect(toOption("pdb")).toEqual({ key: "pdb", value: "pdb", text: "pdb" });
  });

  it("passes an option object through unchanged", () => {
    const opt = { key: "a", value: "a", text: "Alpha" };
    expect(toOption(opt)).toBe(opt);
  });
});
