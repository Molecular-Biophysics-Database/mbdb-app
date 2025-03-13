import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import Calibrants from "../calibrants/Calibrants";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

export default function CalibrantsTab({ name }) {
  const fieldName = "calibrants";

  const tooltip =
    "List of objects that was used to create the calibration curve for converting contrast to molecular weight";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the objects that were used for size calibration
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Calibrants"
        fieldName={fieldName}
        tooltip={tooltip}
        required
        renderChild={({ arrayName, index }) => (
          <FormWrapper headline={`Calibrant ${index + 1}`} tooltip={tooltip}>
            <Calibrants name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
