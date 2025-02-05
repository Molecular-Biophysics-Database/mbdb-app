import React from "react";
import CustomField from "../../../../buildingBlocks/CustomField";
import OptionField from "../../../../buildingBlocks/OptionField";

export default function HomogeneityYes({ name }) {
  const methodOptions = [
    {
      value: "Size exclusion chromatography",
      label: "Size exclusion chromatography",
    },
    {
      value: "Native Gel Electrophoresis",
      label: "Native Gel Electrophoresis",
    },
    { value: "Mass photometry", label: "Mass photometry" },
  ];

  return (
    <>
      <div className="flex">
        <OptionField
          name={name}
          required
          fieldName="method"
          label="Method"
          options={methodOptions}
          tooltip="The method used to evaluate the homogeneity"
        />
        <div className="mx-3">
          <CustomField
            name={name}
            required
            fieldName="expected_number_of_species"
            label="Expected number of species"
            tooltip="The number of species that were expected to be present (e.g. 2 if monomers and dimers are expected to occur as an equilibrium; large aggregates should always be considered as being unexpected in this regard)"
            type="number"
          />
        </div>
        <CustomField
          name={name}
          required
          fieldName="number_of_species_observed"
          label="Number of species observed"
          tooltip="The number of species that was observed to be present"
          type="number"
        />
      </div>
    </>
  );
}
