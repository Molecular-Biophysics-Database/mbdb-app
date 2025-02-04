import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayFieldCopyPaste from "@mbdb_deposit/buildingBlocks/ArrayFieldCopyPaste";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Measurements from "../measurements/Measurements";

export default function MeasurementsTab({ name }) {
  const fieldName = "measurements";

  const tooltip =
    "List of measurements where the complete output from a single sensor going through the measurement protocol is considered a separate measurement";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the sample that was flowing over each measurement
          position at each step in the measurement protocol
        </FormWrapper>
      </div>
      <ArrayFieldCopyPaste
        name={name}
        label="Measurement"
        required
        method="spr"
        fieldName={fieldName}
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => (
          <FormWrapper headline={`Measurement ${index + 1}`} tooltip={tooltip}>
            <Measurements name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
