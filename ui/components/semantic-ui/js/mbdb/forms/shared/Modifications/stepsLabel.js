// The expand toggle text of one modification row (design Modifications).
export const stepsLabel = (protocol) => {
  const count = (protocol ?? []).length;
  if (count === 0) return "No protocol";
  return count === 1 ? "1 step" : `${count} steps`;
};
