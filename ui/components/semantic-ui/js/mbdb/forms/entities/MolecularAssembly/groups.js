// The group spec of the Molecular assembly entity. The entity form and its
// DetailView both read it (guide §8). `components` is an array of complex
// objects, so its entry carries the component mini-table columns and the items'
// details groups (COMPONENT_ITEM_SPEC), so the read-only mini table inside the
// entity's details matches the components table. The other fields are plain
// names (no vocabulary reference). The titles are the model labels of the named
// fields (a DetailView group needs a string title).
import { COMPONENT_ITEM_SPEC } from "@js/mbdb/forms/shared/Components/columns";
import { MODIFICATION_ITEM_SPEC } from "@js/mbdb/forms/shared/Modifications";

export const MOLECULAR_ASSEMBLY_GROUPS = [
  { title: "Molecular weight", fields: ["molecular_weight"] },
  {
    title: "Components",
    fields: [{ field: "components", ...COMPONENT_ITEM_SPEC }],
  },
  { title: "External databases", fields: ["external_databases"] },
  {
    title: "Chemical modifications",
    fields: [{ field: "chemical_modifications", ...MODIFICATION_ITEM_SPEC }],
  },
  { title: "Quality controls", fields: ["quality_controls"] },
  { title: "Additional specifications", fields: ["additional_specifications"] },
];
