import React from "react";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import { useFormikContext, getIn } from "formik";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

function Path( { name } ) {

    const { values } = useFormikContext();

    const measurementPositionValue = getIn(values, 'metadata.method_specific_parameters.measurement_positions');
    const measurementPositionOptions = CreateOptions(measurementPositionValue, 'Select Measurement position, if applicable');

  return (
    <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label='Measurement position'
                tooltip='Name (id) of the measurement position'
                renderChild={({ arrayName, index }) => (
                    <OptionField
                        name={`${arrayName}.${index}.name`}
                        label={`Measurement position`}
                        options={measurementPositionOptions}
                        tooltip='Name (id) of the measurement position'
                    />
                )}
            />
        </div>
    </>
  );
}

export default Path;