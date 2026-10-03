import React from "react";
import PropTypes from "prop-types";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { POLYMER_GROUPS } from "@js/mbdb/forms/entities/Polymer";
import { CHEMICAL_GROUPS } from "@js/mbdb/forms/entities/Chemical";
import { ComponentFields } from "./ComponentFields";
import { COMPONENT_TYPES } from "./constants";

// -1 is "unknown" in the table only; the modal input keeps -1.
const copyNumberText = (n) => (n === -1 ? "unknown" : n ?? "");

// Each component type has its own details groups (the same spec as its entity
// form), which is why detailGroups is a function of the item value.
const DETAIL_GROUPS = { Polymer: POLYMER_GROUPS, Chemical: CHEMICAL_GROUPS };

// The parts of an assembly: a summary table with the copy number visible, each
// component edited in a second-level modal (design Components). Components have
// no `id` in the model, so no `withIds`.
export const Components = ({ fieldPath }) => (
  <ModalArrayField
    fieldPath={fieldPath}
    // the model: required, minItems 1, in every use
    minItems={1}
    itemLabel={(v) => v?.name || `New ${v?.type ?? ""} component`}
    columns={[
      { label: "Name", value: (v) => v.name },
      { label: "Type", value: (v) => v.type },
      { label: "Copy number", value: (v) => copyNumberText(v.copy_number) },
    ]}
    newItemOptions={COMPONENT_TYPES.map((type) => ({
      label: type,
      value: { type },
    }))}
    renderForm={(itemPath) => <ComponentFields fieldPath={itemPath} />}
    detailGroups={(v) => DETAIL_GROUPS[v?.type] ?? []}
    // Name, Type and Copy number are already in the row: do not repeat them
    detailProps={{ exclude: ["name", "type", "copy_number"] }}
  />
);

Components.propTypes = {
  // the array path (`${itemPath}.components`)
  fieldPath: PropTypes.string.isRequired,
};
