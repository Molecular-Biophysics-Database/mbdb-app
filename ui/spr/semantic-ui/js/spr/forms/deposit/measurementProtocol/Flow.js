import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import Path from "./Path";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

function Flow({ colorSchema, name }) {
  const tooltips = {
    path: "list of the flow-path, in terms of measurement positions. Measurement positions that are connected by a flow running serially through them should be mentioned within the inner list, while parallel flows should be mentioned in the outer list",
    direction: "Direction of the flow",
  };

  const unitOptions = [
    { value: "mL/min", label: "mL/min" },
    { value: "µl/s", label: "µl/s" },
  ];

  const directionOptions = [
    { value: "Vertical", label: "Vertical" },
    { value: "Horizontal", label: "Horizontal" },
  ];

  UseDefault(`${name}.path[0]`, [{}]);

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline="Flow"
        tooltip="Information about the liquid flow during the measurement step"
      >
        <div className="flex">
          <div className="-mt-3 mr-3">
            <ArrayField
              name={name}
              label="Path"
              fieldName="path"
              required
              tooltip={tooltips.path}
              renderChild={({ arrayName, index }) => (
                <FormWrapper
                  headline={`Path ${index + 1}`}
                  tooltip={tooltips.path}
                >
                  <Path name={`${arrayName}.${index}`} />
                </FormWrapper>
              )}
            />
          </div>
          <div className="mr-3">
            <CustomField
              name={name}
              fieldName="rate"
              label="Rate"
              required
              tooltip="Numerical value of the flow-rate"
              type="number"
            />
          </div>
          <div className="mr-3">
            <OptionField
              name={name}
              fieldName="unit"
              label="Unit"
              required
              tooltip="The unit of the flow-rate"
              options={unitOptions}
            />
          </div>
          <div className="-mt-3">
            <OptionalField
              name={name}
              label="Direction"
              fieldName="direction"
              tooltip={tooltips.direction}
              renderChild={({ optionalFieldName }) => (
                <OptionField
                  name={optionalFieldName}
                  label="Direction"
                  tooltip={tooltips.direction}
                  options={directionOptions}
                />
              )}
            />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default Flow;
