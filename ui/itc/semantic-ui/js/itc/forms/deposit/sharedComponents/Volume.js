import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

function Volume({ colorSchema, name }) {
  const unitOptions = [
    { value: "ml", label: "ml" },
    { value: "µl", label: "µl" },
  ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Volume"
        tooltip="Titrant volume injected into the cell"
      >
        <ValueUnit
          options={unitOptions}
          name={name}
          tooltipValue="Volume of the sample"
          tooltipUnit="Unit of the volume"
          valueRequired
          unitRequired
        />
      </FormWrapper>
    </>
  );
}

export default Volume;
