import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import ArrayField from "../buildingBlocks/ArrayField";
import Measurement from "../measurement/Measurement";
import UseDefault from "../buildingBlocks/UseDefault";
import { useFormikContext } from "formik";

function MeasurementTab( { name } ) {

    const { values } = useFormikContext();

    const fieldName = 'measurements'

    UseDefault(values, `${name}.${fieldName}`, [{}] );

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Measurement"
                required={true}
                fieldName={fieldName}
                tooltip='List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Measurement ${index + 1}`}
                        tooltipHeader='List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument'
                    >
                        <div>
                            <Measurement
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
  
  export default MeasurementTab;