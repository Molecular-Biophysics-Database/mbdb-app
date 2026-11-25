import React from "react";
import { act, Simulate } from "react-dom/test-utils";
import {
  ValueProbe,
  pickDropdown,
  readProbe,
  renderInForm,
  unmountForm,
} from "@js/mbdb/forms/building-blocks/testUtils";
import { ReferenceField, referenceOptions } from "./ReferenceField";
import { ReferenceNames } from "./ReferenceNames";

// eslint-disable-next-line no-restricted-syntax -- canonical shared fake (§8)
jest.mock(
  "@js/oarepo_ui/forms",
  () =>
    jest.requireActual("@js/mbdb/forms/building-blocks/testUtils").oarepoFake
);

const TARGETS = [
  { id: "a", name: "Alpha" },
  { id: "b", name: "Beta" },
];
let container;
afterEach(() => unmountForm(container));

const render = (value, props) => {
  container = renderInForm(
    <>
      <ReferenceField fieldPath="ref" targetPath="targets" {...props} />
      <ValueProbe path="ref" />
    </>,
    { initialValues: { targets: TARGETS, ref: value } }
  );
};

describe("ReferenceField", () => {
  it("writes { id, name } of the picked item", async () => {
    render(undefined);
    await pickDropdown("ref", "Beta");
    expect(readProbe(container)).toEqual({ id: "b", name: "Beta" });
  });

  it("multiple appends to the stored references", async () => {
    render([{ id: "a", name: "Alpha" }], { multiple: true });
    // Semantic's multiple dropdown calls this on the native event
    const item = [...container.querySelectorAll(".menu .item")].find(
      (el) => el.textContent.trim() === "Beta"
    );
    await act(async () => {
      Simulate.click(item, { nativeEvent: { stopImmediatePropagation() {} } });
      await new Promise((r) => setTimeout(r, 0));
    });
    expect(readProbe(container)).toEqual(TARGETS);
  });

  it("shows names by id, the form's name before the stored one", () => {
    container = renderInForm(
      <ReferenceNames
        value={[{ id: "a" }, { id: "b", name: "Old" }, { id: "x", name: "Gone" }]}
        targetPath="targets"
      />,
      { initialValues: { targets: TARGETS } }
    );
    expect(container.textContent).toBe("Alpha, Beta, Gone");
  });

  it("keeps a reference to a removed item visible", () => {
    expect(
      referenceOptions(TARGETS, [{ id: "x", name: "Gone" }], (t) => t.name).map(
        (o) => o.text
      )
    ).toEqual(["Alpha", "Beta", "Gone (no longer exists)"]);
  });
});
