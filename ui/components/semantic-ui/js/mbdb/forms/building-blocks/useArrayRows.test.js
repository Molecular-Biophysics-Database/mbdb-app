import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
import { Formik, useFormikContext } from "formik";
import { useArrayRows } from "@js/mbdb/forms/building-blocks/useArrayRows";

// jsdom has no WebCrypto in insecure contexts; the app needs only
// https/localhost. Incrementing ids so client-only keys differ per call.
let mockN = 0;
jest.mock("@js/mbdb/forms/building-blocks/randomUUID", () => ({
  randomUUID: () => `uuid-${++mockN}`,
}));

const Probe = ({ path }) => {
  const { values } = useFormikContext();
  const value = path.split(".").reduce((o, p) => o?.[p], values);
  return <span data-testid="probe">{JSON.stringify(value ?? null)}</span>;
};
Probe.propTypes = { path: PropTypes.string.isRequired };

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

const mount = (ui, { initialValues = {} } = {}) => {
  container = document.createElement("div");
  document.body.appendChild(container);
  act(() => {
    ReactDOM.render(
      <Formik initialValues={initialValues} onSubmit={() => {}}>
        {ui}
      </Formik>,
      container
    );
  });
};

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
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
const probe = () =>
  JSON.parse(container.querySelector('[data-testid="probe"]').textContent);

describe("useArrayRows", () => {
  it("keys stay stable on remove-middle and last-remove clears the key", async () => {
    mount(
      <>
        <Rows fieldPath="list" />
        <Probe path="list" />
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
