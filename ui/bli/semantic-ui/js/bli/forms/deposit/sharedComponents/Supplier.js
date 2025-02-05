import React from "react";
import ArrayField from "@mbdb_deposit/buildingBlocks/ArrayField";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

function Supplier({ name, colorSchema, tooltip }) {
  const tooltips = {
    catalogNumber: "The catalog number or identifier of the item",
    furtherInformation: "Further information e.g. batch number",
  };

  return (
    <>
      <FormWrapper
        headline="Supplier"
        colorSchema={colorSchema}
        tooltip={tooltip}
      >
        <div className="flex">
          <div className="mr-3">
            <CustomField
              name={name}
              label="Name"
              fieldName="name"
              required
              tooltip="Name of the supplier"
            />
          </div>
          <div className="-mt-3 mr-3">
            <OptionalField
              name={name}
              label="Catalog number"
              fieldName="catalog_number"
              tooltip={tooltips.catalogNumber}
              renderChild={({ optionalFieldName }) => (
                <CustomField
                  name={optionalFieldName}
                  label="Catalog number"
                  tooltip={tooltips.catalogNumber}
                />
              )}
            />
          </div>
          <div className="-mt-3">
            <ArrayField
              name={name}
              label="Further information"
              fieldName="further_information"
              tooltip={tooltips.furtherInformation}
              renderChild={({ arrayName, index }) => (
                <CustomField
                  name={`${arrayName}.${index}`}
                  label={`Further information ${index + 1}`}
                  tooltip={tooltips.furtherInformation}
                />
              )}
            />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default Supplier;
