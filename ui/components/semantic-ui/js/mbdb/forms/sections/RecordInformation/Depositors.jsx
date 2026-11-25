import React from "react";
import { ModalObjectField } from "@js/mbdb/forms/building-blocks/ModalObjectField";
import { PersonForm, PERSON_GROUPS } from "./PersonForm";
import { Contributors } from "./Contributors";
import { DEPOSITORS_PATH } from "./path";

// The depositors of the record: the required Depositor and Principal
// contact, then the optional Contributors. Every person is a summary row
// edited in a modal. Titles, help and required come from the model (the
// depositors subtree is in the ui_model).
export const Depositors = () => (
  <>
    {["depositor", "principal_contact"].map((person) => (
      <ModalObjectField
        key={person}
        fieldPath={`${DEPOSITORS_PATH}.${person}`}
        summary={(v) => [v?.given_name ?? "", v?.family_name ?? ""]}
        detailGroups={PERSON_GROUPS}
        renderForm={(path) => <PersonForm fieldPath={path} />}
      />
    ))}
    <Contributors />
  </>
);
