import React from "react";
import { ModalObjectField } from "@js/mbdb/forms/building-blocks/ModalObjectField";
import { AssociatedPublicationForm } from "./AssociatedPublicationForm";
import { ASSOCIATED_PUBLICATION_PATH } from "./path";

// The details of the publication summary row: the union of every variant's
// fields; only the filled ones show (an Article has no publisher row).
export const PUBLICATION_GROUPS = [
  {
    title: "Publication",
    fields: ["type", "pid", "title", "journal", "publisher", "degree_type"],
  },
];

// The summary cells of the publication row: Pid, Title, then the type.
const summaryPublication = (v) => [v?.pid ?? "", v?.title ?? "", v?.type ?? ""];

// The optional Associated publication behind a plus button (the former RDM
// 12 form's "+ Associated publication"): Add seeds the type with "Article"
// (the former form's initialValue), the modal holds the form. Label, help and
// the optional-not-required flags come from the model.
export const AssociatedPublication = () => (
  <ModalObjectField
    fieldPath={ASSOCIATED_PUBLICATION_PATH}
    summary={summaryPublication}
    initialValue={{ type: "Article" }}
    renderForm={(path) => <AssociatedPublicationForm fieldPath={path} />}
    detailGroups={PUBLICATION_GROUPS}
  />
);
