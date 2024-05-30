import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

function CellVolume( { colorSchema, name } ) {

    const unitOptions = [
      { value: 'ml', label: 'ml' },
      { value: 'µl', label: 'µl' },
    ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline='Cell volume'
        tooltip='Volume of the cell in which the sample is measured'>
          <ValueUnit
            options={unitOptions}
            name={name}
            tooltipValue='Volume of the sample'
            tooltipUnit='Unit of the volume'
            valueRequired={true}
            unitRequired={true}
          />
      </FormWrapper>
    </>
  );
}

export default CellVolume;