import { getIn } from "formik";
import { entityErrors, entityPath, entityValues } from "./fixtures";

describe("fixtures", () => {
  it("entityErrors resolves dotted and indexed fields", () => {
    expect(
      getIn(
        entityErrors("storage.temperature", "m"),
        entityPath("storage.temperature")
      )
    ).toBe("m");
    expect(
      getIn(
        entityErrors("components.2.name", "m"),
        entityPath("components.2.name")
      )
    ).toBe("m");
  });

  it("entityErrors keeps the old shape for a flat field", () => {
    expect(entityErrors("name", "m")).toEqual({
      metadata: {
        general_parameters: { entities_of_interest: [{ name: "m" }] },
      },
    });
  });

  it("entityValues still builds one typed entity", () => {
    expect(entityValues("Chemical", { name: "Water" })).toEqual({
      metadata: {
        general_parameters: {
          entities_of_interest: [{ type: "Chemical", name: "Water" }],
        },
      },
    });
  });
});
