import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayFieldCopyPaste from "@mbdb_deposit/buildingBlocks/ArrayFieldCopyPaste";
import Measurement from "../measurement/Measurement";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

function MeasurementTab({ name }) {
  const fieldName = "measurements";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="-mt-3">
        <ArrayFieldCopyPaste
          name={name}
          label="Measurement"
          required
          method="mst"
          fieldName={fieldName}
          tooltip="List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Measurement ${index + 1}`}
              tooltip="List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument"
            >
              <div>
                <Measurement name={`${arrayName}.${index}`} />
              </div>
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}

export default MeasurementTab;
