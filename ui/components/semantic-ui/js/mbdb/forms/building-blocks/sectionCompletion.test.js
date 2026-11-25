import { requiredCompletion } from "./sectionCompletion";

jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

const person = {
  children: { given_name: { required: true }, note: {} },
};
const ui_model = {
  children: {
    title: { required: true },
    depositor: { ...person, required: true },
    publication: { children: { pid: { required: true } } },
    people: { child: person },
  },
};
const completion = (formikValues, includesPaths) =>
  requiredCompletion({
    formikValues,
    reduxState: { deposit: { config: { ui_model } } },
    includesPaths,
  });

describe("requiredCompletion", () => {
  const paths = ["title", "depositor", "publication", "people"];

  it("is complete without the optional fields", () => {
    expect(
      completion({ title: "t", depositor: { given_name: "A" } }, paths)
    ).toBe(1);
  });

  it("is not complete when a required field or its child is missing", () => {
    expect(completion({ title: "t" }, paths)).toBe(0.5);
    expect(
      completion({ title: "t", depositor: { note: "n" } }, paths)
    ).toBeLessThan(1);
  });

  it("counts required fields inside a filled optional object or list", () => {
    const values = { title: "t", depositor: { given_name: "A" } };
    expect(
      completion({ ...values, publication: { x: 1 } }, paths)
    ).toBeLessThan(1);
    expect(
      completion({ ...values, people: [{ note: "n" }] }, paths)
    ).toBeLessThan(1);
  });

  it("looks into entities, which have an id, but not into vocabularies", () => {
    const people = [{ id: "1", note: "n" }];
    expect(completion({ people }, ["people"])).toBe(0);
    const vocabulary = {
      children: {
        v: { input: "vocabulary", required: true, children: person.children },
      },
    };
    expect(
      requiredCompletion({
        formikValues: { v: { id: "1" } },
        reduxState: { deposit: { config: { ui_model: vocabulary } } },
        includesPaths: ["v"],
      })
    ).toBe(1);
  });

  it("skips fields of other variants of a polymorphic node", () => {
    const poly = {
      children: {
        e: {
          input: "polymorphic",
          children: {
            type: { required: true },
            a: { required: true },
            b: { required: true },
          },
        },
      },
    };
    const run = (belongs) =>
      requiredCompletion({
        formikValues: { e: { type: "A" } },
        reduxState: { deposit: { config: { ui_model: poly } } },
        includesPaths: ["e"],
        belongs,
      });
    expect(run()).toBe(1);
    expect(run((value, name) => name === "a")).toBe(0.5);
  });

  it("is complete when nothing is required", () => {
    expect(completion({}, ["publication", "people"])).toBe(1);
  });
});
