import React from "react";
import { getIn, useFormikContext } from "formik";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Sample from "./Sample";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

function Measurements( { name } ) {

    const { values } = useFormikContext();

    UseDefault(`${name}.sample`, [{}]);

    const measurementPotionValue = getIn(values, `metadata.method_specific_parameters.measurement_positions`);
    const measurementPotionOptions = CreateOptions(measurementPotionValue, 'Select Measurement position, if applicable');

  return (
    <>
        <div className="mb-3">
            <CustomField
                name={name}
                fieldName='name'
                label='Name'
                required={true}
                tooltip='Name (id) of the measurement which must be unique within a record (i.e. triplicates must be named individually in the raw data file). The name must allow location of the measurement data within the raw data file as well as processed data files if these are present'
                width='w-full'
            />
        </div>
        <div className="flex mb-3">
            <div className="mr-3">
                <OptionField
                    name={name}
                    label='Measurement position'
                    fieldName='measurement_position'
                    required={true}
                    options={measurementPotionOptions}
                />
            </div>
            <div className="-mt-3">
                <OptionalField
                    name={name}
                    fieldName='reference_measurement_position'
                    label='Reference measurement positon'
                    renderChild={({ optionalFieldName }) => (
                        <OptionField
                            name={optionalFieldName}
                            label='Reference measurement position'
                            options={measurementPotionOptions}
                        />
                    )}
                />
            </div>
        </div>
        <div>
            <ArrayField
                name={name}
                fieldName='sample'
                label='Sample'
                required={true}
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Sample ${index + 1}`}
                        colorSchema='light'
                    >
                        <Sample
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
        <div>
            <ArrayField
                name={name}
                fieldName='reference_sample'
                label='Reference sample'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        headline={`Reference sample ${index + 1}`}
                        colorSchema='light'
                    >
                        <Sample
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default Measurements;