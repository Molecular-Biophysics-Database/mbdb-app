import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Sensors from "../sensors/Sensors";

export default function SensorsTab({ name }) {
  const tooltip =
    "List of the sensors used for the measurements, reference sensors included";

  const fieldName = "sensors";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the sensors used in the measurement
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Sensor"
        required
        fieldName={fieldName}
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => (
          <FormWrapper headline={`Sensor ${index + 1}`} tooltip={tooltip}>
            <Sensors name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
