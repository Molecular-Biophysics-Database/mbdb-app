import React from "react";
import ValueUnit from "../../buildingBlocks/ValueUnit";
import ValueError from "../../buildingBlocks/ValueError";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";
import UseDefault from "../../buildingBlocks/UseDefault";
import ArrayField from "../../buildingBlocks/ArrayField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import EntityInvolved from "./EntityInvolved";
import CustomField from "../../buildingBlocks/CustomField";

function CorrectionOfActiveConcentration({ name }) {
  CreateUuid(name);

  const unitOptions = [{ value: "unitless", label: "unitless" }];

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
        <div>
          <ValueUnit
            options={unitOptions}
            name={name}
            valueRequired
            unitRequired
            tooltipValue="The correction of the deviations between nominal and true active concentration of the entity"
            tooltipUnit="The correction of active concentration is unitless"
          />
        </div>
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
        tooltip="List of chemical or molecular assemblies the result describes and how many copies of each are involved"
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            colorSchema="light"
            headline={`Entity involved ${index + 1}`}
            tooltip="List of chemical or molecular assemblies the result describes and how many copies of each are involved"
          >
            <EntityInvolved name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default CorrectionOfActiveConcentration;
