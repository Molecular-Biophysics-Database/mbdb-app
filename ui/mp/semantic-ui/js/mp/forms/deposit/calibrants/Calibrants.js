import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import MolecularWeight from "@mbdb_deposit/general/sharedComponents/MolecularWeight";
import Modification from "@mbdb_deposit/general/sharedComponents/modifications/Modification";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import SizeCalibrants from "./SizeCalibrants";

export default function Calibrants({ name }) {
  const typeOptions = [
    { value: "polyribonucleotide", label: "polyribonucleotide" },
    { value: "polypeptide(D)", label: "polypeptide(D)" },
    { value: "polypeptide(L)", label: "polypeptide(L)" },
    { value: "chemical", label: "chemical" },
    { value: "molecular assembly", label: "molecular assembly" },
    { value: "virion", label: "virion" },
    { value: "nanoparticle", label: "nanoparticle" }
  ];

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            fieldName="name"
            label="Name"
            required
            tooltip="The name of the calibrant"
          />
        </div>
        <OptionField
          name={name}
          fieldName="type"
          label="Type"
          options={typeOptions}
          required
          tooltip="The type of the calibrant (e.g. polypeptide(L))"
        />
      </div>
      <div className="mb-3">
        <ArrayField
          name={name}
          label="Additional specification"
          fieldName="additional_specifications"
          tooltip="Additional information about the calibrant can be specified here"
          renderChild={({ arrayName, index }) => (
            <CustomField
              name={`${arrayName}.${index}`}
              label={`Additional specification ${index + 1}`}
              width="w-[15rem]"
              tooltip="Additional information about the calibrant can be specified here"
            />
          )}
        />
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          fieldName="molecular_weight"
          label="Molecular weight"
          tooltip="The molecular weight of the calibrant"
          renderChild={({optionalFieldName}) => (
            <MolecularWeight
              name={optionalFieldName}
              tooltip="The molecular weight of the calibrant"
              colorSchema="light"
            />
          )}
        />
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          fieldName="size"
          label="Size"
          tooltip="The size of the calibrant"
          renderChild={({ optionalFieldName }) => (
            <SizeCalibrants
                name={optionalFieldName}
                colorSchema="light"
                tooltip="The size of the calibrant"
              />
          )}
        />
      </div>
      <ArrayField
        name={name}
        label="Modification"
        fieldName="modifications"
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
