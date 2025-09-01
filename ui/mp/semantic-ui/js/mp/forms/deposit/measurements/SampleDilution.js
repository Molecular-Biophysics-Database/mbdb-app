import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import { getIn, useFormikContext } from "formik";

export default function SampleDilution({ name, colorSchema }) {
    const { values } = useFormikContext();

    const chemicalEnvironmentsValue = getIn(
        values,
        `metadata.general_parameters.chemical_environments`
    );
    const chemicalEnvironmentsOptions = CreateOptions(
        chemicalEnvironmentsValue,
        "Select Chemical environment, if applicable"
    );
    
    return(
        <>
            <FormWrapper
                headline="Sample dilution"
                colorSchema={colorSchema}
                tooltip="Parameters describing how the sample was diluted within the measurement in flow mode"
            >
                <div className="flex">
                    <div className="mr-3">
                        <OptionField
                            name={name}
                            fieldName="dilution_buffer.chemical_environment"
                            label="Dilution buffer"
                            required
                            options={chemicalEnvironmentsOptions}
                            tooltip="Name (id) of the chemical environment that was used as the dilution buffer (from the chemical environments defined in the record)"
                        />
                    </div>
                    <CustomField
                        name={name}
                        fieldName="dilution_factor"
                        label="Dilution factor"
                        type="number"
                        required
                        min={1}
                        tooltip="F-fold dilution; F = Q_buffer / Q_sample, where Q_buffer is buffer flowrate, Q_sample is sample flowrate. For low dilution factors, use more  precise formula (Q_buffer + Q_sample) / (Q_sample)"
                    />
                </div>
            </FormWrapper>
        
        </>
    )
}