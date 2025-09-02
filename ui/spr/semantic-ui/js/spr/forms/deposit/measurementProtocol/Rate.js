import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

export default function Rate({ colorSchema, name, tooltip }) {
  const unitOptions = [
    { value: "mL/min", label: "mL/min" },
    { value: "µl/s", label: "µl/s" },
  ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Rate"
        tooltip={tooltip}
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="The numerical value of the flowrate"
          tooltipUnit="The unit of the flowrate"
          valueRequired
          unitRequired
        />
      </FormWrapper>
    </>
  );
}
