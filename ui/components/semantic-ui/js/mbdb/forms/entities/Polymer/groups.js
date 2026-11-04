// The group spec of the Polymer entity. The form and its DetailView both read
// it (guide §8), and shared/Components reuses it for a polymer component's
// details. `source_organism` / `expression_organism` are vocabulary
// references, so they declare their vocabulary for the details view.
//
// The titles mirror the same groupings the form shows: "Identification" and
// "Origin" are UI groupings with no model field (literal titles), the rest are
// the blocks' own model labels (kept literal here because a DetailView group
// needs a string title; same as STORAGE_GROUPS).
import { MODIFICATION_ITEM_SPEC } from "@js/mbdb/forms/shared/Modifications";

export const POLYMER_GROUPS = [
  {
    title: "Identification",
    fields: ["polymer_type", "expression_source_type", "variant"],
  },
  { title: "Sequence", fields: ["sequence"] },
  {
    title: "Origin",
    fields: [
      { field: "source_organism", vocabulary: "organisms" },
      { field: "expression_organism", vocabulary: "organisms" },
    ],
  },
  { title: "Molecular weight", fields: ["molecular_weight"] },
  { title: "External databases", fields: ["external_databases"] },
  { title: "Additional specifications", fields: ["additional_specifications"] },
  {
    title: "Modifications",
    // an array inside a nested object: its columns are declared through
    // `children`, so the mini table matches the edit table (design §2b rule 4)
    fields: [
      {
        field: "modifications",
        children: {
          biological_postprocessing: MODIFICATION_ITEM_SPEC,
          chemical: MODIFICATION_ITEM_SPEC,
        },
      },
    ],
  },
  { title: "Quality controls", fields: ["quality_controls"] },
];
