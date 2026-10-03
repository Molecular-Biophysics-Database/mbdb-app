import { toOption } from "./options";

describe("toOption", () => {
  it("expands a string to a {key,value,text} option", () => {
    expect(toOption("pdb")).toEqual({ key: "pdb", value: "pdb", text: "pdb" });
  });

  it("keeps an object's own key", () => {
    expect(toOption({ key: "k1", value: "a", text: "Alpha" })).toEqual({
      key: "k1",
      value: "a",
      text: "Alpha",
    });
  });

  it("fills in the key as String(value) when the object has none", () => {
    expect(toOption({ value: "a", text: "Alpha" })).toEqual({
      key: "a",
      value: "a",
      text: "Alpha",
    });
  });

  it("stringifies boolean values into the key (ButtonGroupField)", () => {
    expect(toOption({ value: true, text: "Yes" })).toEqual({
      key: "true",
      value: true,
      text: "Yes",
    });
    expect(toOption({ value: false, text: "No" })).toEqual({
      key: "false",
      value: false,
      text: "No",
    });
  });
});
