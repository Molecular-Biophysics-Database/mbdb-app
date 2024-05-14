import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import ChemicalEnvironment from "../chemicalEnvironment/ChemicalEnvironment";
import UseDefault from "../../buildingBlocks/UseDefault";

function ChemicalEnvironmentTab( { name } ) {

    const fieldName = 'chemical_environments';

    UseDefault(`${name}.${fieldName}`, [{}] );

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Chemical environment"
                required={true}
                fieldName={fieldName}
                tooltip='Composition of the chemical environment (colloquially known as the buffer)'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Chemical environment ${index + 1}`}
                        tooltip='Composition of the chemical environment (colloquially known as the buffer)'
                    >
                        <div>
                            <ChemicalEnvironment
                                name={`${arrayName}.${index}`}
                            />
                        </div>
                    </FormWrapper>
                )}
            />
        </div>
      </>
    );
  }
  
  export default ChemicalEnvironmentTab;