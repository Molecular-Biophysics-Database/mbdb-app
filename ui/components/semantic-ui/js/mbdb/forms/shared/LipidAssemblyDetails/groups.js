// The group spec of the lipid assembly fields, for the entity's details view
// (step 4). One group; ComplexSubstanceOfChemicalOrigin puts it before
// COMPLEX_SUBSTANCE_COMMON_GROUPS, so the order is assembly fields, then the
// common block. `components` is an array of complex objects, so its entry
// carries the component mini-table columns and the items' details groups.
import { COMPONENT_ITEM_SPEC } from "@js/mbdb/forms/shared/Components/columns";

export const LIPID_ASSEMBLY_GROUPS = [
  {
    title: "Lipid assembly",
    fields: [
      "assembly_type",
      "number_of_mono_layers",
      "size",
      { field: "components", ...COMPONENT_ITEM_SPEC },
    ],
  },
];
