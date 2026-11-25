import {
  POLYMER_GROUPS,
  summaryPolymer,
} from "@js/mbdb/forms/entities/Polymer";
import {
  CHEMICAL_GROUPS,
  summaryChemical,
} from "@js/mbdb/forms/entities/Chemical";

// -1 is "unknown" in a table only; the modal input keeps -1.
export const copyNumberText = (n) => (n === -1 ? "unknown" : n ?? "");

// A component's variant is the entity field set, so the entity's summary
// describes the row too: the Details column shows what the component is
// (polymer type / weight / organism, or the chemical title / formula), not just
// its type (design Components, "the collapsed row").
export const COMPONENT_DETAIL_SUMMARY = {
  Polymer: summaryPolymer,
  Chemical: summaryChemical,
};

// The component table's columns, used by the entity modal's component table AND
// by the read-only mini table that shows the same components inside the
// entity's details (design DetailView §3/§4: a mini table has the same columns
// as its edit table). `field` names the model field behind a column so the mini
// table's own ▸ can skip the columns it already shows; the Details column has
// no single model field and omits it.
export const COMPONENT_COLUMNS = [
  { field: "name", label: "Name", value: (v) => v.name },
  { field: "type", label: "Type", value: (v) => v.type },
  {
    field: "copy_number",
    label: "Copy number",
    value: (v) => copyNumberText(v.copy_number),
  },
  {
    label: "Details",
    value: (v) => COMPONENT_DETAIL_SUMMARY[v?.type]?.(v) ?? "",
  },
];

// Each component type has its own details groups (the same spec as its entity
// form), so the details groups are a function of the component value.
export const componentDetailGroups = (item) => {
  if (item?.type === "Polymer") return POLYMER_GROUPS;
  if (item?.type === "Chemical") return CHEMICAL_GROUPS;
  return [];
};

// What an entity's group entry needs to render a `components` array in its
// details: the mini-table columns and the item's details groups for the mini
// row's own ▸.
export const COMPONENT_ITEM_SPEC = {
  itemColumns: COMPONENT_COLUMNS,
  itemGroups: componentDetailGroups,
};
