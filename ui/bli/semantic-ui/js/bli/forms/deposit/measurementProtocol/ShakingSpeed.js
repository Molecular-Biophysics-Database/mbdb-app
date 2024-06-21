import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ValueUnit from "@mbdb_deposit/buildingBlocks/ValueUnit";

function ShakingSpeed({ colorSchema, name }) {
  const unitOptions = [{ value: "RPM", label: "RPM" }];

  return (
    <>
      <div className="w-fit">
        <FormWrapper
          colorSchema={colorSchema}
          headline="Shaking speed"
          tooltip="The numerical value of the shaking speed of the plate during the measurement step in the units defined in the general parameters"
        >
          <ValueUnit
            options={unitOptions}
            name={name}
            tooltipValue="The numerical value of the shaking speed of the plate during the measurement step in the units defined in the general parameters"
            tooltipUnit="The reported error of the value of the shaking speed (e.g. standard deviation, % error)"
            valueRequired={true}
            unitRequired={true}
          />
        </FormWrapper>
      </div>
    </>
  );
}

export default ShakingSpeed;
