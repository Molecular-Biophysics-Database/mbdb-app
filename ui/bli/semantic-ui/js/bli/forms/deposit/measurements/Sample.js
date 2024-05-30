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

function Sample( { name, colorSchema } ) {

    const { values } = useFormikContext();

    const platesValue = getIn(values, `metadata.method_specific_parameters.plates`);
    const platesOptions = CreateOptions(platesValue, 'Select Plate, if applicable');

    const chemicalEnvironmentsValue = getIn(values, `metadata.general_parameters.chemical_environments`);
    const chemicalEnvironmentsOptions = CreateOptions(chemicalEnvironmentsValue, 'Select Chemical environment, if applicable');

  return (
    <>
        <FormWrapper
            headline='Sample'
            colorSchema={colorSchema}
            tooltip='Sample the sensor was in contact with during the measurement'
        >
            <div className="flex">
                <div className="mr-3">
                    <OptionField
                        name={name}
                        label='Plate'
                        fieldName='plate'
                        required={true}
                        options={platesOptions}
                        tooltip='link to one of the plates'
                    />
                </div>
                <div className="mr-3">
                    <CustomField
                        name={name}
                        fieldName='well_position'
                        label='Well position'
                        required={true}
                        tooltip='The position the well (in the plate) where the sample was during the measurement'
                    />
                </div>
                <div>
                    <OptionField
                        name={name}
                        label='Chemical environment'
                        fieldName='chemical_environment'
                        options={chemicalEnvironmentsOptions}
                        required={true}
                        tooltip='Name (id) of the chemical environment of the sample (from the chemical environments defined in the general parameters'
                    />
                </div>
            </div>
            <div>
                <OptionalField
                    name={name}
                    label='Temperature'
                    fieldName='temperature'
                    tooltip='Temperature of the sample while being measured'
                    renderChild={({ optionalFieldName }) => (
                        <Temperature
                            name={optionalFieldName}
                            tooltip='Temperature of the sample while being measured'
                        />
                    )}
                />
            </div>
            <div>
                <ArrayField
                    name={name}
                    label='Analyte'
                    fieldName='analytes'
                    tooltip='List of names (ids) of entities (from the entities of interest defined in the general parameters) that was used to alter the behavior of the target(s) or entities present at varying concentrations for a series of measurements and their concentrations'
                    renderChild={({ arrayName, index }) => (
                        <FormWrapper
                            headline={`Analyte ${index + 1}`}
                            tooltip='List of names (ids) of entities (from the entities of interest defined in the general parameters) that was used to alter the behavior of the target(s) or entities present at varying concentrations for a series of measurements and their concentrations'
                        >
                            <EntityAndConcentration
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
            <div>
                <ArrayField
                    name={name}
                    label='Preparational protocol'
                    fieldName='preparational_protocol'
                    tooltip='List of steps taken to prepare the sample'
                    renderChild={({ arrayName, index }) => (
                        <FormWrapper
                            headline={`Preparational protocol ${index + 1}`}
                            tooltip='List of steps taken to prepare the sample'
                        >
                            <Protocol
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
        </FormWrapper>
    </>
  );
}

export default Sample;