import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import Identifier from "../../../buildingBlocks/Identifier";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../../../buildingBlocks/RORInstitutionResultListItem";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import { useFormikContext, getIn } from "formik";

function Contact({ name, copy }) {
  const { getFieldData } = useFieldData();
  const { values, setFieldValue } = useFormikContext();

  const depositor = getIn(
    values,
    `metadata.general_parameters.depositors.depositor`
  );

  const principalContact = `metadata.general_parameters.depositors.principal_contact`;

  return (
    <>
      {copy && (
        <>
          <div className="flex mb-3">
            <input
              className="mr-3 accent-dark"
              type="checkbox"
              onChange={(e) => {
                if (e.target.checked) {
                  if (depositor) {
                    setFieldValue(principalContact, depositor);
                    console.log(
                      depositor,
                      "Hello depositor - on checkbox toggle"
                    );
                  }
                } else {
                  console.log("is this even rendering");
                  setFieldValue(principalContact, {});
                }
              }}
            />
            <div className="font-JostMedium">Same as depositor</div>
          </div>
        </>
      )}
      <div className="flex">
        <div className="mr-3">
          <CustomField
            name={name}
            label="Given name"
            fieldName="given_name"
            required
            tooltip="The given name(s), including middlename(s), of the person"
          />
        </div>
        <div>
          <CustomField
            name={name}
            label="Family name"
            fieldName="family_name"
            required
            tooltip="The family name(s) of the person"
          />
        </div>
      </div>
      <div className="flex">
        <div className="mr-3">
          <ArrayField
            name={name}
            label="identifier"
            fieldName="identifiers"
            tooltip="Persistent personal identifiers, currently only ORCIDs are allowed"
            renderChild={({ arrayName, index }) => (
              <Identifier
                name={`${arrayName}.${index}`}
                label={`Identifier ${index + 1}`}
              />
            )}
          />
        </div>
        <div>
          <ArrayField
            name={name}
            label="affiliation"
            fieldName="affiliations"
            tooltip="The affiliation of the person. Note that this is based on the Research Organization Registry (ROR)"
            renderChild={({ arrayName, index }) => (
              <FormWrapper
                headline={`affiliation ${index + 1}`}
                tooltip="The affiliation of the person. Note that this is based on the Research Organization Registry (ROR)"
                colorSchema="light"
              >
                <VocabularyRemoteSelectField
                  overriddenComponents={{
                    "VocabularyRemoteSelect.ext.ResultsList.item":
                      RORInstitutionResultListItem,
                  }}
                  vocabulary="affiliations"
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
      </div>
    </>
  );
}

export default Contact;
