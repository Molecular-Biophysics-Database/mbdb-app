import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import MeasurementProtocol from "../measurementProtocol/MeasurementProtocol";

function MeasurementProtocolStepTab({ name }) {
  const fieldName = "measurement_protocol";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about each step in the measurement protocol
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Measurement protocol step"
        required
        fieldName={fieldName}
        tooltip="List of the steps in the measurement protocol"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Measurement protocol step ${index + 1}`}
            tooltip="List of the steps in the measurement protocol"
          >
            <MeasurementProtocol name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default MeasurementProtocolStepTab;
