import React from "react";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import { useFormikContext, getIn } from "formik";
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

export default function Path({ name }) {
  const { values } = useFormikContext();

  const tooltips = {
    measurementPosition: "Name (id) of the measurement position",
  };

  const measurementPositionOptions = CreateOptions(
    getIn(values, "metadata.method_specific_parameters.measurement_positions"),
    "Select Measurement position, if applicable"
  );

  return (
    <>
      <div className="-mt-3">
        <ArrayField
          name={name}
          label="Measurement position"
          tooltip={tooltips.measurementPosition}
          renderChild={({ arrayName, index }) => (
            <OptionField
              name={`${arrayName}.${index}`}
              label={`Measurement position ${index + 1}`}
              width="w-[15rem]"
              options={measurementPositionOptions}
              tooltip={tooltips.measurementPosition}
            />
          )}
        />
      </div>
    </>
  );
}
