import React from "react";
import PropTypes from "prop-types";
import { ModalObjectField } from "@js/mbdb/forms/building-blocks/ModalObjectField";
import { StorageForm } from "./StorageForm";
import { summaryStorage } from "./summary";

export const STORAGE_GROUPS = [
  {
    title: "Storage",
    fields: ["temperature", "duration", "storage_preparation"],
  },
];

// How a complex substance was stored before measurement: one summary line in
// the entity modal, edited in a second-level modal (design Storage).
export const Storage = ({ fieldPath }) => (
  <ModalObjectField
    fieldPath={fieldPath}
    summary={summaryStorage}
    renderForm={(path) => <StorageForm fieldPath={path} />}
    detailGroups={STORAGE_GROUPS}
  />
);

Storage.propTypes = {
  // the Storage OBJECT path (`${itemPath}.storage`)
  fieldPath: PropTypes.string.isRequired,
};
