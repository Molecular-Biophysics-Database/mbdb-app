import React from "react";
import RecordInformation from "../recordInformation/RecordInformation";
import Depositors from "../recordInformation/depositors/Depositors";
import ArrayField from "../../buildingBlocks/ArrayField";
import AssociatedPublication from "../recordInformation/associatedPublication/AssociatedPublication";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import FundingReference from "../recordInformation/depositors/FundingReference";

export default function RecordInformationTab({ name }) {
  const tooltip =
    "List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects";

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          The bibliographic, funding, and assosiated publication information
        </FormWrapper>
      </div>
      <div className="mb-3">
        <RecordInformation name={`${name}.record_information`} />
      </div>
      <div className="mb-3">
        <AssociatedPublication name={name} />
      </div>
      <div className="mb-3">
        <Depositors name={`${name}.depositors`} />
      </div>

      <ArrayField
        name={name}
        label="Funding reference"
        fieldName="funding_references"
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => (
          <FundingReference
            arrayName={arrayName}
            index={index}
            tooltip={tooltip}
          />
        )}
      />
    </>
  );
}
