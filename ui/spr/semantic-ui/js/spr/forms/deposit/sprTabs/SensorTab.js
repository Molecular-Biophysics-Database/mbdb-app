import React from "react";
import Sensor from "../sensor/Sensor";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

function SensorTab({ name }) {
  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the sensors used in the measurement
        </FormWrapper>
      </div>
      <Sensor name={`${name}.sensor`} />
    </>
  );
}

export default SensorTab;
