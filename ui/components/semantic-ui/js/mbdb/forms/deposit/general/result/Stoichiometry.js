import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import ArrayField from "../../buildingBlocks/ArrayField";
import EntityInvolved from "./EntityInvolved";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import UseDefault from "../../buildingBlocks/UseDefault";
import CreateUuid from "../../buildingBlocks/CreateUuid";

export default function Stoichiometry({ name }) {
  CreateUuid(name);

  const tooltips = {
    entityInvolved:
      "List of chemical or molecular assemblies the result describes and how many copies of each are involved",
  };

  const fieldNameEntityInvolved = "entities_involved";
  UseDefault(`${name}.${fieldNameEntityInvolved}`, [{}]);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          required
          fieldName="name"
          label="Name"
          width="w-full"
          tooltip="Descriptive name (id) of the result (e.g. Kd of Lysozyme and VHH2). Must be unique within a record"
        />
      </div>

      <div className="mr-4">
        <ArrayField
          name={name}
          label="Entity involved"
          fieldName={fieldNameEntityInvolved}
          required
          tooltip={tooltips.entityInvolved}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              colorSchema="light"
              headline={`Entity involved ${index + 1}`}
              tooltip={tooltips.entityInvolved}
              name={arrayName}
            >
              <EntityInvolved name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}
