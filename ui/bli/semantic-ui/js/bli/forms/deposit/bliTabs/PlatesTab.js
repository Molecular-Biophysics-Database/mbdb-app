import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Plates from "../plates/Plates";

export default function PlatesTab({ name }) {
  const tooltip = "Information about the plates used for the measurements";

  const fieldName = "plates";

  UseDefault(`${name}.${fieldName}`, [{}]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about the plates where measurements were performed
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Plate"
        required
        fieldName={fieldName}
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => (
          <FormWrapper headline={`Plate ${index + 1}`} tooltip={tooltip}>
            <Plates name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
