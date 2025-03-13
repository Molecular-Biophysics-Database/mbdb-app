import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Measurements from "../measurements/Measurements";

export default function MeasurementsTab({ name }) {
  const fieldName = "measurements";

  const tooltip =
    "List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the sample composition and measurement times
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Measurement"
        required
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
