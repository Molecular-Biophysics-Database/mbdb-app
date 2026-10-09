// Pure helpers for the ExternalDatabases block. No React; the table reads
// them only. References are stored as "prefix:id" strings; real data is mixed
// case ("Uniprot:P69905"), so known prefixes read case-insensitively, and
// reading must never rewrite the stored string until the user edits a cell.

export const KNOWN_DATABASES = {
  pdb: (id) => `https://www.rcsb.org/structure/${encodeURIComponent(id)}`,
  uniprot: (id) =>
    `https://www.uniprot.org/uniprotkb/${encodeURIComponent(id)}`,
};

// "Uniprot:P69905" -> { database: "uniprot", id: "P69905" }. The split is at
// the FIRST colon only ("pdb:1ABC:A" keeps "1ABC:A" as id). A known prefix is
// lower-cased here — the one normalizing write this block does, so an edited
// row stores "uniprot:…" even when it loaded as "Uniprot:…". An unknown prefix
// is kept as typed: the server is authoritative, and the row must display what
// fetched data actually contains instead of mangling it.
export const parseRef = (stored) => {
  if (stored === undefined || stored === null || stored === "")
    return { database: "", id: "" };
  const text = String(stored);
  const colon = text.indexOf(":");
  const rawPrefix = colon === -1 ? "" : text.slice(0, colon);
  const id = colon === -1 ? text : text.slice(colon + 1);
  const lowered = rawPrefix.toLowerCase();
  return {
    database: Object.hasOwn(KNOWN_DATABASES, lowered) ? lowered : rawPrefix,
    id,
  };
};

// { database: "pdb", id: "1GWD" } -> "pdb:1GWD". Both parts empty -> ""
// (the only empty value this block writes; the old UI wrote ":", which we
// must never produce). parseRef already lower-cased known prefixes on the way
// in, so this is a plain join.
export const formatRef = ({ database, id } = {}) => {
  const db = database ?? "";
  const value = id ?? "";
  if (!db && !value) return "";
  return `${db}:${value}`;
};

// The Open URL for a row: only for a known database AND a non-empty id.
export const refUrl = ({ database, id } = {}) =>
  (id && KNOWN_DATABASES[database]?.(id)) || null;
