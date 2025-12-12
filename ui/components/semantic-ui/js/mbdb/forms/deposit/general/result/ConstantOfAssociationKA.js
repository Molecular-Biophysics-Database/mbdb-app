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

function ConstantOfAssociationKA({ name }) {
  CreateUuid(name);

  const tooltips = {
    entityInvolved:
      "List of chemical or molecular assemblies the result describes and how many copies of each are involved",
  };

  const unitOptions = [
    { value: "M^-1", label: "M^-1" },
    { value: "M^-2", label: "M^-2" },
    { value: "mM^-1", label: "mM^-1" },
    { value: "mM^-2", label: "mM^-2" },
    { value: "µM^-1", label: "µM^-1" },
    { value: "µM^-2", label: "µM^-2" },
    { value: "nM^-1", label: "nM^-1" },
    { value: "nM^-2", label: "nM^-2" },
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
          tooltipUnit="Unit of the constant of association"
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
            name={arrayName}
          >
            <EntityInvolved name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default ConstantOfAssociationKA;
