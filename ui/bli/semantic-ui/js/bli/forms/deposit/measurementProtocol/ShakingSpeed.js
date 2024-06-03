import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";
import ValueError from "@mbdb_deposit/buildingBlocks/ValueError";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

function ShakingSpeed( { colorSchema, name } ) {

    const unitOptions = [
        { value: 'RPM', label: 'RPM' },
      ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline='Shaking speed'
        tooltip='The numerical value of the shaking speed of the plate during the measurement step in the units defined in the general parameters'
      >
          <ValueUnit
            options={unitOptions}
            name={name}
            tooltipValue='The numerical value of the shaking speed of the plate during the measurement step in the units defined in the general parameters'
            tooltipUnit='The reported error of the value of the shaking speed (e.g. standard deviation, % error)'
            valueRequired={true}
            unitRequired={true}
          />
          <OptionalField
                name={name}
                label='Value error'
                fieldName='value_error'
                tooltip='The expected error of the result in terms of a 95 % confidence interval'
                renderChild={({ optionalFieldName }) => (
                    <div>
                        <ValueError
                            name={optionalFieldName}
                        />
                    </div>
                )}
            />
      </FormWrapper>
    </>
  );
}

export default ShakingSpeed;