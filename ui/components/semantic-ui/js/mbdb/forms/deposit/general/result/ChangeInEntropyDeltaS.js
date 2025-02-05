import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import ValueUnit from "../../buildingBlocks/ValueUnit";
import ValueError from "../../buildingBlocks/ValueError";
import ArrayField from "../../buildingBlocks/ArrayField";
import EntityInvolved from "./EntityInvolved";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import UseDefault from "../../buildingBlocks/UseDefault";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";

function ChangeInEntropyDeltaS({ name }) {
  CreateUuid(name);

  const tooltips = {
    entityInvolved:
      "List of chemical or molecular assemblies the result describes and how many copies of each are involved",
  };

  const unitOptions = [
    { value: "kcal/molK", label: "kcal/molK" },
    { value: "kJ/molK", label: "kJ/molK" },
  ];

  const fieldNameEntityInvolved = "entities_involved";
  UseDefault(`${name}.${fieldNameEntityInvolved}`, [{}]);

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            required
            fieldName="name"
            label="Name"
            tooltip="Descriptive name (id) of the result (e.g. Kd of Lysozyme and VHH2). Must be unique within a record"
          />
        </div>

        <ValueUnit
          options={unitOptions}
          name={name}
          valueRequired
          unitRequired
          tooltipValue="Numerical value of the result"
          tooltipUnit="Unit of the change in entropy"
        />
      </div>

      <OptionalField
        name={name}
        label="Value error"
        fieldName="value_error"
        tooltip="The expected error of the result in terms of a 95 % confidence interval"
        renderChild={({ optionalFieldName }) => (
          <ValueError name={optionalFieldName} colorSchema="light" />
        )}
      />

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
          >
            <EntityInvolved name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default ChangeInEntropyDeltaS;
