import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import {
  VocabularySelectField,
  serializeVocabularySuggestions,
} from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";
import { useDepositApiClient } from "@js/oarepo_ui";

// The vocabulary suggest API response carries system fields (e.g. "created",
// "updated") that aren't part of the instrument relation and may not be
// ISO-formatted (the UI-serialized representation renders them for display).
// Strip them here so they never get stored on the record and fail indexing.
const stripSystemFields = (suggestion) => {
  const { created, updated, ...rest } = suggestion;
  return rest;
};

export default function Instrument({ name }) {
  const { values: recordMetadata } = useDepositApiClient();

  const resourceType =
    recordMetadata?.metadata?.general_parameters?.record_information
      ?.resource_type;

  const serializeSuggestions = (suggestions) =>
    serializeVocabularySuggestions(suggestions)
      .filter((opt) =>
        opt.props?.technique
          ? opt.props.technique.startsWith(resourceType)
          : true
      )
      .map(stripSystemFields);

  return (
    <>
      <FormWrapper
        headline="Instrument"
        tooltip="Information about the instrument being used to collect (measure) the raw data annotated by this record"
      >
        <div className="flex">
          <div>
            <VocabularySelectField
              search={(options) => options}
              type="instruments"
              label={<FieldLabel htmlFor={name} icon="" />}
              serializeSuggestions={serializeSuggestions}
              fieldPath={name}
              placeholder="Instrument"
              clearable
            />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}
