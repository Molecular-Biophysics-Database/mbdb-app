// Shared option normalization: callers may pass options as plain strings or
// as Semantic option objects. A string expands to the trivial {key,value,text};
// an object passes its fields through and only fills in the React `key`
// (String of the value, so booleans work) when it does not carry one.
export const toOption = (o) =>
  typeof o === "string"
    ? { key: o, value: o, text: o }
    : { key: String(o.value), ...o };
