// Dropdown option descriptions: the short fact shown on the right of each
// option that tells similar terms apart. The API serializes option fields
// onto the serialized suggestion (processVocabularyItems spreads the item),
// so props/custom_fields of the vocabulary item are readable here. Missing
// data means no description, not a placeholder.

// e.g. "species" — the API returns the rank in lower case.
export const describeOrganism = (option) => option?.props?.rank ?? undefined;

// e.g. "Brno, Czechia" — the city (and state) and country of a ROR
// organization, from the /api/ror/affiliations suggest endpoint.
export const describeAffiliation = (option) =>
  [
    [option?.props?.city, option?.props?.state].filter(Boolean).join(", "),
    option?.props?.country,
  ]
    .filter(Boolean)
    .join(" · ") || undefined;
