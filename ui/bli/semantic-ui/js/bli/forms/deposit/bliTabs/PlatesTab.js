import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Plates from "../plates/Plates";

function PlatesTab( { name } ) {

    const fieldName = 'plates'

    UseDefault(`${name}.${fieldName}`, [{}] );

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Plate"
                required={true}
                fieldName={fieldName}
                tooltip='List of the plate types used for the measurements'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Plate ${index + 1}`}
                        tooltip='List of the plate types used for the measurements'
                    >
                        <div>
                            <Plates
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
  
  export default PlatesTab;