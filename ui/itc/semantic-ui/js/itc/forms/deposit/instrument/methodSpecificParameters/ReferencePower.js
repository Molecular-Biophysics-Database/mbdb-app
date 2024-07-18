import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

function ReferencePower({ colorSchema, name }) {
  const unitOptions = [
    { value: "µcal/s", label: "µcal/s" },
    { value: "µJ/s", label: "µJ/s" },
  ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Reference power"
        tooltip="Energy supplied to the offset header of the reference cell to equilibrate the temperatures"
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="Value of energy supplied to the offset header of the reference cell to equilibrate the temperatures"
          tooltipUnit="Unit of reference power"
          valueRequired
          unitRequired
        />
      </FormWrapper>
    </>
  );
}

export default ReferencePower;
