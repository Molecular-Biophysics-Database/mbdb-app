// Arrow-key roving focus for a group of buttons: ArrowRight/ArrowLeft moves
// focus to the next/previous button inside the event's currentTarget,
// wrapping at the ends. Other keys, and arrows while focus is outside the
// group's buttons, do nothing. Shared by ButtonGroupField and
// DiscriminatorField.
export const onRovingKeyDown = (e) => {
  if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
  const buttons = [...e.currentTarget.querySelectorAll("button")];
  const index = buttons.indexOf(document.activeElement);
  if (index === -1) return;
  e.preventDefault();
  const next =
    e.key === "ArrowRight"
      ? (index + 1) % buttons.length
      : (index - 1 + buttons.length) % buttons.length;
  buttons[next].focus();
};
