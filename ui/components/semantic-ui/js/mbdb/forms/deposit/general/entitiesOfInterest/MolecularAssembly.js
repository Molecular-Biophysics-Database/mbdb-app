import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import ArrayField from "../../buildingBlocks/ArrayField";
import MolecularWeight from "../sharedComponents/MolecularWeight";
import Modification from "../sharedComponents/modifications/Modification";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Components from "../sharedComponents/components/Components";
import CreateUuid from "../../buildingBlocks/CreateUuid";
import ExternalDatabase from "../../buildingBlocks/ExternalDatabase";

function MolecularAssembly({ name }) {
  CreateUuid(name);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          label="Name"
          fieldName="name"
          required
          width="w-full"
          tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
        />
      </div>
      <div className="flex -mt-3 mb-3">
        <div className="mr-3">
          <ExternalDatabase colorSchema="light" name={name} />
        </div>
        <div>
          <ArrayField
            name={name}
            label="Additional specification"
            fieldName="additional_specifications"
            tooltip="Additional information about the moleculer assembly can be specified here"
            renderChild={({ arrayName, index }) => (
              <CustomField
                name={`${arrayName}.${index}`}
                label={`Additional specification ${index + 1}`}
                width="w-[15rem]"
                tooltip="Additional information about the molecular assembly can be specified here"
              />
            )}
          />
        </div>
      </div>
      <div className="mb-3">
        <MolecularWeight
          name={`${name}.molecular_weight`}
          colorSchema="light"
          tooltip="The molecular weight of the molecular assembly"
        />
      </div>
      <div>
        <ArrayField
          name={name}
          label="Chemical Modification"
          fieldName="chemical_modifications"
          tooltip="List describing deliberate modifications made to the molecular assembly through chemical, biochemical, or physical means"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              colorSchema="light"
              tooltip="List describing deliberate modifications made to the molecular assembly through chemical, biochemical, or physical means"
              headline={`Chemical modification ${index + 1}`}
            >
              <Modification name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </div>
      <div>
        <Components
          name={name}
          colorSchema="light"
          tooltip="Description of the individual components (e.g. polypeptide, heme, lipids, metal ions etc.) the molecular assembly is composed of (e.g. Hemoglobin alpha) and how many copies of each component were present"
        />
      </div>
    </>
  );
}

export default MolecularAssembly;
