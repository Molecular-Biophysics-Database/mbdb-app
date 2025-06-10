import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import MolecularWeight from "@mbdb_deposit/general/sharedComponents/MolecularWeight";
import Modification from "@mbdb_deposit/general/sharedComponents/modifications/Modification";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

export default function Calibrants({ name }) {
  const typeOptions = [
    { value: "polypeptide(D)", label: "polypeptide(D)" },
    { value: "polyribonucleotide", label: "polyribonucleotide" },
    { value: "chemical", label: "chemical" },
    { value: "molecular assembly", label: "molecular assembly" },
    { value: "virion", label: "virion" },
  ];

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            fieldName="name"
            label="Name"
            tooltip="The name of the calibrant"
          />
        </div>
        <OptionField
          name={name}
          fieldName="type"
          label="Type"
          options={typeOptions}
        />
      </div>
      <div className="mb-3">
        <MolecularWeight
          name={`${name}.molecular_weight`}
          tooltip="The molecular weight of the calibrant"
          colorSchema="light"
        />
      </div>
      <ArrayField
        name={`${name}.modifications`}
        label="Modification"
        fieldName="modification"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Modification ${index + 1}`}
            colorSchema="light"
            tooltip="If the calibrant had a modification, such as post-translational modification, chemical modification, or surface modification, it can be described here"
          >
            <Modification name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
