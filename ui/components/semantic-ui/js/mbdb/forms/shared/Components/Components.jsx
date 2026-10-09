import React from "react";
import PropTypes from "prop-types";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { ComponentFields } from "./ComponentFields";
import { COMPONENT_TYPES } from "./constants";
import { COMPONENT_COLUMNS, componentDetailGroups } from "./columns";

// The parts of an assembly: a summary table with the copy number and the
// item's identity (Details) visible, each component edited in a second-level
// modal (design Components). Components have no `id` in the model, so no
// `withIds`. The columns live in ./spec so the entity's details mini table
// shows the same ones.
export const Components = ({ fieldPath }) => (
  <ModalArrayField
    fieldPath={fieldPath}
    // the model: required, minItems 1, in every use
    minItems={1}
    itemLabel={(v) => v?.name || `New ${v?.type ?? ""} component`}
    columns={COMPONENT_COLUMNS}
    newItemOptions={COMPONENT_TYPES.map((type) => ({
      label: type,
      value: { type },
    }))}
    renderForm={(itemPath) => <ComponentFields fieldPath={itemPath} />}
    detailGroups={componentDetailGroups}
    // Name, Type and Copy number are already in the row: do not repeat them
    detailProps={{ exclude: ["name", "type", "copy_number"] }}
    // a nested modal's Done button reads "Done, back to component"
    crumbNoun="component"
  />
);

Components.propTypes = {
  // the array path (`${itemPath}.components`)
  fieldPath: PropTypes.string.isRequired,
};
