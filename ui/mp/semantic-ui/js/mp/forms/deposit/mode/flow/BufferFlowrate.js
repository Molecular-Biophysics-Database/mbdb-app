import React from "react";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

export default function BufferFlowrate({ name, colorSchema }) {
  const unitOptions = [
    { value: "mL/min", label: "mL/min" },
    { value: "µl/s", label: "µl/s" },
  ];

  return (
    <>
      <FormWrapper
        headline="Buffer flowrate"
        tooltip="Numerical value of the buffer flowrate"
        colorSchema={colorSchema}
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="Numerical value of the flowrate"
          tooltipUnit="The unit of the flowrate"
        />
      </FormWrapper>
    </>
  );
}
