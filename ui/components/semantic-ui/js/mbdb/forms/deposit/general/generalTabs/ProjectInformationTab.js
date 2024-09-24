import React from "react";
import RecordInformation from "../projectInformation/RecordInformation";
import Depositors from "../projectInformation/depositors/Depositors";
import ArrayField from "../../buildingBlocks/ArrayField";
import AssociatedPublication from "../projectInformation/associatedPublication/AssociatedPublication";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../../buildingBlocks/RORInstitutionResultListItem";

function ProjectInformationTab({ name }) {
  const { getFieldData } = useFieldData();

  return (
    <>
      <div className="mb-3">
        <RecordInformation name={`${name}.record_information`} />
      </div>
      <div className="mb-3">
        <AssociatedPublication name={name} />
      </div>
      <div className="mb-3">
        <Depositors name={`${name}.depositors`} />
      </div>
      <div>
        <ArrayField
          name={name}
          label="Funding reference"
          fieldName="funding_references"
          tooltip="List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`funding reference ${index + 1}`}
              tooltip="List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects"
            >
              <VocabularyRemoteSelectField
                overriddenComponents={{
                  "VocabularyRemoteSelect.ext.ResultsList.item":
                    RORInstitutionResultListItem,
                }}
                vocabulary="grants"
                fieldPath={`${arrayName}.${index}`}
                modalHeader={
                  getFieldData({
                    fieldPath: `${arrayName}.${index}`,
                    fieldRepresentation: "text",
                  }).label
                }
              />
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}

export default ProjectInformationTab;
