import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import RawMeasurementFile from "../rawMeasurementFiles/RawMeasurementFile";
import UseDefault from "../../buildingBlocks/UseDefault";

function RawMeasurementFilesTab( { name } ) {

    const fieldName = 'raw_measurement_files';

    UseDefault(`${name}.${fieldName}`, [{}] );

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Raw measurement file"
                required={true}
                fieldName={fieldName}
                tooltip='List of file(s) containing the raw measurements'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Raw measurement file ${index + 1}`}
                        tooltip='List of file(s) containing the raw measurements'
                    >
                        <div>
                            <RawMeasurementFile
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

  export default RawMeasurementFilesTab;