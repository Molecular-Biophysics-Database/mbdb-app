import React from "react";
import FormWrapper from "../../../../buildingBlocks/FormWrapper";
import ValueUnit from "../../../../buildingBlocks/ValueUnit";

function DeviationFromExpectedMass({ name, colorSchema }) {
  const unitOptions = [
    { value: "g/mol", label: "g/mol" },
    { value: "Da", label: "Da" },
    { value: "kDa", label: "kDa" },
    { value: "MDa", label: "MDa" },
  ];

  return (
    <>
      <FormWrapper
        headline="Deviation from expected mass"
        colorSchema={colorSchema}
        tooltip="The amount, including unit, by which the obtained intact mass deviated from the expected intact mass (e.g. 1kDa)"
      >
        <div>
          <ValueUnit
            name={name}
            unitRequired={true}
            valueRequired={true}
            options={unitOptions}
            tooltipValue="The numerical value of the molecular weight, -1 if unknown"
            tooltipUnit="The unit of the molecular weight"
          />
        </div>
      </FormWrapper>
    </>
  );
}

export default DeviationFromExpectedMass;
