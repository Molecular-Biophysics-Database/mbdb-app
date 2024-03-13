import React from "react";
import ArrayField from "../buildingBlocks/ArrayField";
import FormWrapper from "../buildingBlocks/FormWrapper";
import Contact from "../buildingBlocks/Contact";

function Depositors( { name } ) {

  return (
    <>
        <div className="mb-3">
            <FormWrapper
                headline='Depositor'
                tooltipHeader='The person who made the deposition to MBDB'
            >
                <Contact name={`${name}.depositor`} />
            </FormWrapper>
        </div>
        <div className="mb-3">
            <FormWrapper 
                headline='Principal contact'
                tooltipHeader='The person responsible for the record and the one to contact for inquiries, would typically be the principle investigator group leader, or laboratory head'
            >
                <Contact name={`${name}.principal_contact`} />
            </FormWrapper>
        </div>
        <div>
            <ArrayField
                name={name}
                label="Contributor"
                fieldName='contributors'
                tooltip='List of other people who contributed to generating the deposited data, metadata, results , or the deposition itself'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Contributor ${index + 1}`}
                        tooltipHeader='List of other people who contributed to generating the deposited data, metadata, results , or the deposition itself'
                    >
                        <Contact
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default Depositors;