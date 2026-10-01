import { hasData } from "@js/mbdb/forms/building-blocks/errors";

// Pure helpers of the chemical basic-information field.

// A manual chemical is told apart from a picked vocabulary term by having
// data but no id (the stored manual shape starts with { title: { en } }).
export const isManualChemical = (value) => hasData(value) && !value.id;

// "760.1 g/mol", or the part of it that exists. Used by the dropdown
// options (custom_fields.molecular_weight) and the picker's meta line
// (stored basic_information.molecular_weight).
export const molecularWeightText = (mw) =>
  mw?.value !== undefined
    ? [mw.value, mw.unit].filter(Boolean).join(" ")
    : undefined;

// The dropdown description for a chemicals option: formula and molecular
// weight, joined with " · ", skipping whatever is missing so no dangling
// separators appear. In a vocabulary item the facts live under
// custom_fields (in the stored record they are top-level keys instead).
export const describeChemical = (option) => {
  const custom = option?.custom_fields ?? {};
  const parts = [
    custom.chemical_formula,
    molecularWeightText(custom.molecular_weight),
  ].filter((part) => part !== undefined && part !== "");
  return parts.length > 0 ? parts.join(" · ") : undefined;
};

// "Check your chemistry" links next to the label. Query goes in the URL
// hash: PubChem accepts a title or the id, ChEMBL only a title.
export const chemicalLinks = (value) => {
  const title = value?.title?.en ?? value?.title ?? value?.id;
  if (!title) return [];
  const query = encodeURIComponent(title);
  return [
    {
      label: "PubChem ↗",
      href: `https://pubchem.ncbi.nlm.nih.gov/#query=${query}`,
    },
    {
      label: "ChEMBL ↗",
      href: `https://www.ebi.ac.uk/chembl/g/#search_results/all/query=${query}`,
    },
  ];
};
