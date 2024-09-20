import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../buildingBlocks/RORInstitutionResultListItem";

function Instrument({ name }) {
  const { getFieldData } = useFieldData();

  return (
    <>
      <FormWrapper
        headline="Instrument"
        tooltip="Information about the instrument being used to collect (measure) the raw data annotated by this record"
      >
        <div className="flex">
          <div>
            <VocabularyRemoteSelectField
              overriddenComponents={{
                "VocabularyRemoteSelect.ext.ResultsList.item":
                  RORInstitutionResultListItem,
              }}
              vocabulary="instruments"
              multiple={true}
              fieldPath={name}
              modalHeader={
                getFieldData({
                  fieldPath: name,
                  fieldRepresentation: "text",
                }).label
              }
              {...getFieldData({
                fieldPath: name,
                icon: "building outline",
              })}
            />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default Instrument;
