import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";



function Instrument({ name }) {
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
              // filter on the technique field
              // TODO: get the value of metadata.general_parameters.record_information.resource_type
              // instead of using hardcoded "BLI"
              filterFunction={opt => opt.props.technique.startsWith("BLI")}
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
