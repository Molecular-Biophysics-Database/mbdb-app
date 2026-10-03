import React from "react";
import PropTypes from "prop-types";
import { act, Simulate } from "react-dom/test-utils";
import { useArrayRows } from "@js/mbdb/forms/building-blocks/useArrayRows";
import {
  renderInForm,
  unmountForm,
  ValueProbe,
  readProbe,
} from "@js/mbdb/forms/building-blocks/testUtils";

// jsdom has no WebCrypto; client-only row keys (plan 3R X6).
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () =>
  jest
    .requireActual("@js/mbdb/forms/building-blocks/testUtils")
    .mockRandomUUID()
);

const Rows = ({ fieldPath }) => {
  const { items, keyFor, remove, push, replace } = useArrayRows(fieldPath);
  return (
    <>
      <ul>
        {items.map((item, i) => (
          <li key={keyFor(item, i)} data-key={keyFor(item, i)}>
            {item.name}
          </li>
        ))}
      </ul>
      <button
        type="button"
        data-testid="remove-mid"
        onClick={() => remove(1)}
      />
      <button
        type="button"
        data-testid="remove-last"
        onClick={() => remove(items.length - 1)}
      />
      <button
        type="button"
        data-testid="push"
        onClick={() => push({ name: "added" })}
      />
      <button
        type="button"
        data-testid="replace"
        onClick={() => replace(0, { name: "replaced" })}
      />
    </>
  );
};
Rows.propTypes = { fieldPath: PropTypes.string.isRequired };

let container;

const mount = (ui, opts = {}) => {
  container = renderInForm(ui, opts);
};

afterEach(() => {
  unmountForm(container);
  container = null;
});

const click = async (testId) => {
  await act(async () => {
    Simulate.click(container.querySelector(`[data-testid="${testId}"]`));
  });
};
const keys = () =>
  [...container.querySelectorAll("li")].map((l) => l.dataset.key);
const names = () =>
  [...container.querySelectorAll("li")].map((l) => l.textContent);
const probe = () => readProbe(container);

describe("useArrayRows", () => {
  it("keys stay stable on remove-middle and last-remove clears the key", async () => {
    mount(
      <>
        <Rows fieldPath="list" />
        <ValueProbe path="list" />
      </>,
      {
        initialValues: {
          list: [{ name: "A" }, { name: "B" }, { name: "C" }],
        },
      }
    );
    const before = keys();
    expect(before).toHaveLength(3);
    expect(new Set(before).size).toBe(3); // all distinct

    // remove the middle row: A and C keep their keys
    await click("remove-mid");
    expect(names()).toEqual(["A", "C"]);
    expect(keys()).toEqual([before[0], before[2]]);

    // remove the last remaining rows: the whole key list empties and the
    // Formik key is cleared (never [])
    await click("remove-last");
    await click("remove-last");
    expect(names()).toEqual([]);
    expect(probe()).toBeNull();
  });

  it("push mints a fresh key; replace keeps the slot's key", async () => {
    mount(<Rows fieldPath="list" />, {
      initialValues: { list: [{ name: "A" }] },
    });
    const [a] = keys();

    await click("push");
    expect(names()).toEqual(["A", "added"]);
    const afterPush = keys();
    expect(afterPush[0]).toBe(a); // original key untouched
    expect(afterPush[1]).not.toBe(a); // new key minted

    await click("replace");
    expect(names()).toEqual(["replaced", "added"]);
    expect(keys()[0]).toBe(a); // replace keeps the slot key
  });
});
