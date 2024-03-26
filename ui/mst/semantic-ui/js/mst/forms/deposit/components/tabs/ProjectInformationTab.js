import React from "react";
import RecordInformation from "../projectInformation/RecordInformation";
import Depositors from "../projectInformation/Depositors";
import ArrayField from "../buildingBlocks/ArrayField";
import CustomField from "../buildingBlocks/CustomField";
import FormWrapper from "../buildingBlocks/FormWrapper";
import AssociatedPublication from "../projectInformation/AssociatedPublication";

function ProjectInformationTab( { name } ) {

  return (
    <>
        <div className="mb-3">
            <RecordInformation name={`${name}.record_information`} />
        </div>
        <div className="mb-3">
            <AssociatedPublication name={`${name}.associated_publication`}/>
        </div>
        <div className="mb-3">
            <Depositors name={`${name}.depositors`} />
        </div>
        <div>
            <ArrayField
                name={name}
                label='Funding reference'
                fieldName='funding_reference'
                tooltip='List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Funding reference ${index + 1}`}
                        tooltipHeader='List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects'    
                    >
                        <CustomField
                            name={`${arrayName}.${index}`}
                            label='funding reference'
                            tooltip='List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects'
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default ProjectInformationTab;