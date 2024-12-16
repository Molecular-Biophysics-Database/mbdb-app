import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";
import Plates from "../plates/Plates";

function PlatesTab({ name }) {
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
        tooltip="Information about the plates used for the measurements"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Plate ${index + 1}`}
            tooltip="Information about the plates used for the measurements"
          >
            <Plates name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default PlatesTab;
