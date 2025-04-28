import React from "react";
import { useFieldData } from "@js/oarepo_ui";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { RORInstitutionResultListItem } from "../../../buildingBlocks/RORInstitutionResultListItem";

function Affiliation({ arrayName, index, tooltip }) {
  const { getFieldData } = useFieldData();

  const field = getFieldData({
    fieldPath: `${arrayName}.${index}`,
    fieldRepresentation: "text",
  });

  return (
    <FormWrapper
      headline={`Affiliation ${index + 1}`}
      tooltip={tooltip}
      colorSchema="light"
    >
      <VocabularyRemoteSelectField
        overriddenComponents={{
          "VocabularyRemoteSelect.ext.ResultsList.item":
            RORInstitutionResultListItem,
        }}
        vocabulary="affiliations"
        fieldPath={`${arrayName}.${index}`}
        modalHeader={field?.label || `Affiliation ${index + 1}`}
      />
    </FormWrapper>
  );
}

export default Affiliation;