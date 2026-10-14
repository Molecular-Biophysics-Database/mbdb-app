// Pure helpers for the Sequence block. No React; the component reads them only.

// normalizeSequence: stored sequences hold no FASTA header and no whitespace.
// Normalization happens on blur only (the component), never on every keystroke,
// so the cursor does not jump while the user is typing a multi-line paste.
// An empty result becomes undefined (guide §7: empty means key absent).
export const normalizeSequence = (text) => {
  const normalized = String(text ?? "")
    .replace(/^>[^\n]*(\n|$)/, "") // drop a leading FASTA header line, keep the rest
    .replace(/\s+/g, "");
  return normalized === "" ? undefined : normalized;
};

// countResidues: a residue is a letter outside a `<…>` non-canonical group,
// plus one per group ("AC<Hyp>G" = 4). Case is irrelevant to the count;
// undefined renders as 0, so callers never need a null guard.
export const countResidues = (text) =>
  (String(text ?? "").match(/[A-Za-z]|<[^>]*>/g) ?? []).length;

// BLAST only: there is no UniProt URL that takes a sequence (design decision).
export const blastUrl = (sequence) =>
  `https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins&PROGRAM=blastp&QUERY=${encodeURIComponent(
    sequence ?? ""
  )}`;
