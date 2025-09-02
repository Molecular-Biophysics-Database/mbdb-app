import React from "react";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

export default function SampleFlowrate({ name, colorSchema }) {
  const unitOptions = [
    { value: "mL/min", label: "mL/min" },
    { value: "µl/s", label: "µl/s" },
  ];

  return (
    <>
      <FormWrapper
        headline="Sample flowrate"
        tooltip="Numerical value of the sample flowrate"
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
