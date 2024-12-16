import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayFieldCopyPaste from "@mbdb_deposit/buildingBlocks/ArrayFieldCopyPaste";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Measurements from "../measurements/Measurements";

function MeasurementsTab({ name }) {
  const fieldName = "measurements";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about each measurement for all the sensors at each step in
          the measurement protocol
        </FormWrapper>
      </div>
      <ArrayFieldCopyPaste
        name={name}
        label="Measurement"
        required
        method="bli"
        fieldName={fieldName}
        tooltip="List of measurement where each step from each sensor is considered a single measurement"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Measurement ${index + 1}`}
            tooltip="List of measurement where each step from each sensor is considered a single measurement"
          >
            <Measurements name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default MeasurementsTab;
