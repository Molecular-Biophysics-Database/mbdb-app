// Shared option normalization: callers may pass options as plain strings or
// as Semantic option objects. A string expands to the trivial {key,value,text}.
export const toOption = (o) =>
  typeof o === "string" ? { key: o, value: o, text: o } : o;
