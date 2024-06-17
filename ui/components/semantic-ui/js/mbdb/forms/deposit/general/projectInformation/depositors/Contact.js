import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";

function Contact( { name } ) {

  return (
    <>
        <div className='flex'>
          <div className='mr-3'>
            <CustomField
              name={name}
              label='Given name'
              fieldName='given_name'
              required={true}
              tooltip='The given name(s), including middlename(s), of the person'
            />
          </div>
          <div>
            <CustomField
              name={name}
              label='Family name'
              fieldName='family_name'
              required={true}
              tooltip='The family name(s) of the person'
            />
          </div>
        </div>
        <div className="flex">
            <div className="mr-3">
                <ArrayField
                    name={name}
                    label='identifier'
                    fieldName='identifiers'
                    tooltip='Persistent personal identifiers, currently only ORCIDs are allowed'
                    renderChild={({ arrayName, index }) => (
                      <CustomField
                        name={`${arrayName}.${index}`}
                        label={`identifier ${index + 1}`}
                        tooltip='Persistent personal identifiers, currently only ORCIDs are allowed'
                      />
                    )}
                />
            </div>
            <div>
              <ArrayField
                name={name}
                label='affiliation'
                fieldName='affiliations'
                tooltip='The affiliation of the person. Note that this is based on the Research Organization Registry (ROR)'
                renderChild={({ arrayName, index }) => (
                  <VocabularySelectField
                    search={(options) => options}
                    type="affiliations"
                    externalAuthority={true}
                    label={
                      <FieldLabel
                        htmlFor={`${arrayName}.${index}`}
                        icon=""
                      />
                    }
                    fieldPath={`${arrayName}.${index}`}
                    placeholder={`affiliation ${index + 1}`}
                  />
                )}
              />
            </div>
        </div>
    </>
  );
}

export default Contact;