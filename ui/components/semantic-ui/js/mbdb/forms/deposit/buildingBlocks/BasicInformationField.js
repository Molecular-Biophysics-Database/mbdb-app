import React from "react";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";
import FormWrapper from "./FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "./RORInstitutionResultListItem";

function BasicInformationField({ name, colorSchema }) {
  const { getFieldData } = useFieldData();

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Basic information"
        tooltip="Basic information about the chemical. Note that this information is based on PubChem records"
        >
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
          <div className="flex">
            <div>
              <VocabularyRemoteSelectField
              overriddenComponents={{
                  "VocabularyRemoteSelect.ext.ResultsList.item":
                  RORInstitutionResultListItem,
              }}
              vocabulary="chemicals"
              fieldPath={name}
              modalHeader={
                  getFieldData({
                      fieldPath: name,
                      fieldRepresentation: "text",
                  }).label
              }
              />
            </div>
              <div className="text-accent ml-1">
                <Tooltip
                  title={
                    <Typography style={{color: "white", fontSize: 13}}>
                      This field is required and cannot be left blank or unset
                    </Typography>
                  }
                >
                  <span>*</span>
                </Tooltip>
              </div>
            </div>
      </FormWrapper>
    </>
  );
}

export default BasicInformationField;
