// Text from a number input → number, or undefined for "", whitespace or
// unparseable text. Infinity is not finite and becomes undefined too, so a
// stored value is always a real number or absent — never NaN.
export const parseNumberInput = (raw) => {
  if (raw === null || raw === undefined) return undefined;
  const text = String(raw).trim();
  if (text === "") return undefined;
  const n = Number(text);
  return Number.isFinite(n) ? n : undefined;
};
