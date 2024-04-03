import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import ArrayField from "../buildingBlocks/ArrayField";
import ChemicalEnvironment from "../chemicalEnvironment/ChemicalEnvironment";
import UseDefault from "../buildingBlocks/UseDefault";
import { useFormikContext } from 'formik';

function ChemicalEnvironmentTab( { name } ) {

    const { values } = useFormikContext();

    const fieldName = 'chemical_environments'

    UseDefault(values, `${name}.${fieldName}[0].name`, "" );

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
                        tooltipHeader='Composition of the chemical environment (colloquially known as the buffer)'
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