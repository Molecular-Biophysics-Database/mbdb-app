import React from "react";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import { useFormikContext, getIn } from "formik";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

function Path( { colorSchema, name } ) {

    const { values } = useFormikContext();

    const measurementPositionValue = getIn(values, 'metadata.method_specific_parameters.measurement_positions');
    const measurementPositionOptions = CreateOptions(measurementPositionValue, 'Select Measurement position, if applicable');

    const fieldName = `measurement_position`

    UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
        <FormWrapper
            colorSchema={colorSchema}
            headline='Path'
            tooltip='list of the flow-path, in terms of measurement positions. Measurement positions that are connected by a flow running serially through them should be mentioned within the inner list, while parallel flows should be mentioned in the outer list'>
                <div className="-mt-3">
                    <ArrayField
                        name={name}
                        label='Measurement position'
                        fieldName={fieldName}
                        required={true}
                        tooltip='Name (id) of the measurement position'
                        renderChild={({ arrayName, index }) => (
                            <OptionField
                                name={`${arrayName}.${index}`}
                                label={`Measurement position ${index + 1}`}
                                options={measurementPositionOptions}
                                tooltip='Name (id) of the measurement position'
                            />
                        )}
                    />
                </div>
        </FormWrapper>
    </>
  );
}

export default Path;