import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import OptionField from "../../buildingBlocks/OptionField";
import OptionalField from "../../buildingBlocks/OptionalField";

function Size({ name, colorSchema }) {
  const tooltips = {
    median: "The median of the size",
    upper: "The upper bound of the size",
    lower: "The lower bound of the size",
  };

  const typeOptions = [
    { value: "radius", label: "radius" },
    { value: "diameter", label: "diameter" },
    { value: "path length", label: "path length" },
  ];

  const unitOptions = [
    { value: "Å", label: "Å" },
    { value: "nm", label: "nm" },
    { value: "μm", label: "μm" },
    { value: "mm", label: "mm" },
    { value: "cm", label: "cm" },
    { value: "m", label: "m" },
  ];

  return (
    <>
      <FormWrapper
        headline="Size"
        tooltip="The size of the lipid assembly"
        colorSchema={colorSchema}
      >
        <div className="flex mb-3">
          <div className="mr-3">
            <OptionField
              name={name}
              options={typeOptions}
              fieldName="type"
              label="Type"
              tooltip="The type of size (e.g. radius)"
            />
          </div>
          <div className="mr-3">
            <CustomField
              name={name}
              fieldName="mean"
              label="Mean"
              type="number"
              tooltip="The mean of the size"
            />
          </div>

          <OptionField
            name={name}
            options={unitOptions}
            fieldName="unit"
            label="Unit"
            tooltip="The unit of the size"
          />
        </div>
        <div className="flex -mt-3">
          <div className="mr-3">
            <OptionalField
              name={name}
              label="Median"
              fieldName="median"
              tooltip={tooltips.median}
              renderChild={({ optionalFieldName }) => (
                <CustomField
                  name={optionalFieldName}
                  label="Median"
                  type="number"
                  tooltip={tooltips.median}
                />
              )}
            />
          </div>
          <div className="mr-3">
            <OptionalField
              name={name}
              label="Upper"
              fieldName="upper"
              tooltip={tooltips.upper}
              renderChild={({ optionalFieldName }) => (
                <CustomField
                  name={optionalFieldName}
                  label="Upper"
                  type="number"
                  tooltip={tooltips.upper}
                />
              )}
            />
          </div>

          <OptionalField
            name={name}
            label="Lower"
            fieldName="lower"
            tooltip={tooltips.lower}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Lower"
                type="number"
                tooltip={tooltips.lower}
              />
            )}
          />
        </div>
      </FormWrapper>
    </>
  );
}

export default Size;
