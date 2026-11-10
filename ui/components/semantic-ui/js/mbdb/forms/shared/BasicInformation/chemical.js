import { hasData } from "@js/mbdb/forms/building-blocks/errors";
import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";

// Pure helpers of the chemical basic-information field.

// Manual entry is on: the backend keeps manual chemicals via the vocabulary's
// AutoCreateChemicalMixin (verified end-to-end 2026-10-02: `samples/chemical_lost.json`
// PUT → 201 → GET keeps `basic_information: { id: "manual:3600b56a-…" }`, and the pid
// tombstone problem is handled there too).
export const MANUAL_CHEMICALS_ENABLED = true;

// A manual chemical is told apart from a picked vocabulary term by having
// data but no id (the stored manual shape starts with { title: { en } }).
export const isManualChemical = (value) => hasData(value) && !value.id;

// The dropdown description for a chemicals option: formula and molecular
// weight, joined with " · ", skipping whatever is missing so no dangling
// separators appear. In a vocabulary item the facts live under
// custom_fields (in the stored record they are top-level keys instead).
export const describeChemical = (option) => {
  const custom = option?.custom_fields ?? {};
  const parts = [
    custom.chemical_formula,
    valueUnitText(custom.molecular_weight),
  ].filter((part) => part !== undefined && part !== "");
  return parts.length > 0 ? parts.join(" · ") : undefined;
};

// "Check your chemistry" links next to the label. Query goes in the URL
// hash: PubChem accepts a title or the id, ChEMBL only a title (a ChEMBL
// search for an InChIKey id finds nothing).
export const chemicalLinks = (value) => {
  const title = value?.title?.en ?? value?.title ?? undefined;
  const pubchemQuery = title ?? value?.id;
  if (!pubchemQuery) return [];
  const links = [
    {
      label: "PubChem ↗",
      href: `https://pubchem.ncbi.nlm.nih.gov/#query=${encodeURIComponent(
        pubchemQuery
      )}`,
    },
  ];
  if (title) {
    links.push({
      label: "ChEMBL ↗",
      href: `https://www.ebi.ac.uk/chembl/g/#search_results/all/query=${encodeURIComponent(
        title
      )}`,
    });
  }
  return links;
};
