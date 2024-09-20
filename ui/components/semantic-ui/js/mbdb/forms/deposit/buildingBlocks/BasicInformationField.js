import React from "react";
import FormWrapper from "./FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "./RORInstitutionResultListItem";

function BasicInformationField({ name, colorSchema }) {
  const { getFieldData } = useFieldData();

  return (
    <>
      <FormWrapper colorSchema={colorSchema}>
        <div className="flex mb-2">
          <div className="mr-2 mt-0.5">Check you chemistry</div>
          <div>
            <a
              className="flex justify-center py-1 mr-2 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
              href="https://pubchem.ncbi.nlm.nih.gov/"
              target="_blank"
              rel="noreferrer"
            >
              PubChem
            </a>
          </div>
          <div>
            <a
              className="flex justify-center py-1 px-4 bg-dark rounded-full text-white hover:bg-secondary hover:text-dark transition-all"
              href="https://www.ebi.ac.uk/chembl/"
              target="_blank"
              rel="noreferrer"
            >
              ChEMBL
            </a>
          </div>
        </div>
        <VocabularyRemoteSelectField
          overriddenComponents={{
            "VocabularyRemoteSelect.ext.ResultsList.item":
              RORInstitutionResultListItem,
          }}
          vocabulary="chemicals"
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
            icon: false,
          })}
        />
      </FormWrapper>
    </>
  );
}

export default BasicInformationField;
