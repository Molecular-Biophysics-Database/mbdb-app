// Jest only discovers tests under the webpack entry dirs (js/mbdb/forms), so
// this test for mbdb-semantic-ui-react code lives here in building-blocks.
import React from "react";
import ReactDOM from "react-dom";
import { act, Simulate } from "react-dom/test-utils";
// Deep imports: the sources live in mbdb-semantic-ui-react.
import {
  HelpModeProvider,
  useHelpMode,
  HelpLabel,
  HelpIcon,
} from "mbdb-semantic-ui-react/HelpMode";
import { FieldHelp } from "mbdb-semantic-ui-react/FieldHelp";

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

const ModeProbe = () => <span data-testid="mode">{useHelpMode()}</span>;

const mode = () => container.querySelector('[data-testid="mode"]').textContent;
const helptexts = () => [...container.querySelectorAll("label.helptext")];
const helpIcons = () => [...container.querySelectorAll('[aria-label^="Help"]')];

describe("help mode context", () => {
  it("useHelpMode returns invenio without a provider", () => {
    render(<ModeProbe />);
    expect(mode()).toBe("invenio");
  });

  it("an unknown provider mode falls back to invenio", () => {
    render(
      <HelpModeProvider mode="bogus">
        <ModeProbe />
      </HelpModeProvider>
    );
    expect(mode()).toBe("invenio");
  });
});

describe("FieldHelp", () => {
  it("renders label.helptext.mbdb-field-help in invenio mode", () => {
    render(<FieldHelp help="Some help" />);
    expect(helptexts().length).toBe(1);
    expect(helptexts()[0].classList.contains("mbdb-field-help")).toBe(true);
    expect(helptexts()[0].textContent).toBe("Some help");
  });

  it("renders nothing in popup mode", () => {
    render(
      <HelpModeProvider mode="popup">
        <FieldHelp help="Some help" />
      </HelpModeProvider>
    );
    expect(container.innerHTML).toBe("");
  });

  it("renders nothing for empty help in invenio mode", () => {
    render(<FieldHelp help={null} />);
    expect(container.innerHTML).toBe("");
  });
});

describe("HelpLabel", () => {
  it("renders no icon in invenio mode", () => {
    render(<HelpLabel label="Name" help="Some help" />);
    expect(container.textContent).toBe("Name");
    expect(helpIcons().length).toBe(0);
  });

  it('renders an icon with aria-label="Help: Name" in popup mode', () => {
    render(
      <HelpModeProvider mode="popup">
        <HelpLabel label="Name" help="Some help" />
      </HelpModeProvider>
    );
    const icons = helpIcons();
    expect(icons.length).toBe(1);
    expect(icons[0].getAttribute("aria-label")).toBe("Help: Name");
    expect(container.textContent).toContain("Name");
  });

  it("renders no icon in popup mode when help is empty", () => {
    render(
      <HelpModeProvider mode="popup">
        <HelpLabel label="Name" help={null} />
      </HelpModeProvider>
    );
    expect(container.textContent).toBe("Name");
    expect(helpIcons().length).toBe(0);
  });

  it("the icon has tabIndex 0", () => {
    render(
      <HelpModeProvider mode="popup">
        <HelpLabel label="Name" help="Some help" />
      </HelpModeProvider>
    );
    expect(helpIcons()[0].getAttribute("tabindex")).toBe("0");
  });
});

describe("HelpIcon", () => {
  it("renders nothing when help is empty", () => {
    render(<HelpIcon help={null} label="Name" />);
    expect(container.innerHTML).toBe("");
  });

  it("opens its popup on keyboard focus", () => {
    render(
      <HelpModeProvider mode="popup">
        <HelpIcon help="Focus help content" label="Name" />
      </HelpModeProvider>
    );
    const icon = container.querySelector('[aria-label^="Help"]');
    expect(icon).not.toBeNull();
    act(() => {
      Simulate.focus(icon);
    });
    expect(document.querySelector(".ui.popup")).not.toBeNull();
    expect(document.body.textContent).toContain("Focus help content");
  });
});
