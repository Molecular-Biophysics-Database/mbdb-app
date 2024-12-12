import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Measurements from "../measurements/Measurements";

function MeasurementsTab({ name }) {
  const fieldName = "measurements";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the content of the syringe and the cell
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Measurement"
        required
        fieldName={fieldName}
        tooltip="List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Measurement ${index + 1}`}
            tooltip="List of the information about each measurement. This includes target(s), ligand(s), chemical environment, and the position of the sample within the instrument"
          >
            <Measurements name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default MeasurementsTab;
