import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

export default function CellTemperature({ colorSchema, name }) {
  const unitOptions = [
    { value: "K", label: "K" },
    { value: "°C", label: "°C" },
    { value: "°F", label: "°F" },
  ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Cell temperature"
        tooltip="Temperature of the cell in which the sample is measured"
        required
        name={name}
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="The numerical value of the temperature"
          tooltipUnit="The unit of the temperature"
          valueRequired
          unitRequired
        />
      </FormWrapper>
    </>
  );
}
