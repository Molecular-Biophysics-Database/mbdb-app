import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import { getIn, useFormikContext } from "formik";
import CustomField from "../buildingBlocks/CustomField";
import OptionField from "../buildingBlocks/OptionField";
import ArrayField from "../buildingBlocks/ArrayField";
import Protocol from "./Protocol";
import CreateOptions from "../buildingBlocks/CreateOptions";

function LigandInformation({ name, colorSchema }) {
  const { values } = useFormikContext();

  const ligandValue = getIn(
    values,
    `metadata.general_parameters.entities_of_interest`
  );
  const ligandOptions = CreateOptions(
    ligandValue,
    "Select Ligand, if applicable"
  );

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Ligand"
        tooltip="Information about the ligand and how it was immobilized"
      >
        <div className="flex">
          <div className="mr-3">
            <OptionField
              name={name}
              options={ligandOptions}
              label="Entity"
              fieldName="entity"
              tooltip="Name (id) of the ligand (entity that is immobilized, from the list of entities of interest defined in the general parameters"
            />
          </div>
          <div>
            <CustomField
              name={name}
              fieldName="immobilization_chemistry"
              label="Immobilization chemistry"
              tooltip="The type of chemistry on ligands and surface that allows for immobilization of the ligands on the surface of the sensor"
              width="w-[16.5rem]"
            />
          </div>
        </div>
        <div>
          <ArrayField
            name={name}
            label="Immobilization protocol"
            fieldName="immobilization_protocol"
            tooltip="List of steps for immobilizing the ligand on the surface of the sensor"
            renderChild={({ arrayName, index }) => (
              <FormWrapper
                headline={`Ligand immobilization protocol ${index + 1}`}
                tooltip="List of steps for immobilizing the ligand on the surface of the sensor"
              >
                <Protocol name={`${arrayName}.${index}`} />
              </FormWrapper>
            )}
          />
        </div>
      </FormWrapper>
    </>
  );
}

export default LigandInformation;
