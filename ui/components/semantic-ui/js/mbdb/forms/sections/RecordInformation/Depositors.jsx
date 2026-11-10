import React from "react";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { PersonForm } from "./PersonForm";
import { Contributors } from "./Contributors";
import { DEPOSITORS_PATH } from "./path";

// The depositors of the record: the required Depositor and Principal
// contact (the person form inline, each under its model-titled group), then
// the optional Contributors behind a plus button. Titles, help and required
// come from the model (the depositors subtree is in the ui_model).
export const Depositors = () => (
  <>
    <FieldGroup fieldPath={`${DEPOSITORS_PATH}.depositor`} nested>
      <PersonForm fieldPath={`${DEPOSITORS_PATH}.depositor`} />
    </FieldGroup>
    <FieldGroup fieldPath={`${DEPOSITORS_PATH}.principal_contact`} nested>
      <PersonForm fieldPath={`${DEPOSITORS_PATH}.principal_contact`} />
    </FieldGroup>
    <Contributors />
  </>
);
