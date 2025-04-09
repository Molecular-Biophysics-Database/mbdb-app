import React from "react";
import { useFieldData } from "@js/oarepo_ui";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { OpenAireProjectResultListItem } from "../../../buildingBlocks/OpenAireProjectResultListItem";

function FundingReference({ arrayName, index, tooltip }) {
  const { getFieldData } = useFieldData();

  const field = getFieldData({
    fieldPath: `${arrayName}.${index}`,
    fieldRepresentation: "text",
  });

  return (
    <FormWrapper
      headline={`Funding reference ${index + 1}`}
      tooltip={tooltip}
    >
      <VocabularyRemoteSelectField
        overriddenComponents={{
            "VocabularyRemoteSelect.ext.ResultsList.item":
                OpenAireProjectResultListItem,
        }}
        vocabulary="grants"
        fieldPath={`${arrayName}.${index}`}
        modalHeader={field?.label || `Funding reference ${index + 1}`}
      />
    </FormWrapper>
  );
}

export default FundingReference;