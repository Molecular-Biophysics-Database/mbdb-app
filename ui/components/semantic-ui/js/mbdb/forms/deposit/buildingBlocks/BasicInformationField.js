import React from "react";
import FormWrapper from "./FormWrapper";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";

function BasicInformationField({ name, colorSchema }) {
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
        <VocabularySelectField
          search={(options) => options}
          type="chemicals"
          externalAuthority={true}
          label={<FieldLabel htmlFor={`${name}.basic_information`} icon="" />}
          fieldPath={`${name}.basic_information`}
          placeholder="Basic information"
        />
      </FormWrapper>
    </>
  );
}

export default BasicInformationField;
