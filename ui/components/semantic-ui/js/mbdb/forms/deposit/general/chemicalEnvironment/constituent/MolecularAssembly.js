import React from "react";
import CustomField from "../../../buildingBlocks/CustomField";
import ArrayField from "../../../buildingBlocks/ArrayField";
import MolecularWeight from "../../sharedComponents/MolecularWeight";
import Modification from "../../sharedComponents/modifications/Modification";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import Components from "../../sharedComponents/components/Components";
import Concentration from "../../../sharedComponents/Concentration";
import ExternalDatabase from "../../../buildingBlocks/ExternalDatabase";

function MolecularAssembly({ name }) {
  return (
    <>
      <div>
        <CustomField
          name={name}
          label="Name"
          fieldName="name"
          width="w-full"
          tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
        />
      </div>
      <div className="flex mb-3">
        <div className="mr-3">
          <ExternalDatabase name={name} />
        </div>
        <div>
          <ArrayField
            name={name}
            label="Additional specification"
            fieldName="additional_specifications"
            tooltip="Additional information about the complex substance can be specified here"
            renderChild={({ arrayName, index }) => (
              <CustomField
                name={`${arrayName}.${index}`}
                label={`Additional specification ${index + 1}`}
                width="w-[15rem]"
                tooltip="Additional information about the complex substance can be specified here"
              />
            )}
          />
        </div>
      </div>
      <div className="flex">
        <div className="mr-3">
          <MolecularWeight
            name={`${name}.molecular_weight`}
            tooltip="The molecular weight of the molecular assembly"
          />
        </div>
        <div className="mb-3">
          <Concentration
            name={`${name}.concentration`}
            tooltip="The molecular weight of the molecular assembly"
          />
        </div>
      </div>
      <div className="-mt-3">
        <ArrayField
          name={name}
          label="Chemical Modification"
          fieldName="chemical_modifications"
          tooltip="List describing deliberate modifications made to the molecular assembly through chemical, biochemical, or physical means"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Chemical modification ${index + 1}`}
              tooltip="List describing deliberate modifications made to the molecular assembly through chemical, biochemical, or physical means"
            >
              <Modification
                name={`${arrayName}.${index}`}
                colorSchema="light"
              />
            </FormWrapper>
          )}
        />
      </div>
      <div>
        <Components
          name={name}
          colorSchemaHeadline="light"
          colorSchemaProtocol="light"
          molecularWeightColorSchema="light"
          tooltip="Description of the individual components (e.g. polypeptide, heme, lipids, metal ions etc.) the molecular assembly is composed of (e.g. Hemoglobin alpha) and how many copies of each component were present"
        />
      </div>
    </>
  );
}

export default MolecularAssembly;
