import React from "react";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { PersonForm, PERSON_GROUPS } from "./PersonForm";
import { DEPOSITORS_PATH } from "./path";

// The text of a person summary cell / the table's two name columns.
export const personName = (v) =>
  [v?.given_name, v?.family_name].filter(Boolean).join(" ");

// The contributors: one row per person in a summary table, each edited in a
// modal that holds the Person form. Label and help come from the model.
export const Contributors = () => (
  <ModalArrayField
    fieldPath={`${DEPOSITORS_PATH}.contributors`}
    itemLabel={(v) => `Contributor: ${personName(v) || "new"}`}
    newItemOptions={[{ label: "contributor", value: {} }]}
    columns={[
      { label: "Given name", value: (v) => v?.given_name ?? "" },
      { label: "Family name", value: (v) => v?.family_name ?? "" },
    ]}
    detailGroups={PERSON_GROUPS}
    renderForm={(itemPath) => <PersonForm fieldPath={itemPath} />}
  />
);
