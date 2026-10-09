import React from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { useEditSession } from "./useEditSession";

// The hook's return, captured per render into these locals for assertions.
let api;
const HookProbe = ({ ops }) => {
  api = useEditSession(ops);
  return null;
};
HookProbe.propTypes = {
  ops: PropTypes.object.isRequired,
};

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const render = (ops) => {
  act(() => {
    ReactDOM.render(<HookProbe ops={ops} />, container);
  });
};

const ops = () => ({
  read: jest.fn(),
  restore: jest.fn(),
  remove: jest.fn(),
});

describe("useEditSession", () => {
  it("Cancel of a new session removes the key", () => {
    const o = ops();
    render(o);
    expect(api.session).toBeNull();

    act(() => api.openNew(3));
    expect(api.session).toMatchObject({ key: 3, isNew: true, snapshot: null });

    act(() => api.cancel());
    expect(o.remove).toHaveBeenCalledWith(3);
    expect(o.restore).not.toHaveBeenCalled();
    expect(api.session).toBeNull();
  });

  it("Cancel of an existing session restores the snapshot taken at open", () => {
    // mutating the live value after open must not change what Cancel restores
    const live = { nested: { name: "before" } };
    const o = { ...ops(), read: jest.fn(() => live) };
    render(o);

    act(() => api.openExisting("k"));
    live.nested.name = "after";
    const restored = o.restore.mock.calls.length;
    expect(restored).toBe(0);
    expect(api.session.snapshot).toEqual({ nested: { name: "before" } });

    act(() => api.cancel());
    expect(o.restore).toHaveBeenCalledWith("k", {
      nested: { name: "before" },
    });
    expect(o.remove).not.toHaveBeenCalled();
    expect(api.session).toBeNull();
  });

  it("openExisting carries extra state through (scrollToError)", () => {
    const o = ops();
    render(o);
    act(() => api.openExisting(0, { scrollToError: true }));
    expect(api.session).toMatchObject({
      key: 0,
      isNew: false,
      scrollToError: true,
    });
  });

  it("Done closes without calling remove or restore", () => {
    const o = ops();
    render(o);
    act(() => api.openNew(0));
    act(() => api.done());
    expect(o.remove).not.toHaveBeenCalled();
    expect(o.restore).not.toHaveBeenCalled();
    expect(api.session).toBeNull();
  });
});
