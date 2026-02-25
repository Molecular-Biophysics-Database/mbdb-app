import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import Calibrants from "../calibrants/Calibrants";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

export default function CalibrantsTab({ name }) {
  const fieldName = "calibrants";

  const tooltip =
    "List of objects that was used to create the calibration curve for converting contrast to molecular weight or converting the position of optimum contrast to particle size";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the objects that were used for molecular weight or size calibration
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Calibrants"
        fieldName={fieldName}
        tooltip={tooltip}
        required
        renderChild={({ arrayName, index }) => (
          <FormWrapper headline={`Calibrant ${index + 1}`} tooltip={tooltip} name={arrayName}>
            <Calibrants name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
