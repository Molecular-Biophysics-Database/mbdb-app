import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Measurements from "../measurements/Measurements";

function MeasurementsTab( { name } ) {

    const fieldName = 'measurements';

    UseDefault(`${name}.${fieldName}`, [{}] );

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Measurement"
                required={true}
                fieldName={fieldName}
                tooltip='List of measurements where the complete output from a single sensor going through the measurement protocol is considered a separate measurement'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Measurement ${index + 1}`}
                        tooltip='List of measurements where the complete output from a single sensor going through the measurement protocol is considered a separate measurement'
                    >
                        <div>
                            <Measurements
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
  
  export default MeasurementsTab;