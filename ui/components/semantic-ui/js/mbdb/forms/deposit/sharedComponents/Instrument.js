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
                // filter on the props.technique field (which is only present when searching)...
                if (opt.props) {
                    return opt.props.technique.startsWith(resourceType);
                }
                // ... don't filter away anything if an element is already present in the field
                else {
                    return true
                }
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
