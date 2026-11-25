import React from "react";
import ReactDOM from "react-dom";
import { act } from "react-dom/test-utils";
import { ExternalLink } from "./ExternalLink";

let container;

beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  ReactDOM.unmountComponentAtNode(container);
  container.remove();
});

const render = (ui) => {
  act(() => {
    ReactDOM.render(ui, container);
  });
};

describe("ExternalLink", () => {
  it("renders an anchor with target/rel and no type attribute", () => {
    render(<ExternalLink href="https://www.uniprot.org">UniProt</ExternalLink>);
    const a = container.querySelector("a");
    expect(a).not.toBeNull();
    expect(a.getAttribute("href")).toBe("https://www.uniprot.org");
    expect(a.getAttribute("target")).toBe("_blank");
    expect(a.getAttribute("rel")).toBe("noreferrer");
    // an anchor has no type="button"; Button must not leak the button type
    expect(a.getAttribute("type")).toBeNull();
    expect(a.textContent).toContain("UniProt");
    expect(a.querySelector("i.icon.external")).not.toBeNull();
  });

  it("renders nothing without an href", () => {
    render(<ExternalLink>Open</ExternalLink>);
    expect(container.innerHTML).toBe("");
    render(<ExternalLink href="">Open</ExternalLink>);
    expect(container.innerHTML).toBe("");
  });
});
