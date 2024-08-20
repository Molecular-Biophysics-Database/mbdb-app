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

function HillCoefficient({ name }) {
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
            valueRequired={true}
            unitRequired={true}
            tooltipValue="Numerical value of the result"
            tooltipUnit="Hill coefficient is unitless"
          />
        </div>
      </div>
      <div>
        <OptionalField
          name={name}
          label="Value error"
          fieldName="value_error"
          tooltip="The expected error of the result in terms of a 95 % confidence interval"
          renderChild={({ optionalFieldName }) => (
            <div>
              <ValueError name={optionalFieldName} colorSchema="light" />
            </div>
          )}
        />
      </div>
      <div>
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
      </div>
    </>
  );
}

export default HillCoefficient;
