import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import MeasurementPositions from "../measurementPositions/MeasurementPositions";

function MeasurementPositionsTab({ name }) {
  const fieldName = "measurement_positions";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about each measurement position in each flow channel where
          measurements were performed
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Measurement position"
        required
        fieldName={fieldName}
        tooltip="Information about each of the positions where data was collected including reference positions"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Measurement position ${index + 1}`}
            tooltip="Information about each of the positions where data was collected including reference positions"
          >
            <MeasurementPositions name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default MeasurementPositionsTab;
