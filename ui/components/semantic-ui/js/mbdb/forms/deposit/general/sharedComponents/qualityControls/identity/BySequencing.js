import React from "react";
import CustomField from "../../../../buildingBlocks/CustomField";
import FormWrapper from "../../../../buildingBlocks/FormWrapper";
import OptionField from "../../../../buildingBlocks/OptionField";

function BySequencing({ name, colorSchema }) {
  const methodOptions = [
    {
      value: "Mass spectrometry-Mass spectrometry",
      label: "Mass spectrometry-Mass spectrometry",
    },
    { value: "Edman degradation", label: "Edman degradation" },
    { value: "Sanger sequencing", label: "Sanger sequencing" },
    {
      value: "Next generation sequencing",
      label: "Next generation sequencing",
    },
  ];

  return (
    <>
      <FormWrapper
        headline="By sequencing"
        colorSchema={colorSchema}
        tooltip="How identity was assessed by sequencing, if applicable"
      >
        <div className="flex">
          <div className="mr-3">
            <OptionField
              name={name}
              required
              fieldName="method"
              label="Method"
              options={methodOptions}
              tooltip="The method used to assess identity"
            />
          </div>
          <div>
            <CustomField
              name={name}
              required
              fieldName="coverage"
              label="Coverage"
              tooltip="The amount of the total (expected) sequence that was actually observed by sequencing in percent"
            />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default BySequencing;
