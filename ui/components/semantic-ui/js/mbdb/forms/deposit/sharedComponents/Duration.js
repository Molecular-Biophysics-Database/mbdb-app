import React from "react";
import ValueUnit from "../buildingBlocks/ValueUnit";
import FormWrapper from "../buildingBlocks/FormWrapper";

export default function Duration({ name, tooltip, colorSchema }) {
  const unitOptions = [
    { value: "nanoseconds", label: "nanoseconds" },
    { value: "microseconds", label: "microseconds" },
    { value: "milliseconds", label: "milliseconds" },
    { value: "seconds", label: "seconds" },
    { value: "minutes", label: "minutes" },
    { value: "hours", label: "hours" },
    { value: "days", label: "days" },
    { value: "months", label: "months" },
    { value: "years", label: "years" },
  ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Duration"
        tooltip={tooltip}
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="The numerical value of the time point or duration"
          tooltipUnit="The unit of the time duration"
        />
      </FormWrapper>
    </>
  );
}
