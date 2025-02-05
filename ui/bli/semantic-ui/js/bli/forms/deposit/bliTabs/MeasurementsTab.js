import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayFieldCopyPaste from "@mbdb_deposit/buildingBlocks/ArrayFieldCopyPaste";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Measurements from "../measurements/Measurements";

export default function MeasurementsTab({ name }) {
  const tooltip =
    "List of measurement where each step from each sensor is considered a single measurement";

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
