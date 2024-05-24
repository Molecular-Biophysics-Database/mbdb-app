import React from "react";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import InjectionParameter from "./InjectionParameter";

function Titration( { name } ) {

  return (
    <>
        <div className="flex flex-col">
            <div>
                <CustomField
                    name={name}
                    fieldName='number_injections'
                    label='Number of injections'
                    tooltip='Number of injections performed in the measurement'
                    type='number'
                />
            </div>
            <div>
                <ArrayField
                    name={name}
                    label="Injection parameter"
                    fieldName='injection_parameters'
                    tooltip='Characteristics of each injection (i. e. number of injections at a specific volume of 0.2 ml)'
                    renderChild={({ arrayName, index }) => (
                        <FormWrapper
                            headline={`Injection parameter ${index + 1}`}
                            tooltip='Characteristics of each injection (i. e. number of injections at a specific volume of 0.2 ml)'
                        >
                            <InjectionParameter
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
        </div>
    </>
  );
}

export default Titration;