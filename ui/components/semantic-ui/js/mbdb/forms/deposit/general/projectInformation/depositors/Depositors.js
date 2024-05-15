import ArrayField from "../../../buildingBlocks/ArrayField";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import Contact from "./Contact";

function Depositors( { name } ) {

  return (
    <>
        <div className="mb-3">
            <FormWrapper
                headline='Depositor'
                tooltip='The person who made the deposition to MBDB'
            >
                <Contact name={`${name}.depositor`} />
            </FormWrapper>
        </div>
        <div className="mb-3">
            <FormWrapper 
                headline='Principal contact'
                tooltip='The person responsible for the record and the one to contact for inquiries, would typically be the principle investigator group leader, or laboratory head'
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
                        tooltip='List of other people who contributed to generating the deposited data, metadata, results , or the deposition itself'
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