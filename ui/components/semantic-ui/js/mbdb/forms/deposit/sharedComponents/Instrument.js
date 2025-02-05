import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";
import { useDepositApiClient } from "@js/oarepo_ui";

function Instrument({ name }) {
  const { values: recordMetadata } = useDepositApiClient();

  const resourceType =
    recordMetadata?.metadata?.general_parameters?.record_information
      ?.resource_type;

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
              filterFunction={(opt) => {
                return opt.props?.technique
                  ? opt.props.technique.startsWith(resourceType)
                  : true;
              }}
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

export default Instrument;
