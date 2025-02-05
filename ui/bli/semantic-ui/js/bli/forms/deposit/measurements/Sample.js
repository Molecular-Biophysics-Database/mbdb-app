import React from "react";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import Protocol from "@mbdb_deposit/sharedComponents/Protocol";
import { useFormikContext } from "formik";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import { getIn } from "formik";
import Temperature from "@mbdb_deposit/sharedComponents/Temperature";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";
import EntityAndConcentration from "@mbdb_deposit/sharedComponents/EntityAndConcentration";

function Sample({ name, colorSchema }) {
  const tooltips = {
    temperature: "Temperature of the sample while being measured",
    analyte:
      "List of names (ids) of entities (from the entities of interest defined in the general parameters) that was used to alter the behavior of the target(s) or entities present at varying concentrations for a series of measurements and their concentrations",
    preparation_protocol: "List of steps taken to prepare the sample",
  };

  const { values } = useFormikContext();

  const platesOptions = CreateOptions(
    getIn(values, "metadata.method_specific_parameters.plates"),
    "Select Plate, if applicable"
  );

  const chemicalEnvironmentsOptions = CreateOptions(
    getIn(values, "metadata.general_parameters.chemical_environments"),
    "Select Chemical environment, if applicable"
  );

  return (
    <>
      <FormWrapper
        headline="Sample"
        colorSchema={colorSchema}
        tooltip="Sample the sensor was in contact with during the measurement"
      >
        <div className="flex">
          <div className="mr-3">
            <OptionField
              name={name}
              label="Plate"
              fieldName="plate"
              required
              options={platesOptions}
              tooltip="link to one of the plates"
            />
          </div>
          <div className="mr-3">
            <CustomField
              name={name}
              fieldName="well_position"
              label="Well position"
              required
              tooltip="The position the well (in the plate) where the sample was during the measurement"
            />
          </div>
          <OptionField
            name={name}
            label="Chemical environment"
            fieldName="chemical_environment"
            options={chemicalEnvironmentsOptions}
            required
            tooltip="Name (id) of the chemical environment of the sample (from the chemical environments defined in the general parameters"
          />
        </div>

        <OptionalField
          name={name}
          label="Temperature"
          fieldName="temperature"
          tooltip={tooltips.temperature}
          renderChild={({ optionalFieldName }) => (
            <Temperature
              name={optionalFieldName}
              tooltip={tooltips.temperature}
            />
          )}
        />

        <ArrayField
          name={name}
          label="Analyte"
          fieldName="analytes"
          tooltip={tooltips.analyte}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Analyte ${index + 1}`}
              tooltip={tooltips.analyte}
            >
              <EntityAndConcentration name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />

        <ArrayField
          name={name}
          label="Preparation protocol"
          fieldName="preparation_protocol"
          tooltip={tooltips.preparation_protocol}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              headline={`Preparation protocol step ${index + 1}`}
              tooltip={tooltips.preparation_protocol}
            >
              <Protocol name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </FormWrapper>
    </>
  );
}

export default Sample;
