import { onRovingKeyDown } from "./rovingFocus";

const makeGroup = () => {
  const group = document.createElement("div");
  ["a", "b", "c"].forEach((name) => {
    const button = document.createElement("button");
    button.textContent = name;
    group.appendChild(button);
  });
  document.body.appendChild(group);
  return group;
};

describe("onRovingKeyDown", () => {
  let group;
  let buttons;

  beforeEach(() => {
    group = makeGroup();
    buttons = [...group.querySelectorAll("button")];
  });

  afterEach(() => {
    group.remove();
  });

  const key = (keyName) =>
    onRovingKeyDown({
      key: keyName,
      currentTarget: group,
      preventDefault: () => {},
    });

  it("wraps from the last button to the first on ArrowRight", () => {
    buttons[2].focus();
    key("ArrowRight");
    expect(document.activeElement).toBe(buttons[0]);
    buttons[1].focus();
    key("ArrowRight");
    expect(document.activeElement).toBe(buttons[2]);
  });

  it("wraps from the first button to the last on ArrowLeft", () => {
    buttons[0].focus();
    key("ArrowLeft");
    expect(document.activeElement).toBe(buttons[2]);
  });

  it("does nothing for other keys", () => {
    buttons[1].focus();
    key("ArrowDown");
    expect(document.activeElement).toBe(buttons[1]);
  });
});
