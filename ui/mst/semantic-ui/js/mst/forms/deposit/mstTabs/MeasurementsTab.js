import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayFieldCopyPaste from "@mbdb_deposit/buildingBlocks/ArrayFieldCopyPaste";
import Measurement from "../measurement/Measurement";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

export default function MeasurementsTab({ name }) {
  const fieldName = "measurements";

  const tooltip =
    "List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the individual measurements (content of the
          capillaries)
        </FormWrapper>
      </div>
      <ArrayFieldCopyPaste
        name={name}
        label="Measurement"
        required
        method="mst"
        fieldName={fieldName}
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => (
          <FormWrapper headline={`Measurement ${index + 1}`} tooltip={tooltip}>
            <Measurement name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
