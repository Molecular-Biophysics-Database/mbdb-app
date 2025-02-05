import React from "react";
import ValueUnit from "../buildingBlocks/ValueUnit";
import FormWrapper from "../buildingBlocks/FormWrapper";

export default function Temperature({ name, tooltip, colorSchema }) {
  const unitOptions = [
    { value: "K", label: "K" },
    { value: "°C", label: "°C" },
    { value: "°F", label: "°F" },
  ];

  return (
    <>
      <FormWrapper
        headline="Temperature"
        colorSchema={colorSchema}
        tooltip={tooltip}
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="The numeric value of the temperature"
          tooltipUnit="The unit of temperature"
        />
      </FormWrapper>
    </>
  );
}
