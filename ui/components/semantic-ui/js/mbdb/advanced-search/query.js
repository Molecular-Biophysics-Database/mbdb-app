const quote = (value) => `"${value.replace(/[\\"]/g, "\\$&")}"`;

const phrase = (path, value) => `${path}:${quote(value)}`;

// always a range: ">=" fails on negative numbers
const range = (path, from, to) => `${path}:[${from || "*"} TO ${to || "*"}]`;

const RANGE_OPERATORS = {
  is: { text: "is", clause: (path, value) => range(path, value, value) },
  from: { text: "at least", clause: (path, value) => range(path, value) },
  to: { text: "at most", clause: (path, value) => range(path, "", value) },
  between: {
    text: "between",
    clause: (path, value, value2) => range(path, value, value2),
  },
};
const IS = { text: "is", clause: phrase };
const CONTAINS = { text: "contains", clause: phrase };

export const OPERATORS = {
  words: {
    contains: {
      text: "contains",
      clause: (path, value) => phrase(`${path}.words`, value),
    },
    is: IS,
  },
  text: { contains: CONTAINS },
  keyword: { is: IS },
  enum: { is: IS },
  number: RANGE_OPERATORS,
  date: RANGE_OPERATORS,
};

export const defaultOperator = (kind) => Object.keys(OPERATORS[kind])[0];

/**
 * Lucene query for the rows, or an Error naming what is wrong with them.
 * Rows combine left to right unless bracketed; the parentheses are always
 * written out, because query strings have no AND/OR precedence.
 */
export const buildQuery = (rows, fields) => {
  const stack = [];
  let current = "";

  const combine = (left, join, right) => {
    if (!left) return join === "AND NOT" ? `(NOT ${right})` : right;
    return `(${left} ${join} ${right})`;
  };

  rows.forEach((row, index) => {
    const field = fields.find(({ path }) => path === row.path);
    const value = row.value.trim();
    const value2 = row.value2.trim();
    if (!field || !value || (row.operator === "between" && !value2)) {
      throw new Error(`Condition ${index + 1} is not filled in.`);
    }
    let { join } = row;
    if (row.open) {
      stack.push({ left: current, join });
      current = "";
      join = "AND";
    }
    const clause = OPERATORS[field.kind][row.operator].clause(field.path, value, value2);
    current = combine(current, join, clause);
    if (row.close) {
      if (!stack.length) {
        throw new Error(`Condition ${index + 1} closes a bracket that is not open.`);
      }
      const { left, join: outerJoin } = stack.pop();
      current = combine(left, outerJoin, current);
    }
  });
  if (stack.length) throw new Error("A bracket is not closed.");
  return current;
};
