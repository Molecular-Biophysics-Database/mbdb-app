import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Sensors from "../sensors/Sensors";

function SensorsTab({ name }) {
  const fieldName = "sensors";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="-mt-3">
        <ArrayField
          name={name}
          label="Sensor"
          required
          fieldName={fieldName}
          tooltip="List of the sensors used for the measurements, reference sensors included"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Sensor ${index + 1}`}
              tooltip="List of the sensors used for the measurements, reference sensors included"
            >
              <div>
                <Sensors name={`${arrayName}.${index}`} />
              </div>
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}

export default SensorsTab;
