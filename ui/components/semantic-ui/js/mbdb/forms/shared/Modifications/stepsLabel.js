// The expand toggle text of one modification row (design Modifications): the
// protocol step NAMES, joined — "PNGase F, Desalting" — so a reader sees what
// is inside without opening the row (lead, 2026-10-04; it used to be a count).
//
// A step with no name yet (a freshly added row is `{}` before typing) is
// skipped; when a protocol exists but no step has a name, the count is shown so
// the toggle is never empty. An empty/absent protocol reads "No protocol".
export const stepsLabel = (protocol) => {
  const steps = protocol ?? [];
  if (steps.length === 0) return "No protocol";
  const names = steps.map((step) => step?.name).filter(Boolean);
  if (names.length === 0)
    return steps.length === 1 ? "1 step" : `${steps.length} steps`;
  return names.join(", ");
};
