import React from "react";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import Ligand from "./Ligand";
import Target from "./Target";
import Protocol from "@mbdb_deposit/sharedComponents/Protocol";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import { getIn, useFormikContext } from "formik";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

function Sample({ name, tooltip, colorSchema }) {
  const { values } = useFormikContext();

  const tooltips = {
    preparationProtocol:
      "List of the steps performed during the preparation of the complex substance",
    target:
      "List of names (ids), from the entities of interest defined in the general parameters, of directly measured entities",
    ligand:
      "List of names (ids) of entities (from the entities of interest defined in the general parameters) that were used to alter the behavior of the target(s)",
  };

  const measurementContainerOptions = [
    {
      value: "Monolith Standard Capillary",
      label: "Monolith Standard Capillary",
    },
    {
      value: "Monolith Premium Capillary",
      label: "Monolith Premium Capillary",
    },
    {
      value: "Monolith LabelFree Capillary",
      label: "Monolith LabelFree Capillary",
    },
    {
      value: "Monolith LabelFree Premium Capillary",
      label: "Monolith LabelFree Premium Capillary",
    },
    {
      value: "Monolith NT.Automated Capillary Chip",
      label: "Monolith NT.Automated Capillary Chip",
    },
    {
      value: "Monolith NT.Automated Premium Capillary Chip",
      label: "Monolith NT.Automated Premium Capillary Chip",
    },
    {
      value: "Monolith NT.Automated LabelFree Capillary Chip",
      label: "Monolith NT.Automated LabelFree Capillary Chip",
    },
    {
      value: "Monolith NT.Automated LabelFree Premium Capillary Chip",
      label: "Monolith NT.Automated LabelFree Premium Capillary Chip",
    },
    { value: "384-well plate", label: "384-well plate" },
    { value: "Other", label: "Other" },
  ];

  const chemicalEnvironmentOptions = CreateOptions(
    getIn(values, "metadata.general_parameters.chemical_environments"),
    "Select Chemical Environment, if applicable"
  );

  const fieldNameTarget = "targets";
  UseDefault(`${name}.${fieldNameTarget}`, [{}]);

  const fieldNameLigand = "ligands";
  UseDefault(`${name}.${fieldNameLigand}`, [{}]);

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Sample"
        tooltip={tooltip}
      >
        <div className="flex mb-3">
          <div className="mr-3">
            <OptionField
              name={name}
              fieldName="chemical_environment"
              label="Chemical environment"
              options={chemicalEnvironmentOptions}
              required
              tooltip="Name (id) of the chemical environment of the sample (from the chemical environments defined in the general parameters"
              width="w-[14rem]"
            />
          </div>

          <OptionField
            name={name}
            fieldName="measurement_container"
            options={measurementContainerOptions}
            label="Measurement container"
            required
            tooltip="The container the sample was in during the measurement"
            width="w-[14rem]"
          />
        </div>

        <ArrayField
          name={name}
          label="Preparation protocol"
          fieldName="preparation_protocol"
          tooltip={tooltips.preparationProtocol}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Preparation protocol step ${index + 1}`}
              tooltip={tooltips.preparationProtocol}
            >
              <Protocol name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />

        <ArrayField
          name={name}
          label="Target"
          fieldName={fieldNameTarget}
          required
          tooltip={tooltips.target}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Target ${index + 1}`}
              tooltip={tooltips.target}
            >
              <Target name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />

        <ArrayField
          name={name}
          label="Ligand"
          fieldName={fieldNameLigand}
          required
          tooltip={tooltips.ligand}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Ligand ${index + 1}`}
              tooltip={tooltips.ligand}
            >
              <Ligand name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </FormWrapper>
    </>
  );
}

export default Sample;
