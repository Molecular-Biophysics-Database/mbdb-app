import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

function StirringSpeed( { colorSchema, name } ) {

    const unitOptions = [
      { value: 'RPM', label: 'RPM' },
    ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline='Stirring speed'
        tooltip='Sample cell stirring speed in RPM'>
          <ValueUnit
            options={unitOptions}
            name={name}
            tooltipValue='The numerical value of the stirring speed'
            tooltipUnit='The unit of the stirring speed'
            valueRequired={true}
            unitRequired={true}
          />
      </FormWrapper>
    </>
  );
}

export default StirringSpeed;