import React from "react";
import FormWrapper from "../../../../buildingBlocks/FormWrapper";
import { getIn, useFormikContext } from "formik";
import HomogeneityYes from "./HomogeneityYes";
import OptionalField from "../../../../buildingBlocks/OptionalField";
import DynamicOptionField from "../../../../buildingBlocks/DynamicOptionField";

function Purity({ name, colorSchema }) {
  const { values } = useFormikContext();

  const typeOptions = [
    { value: "Yes", label: "Yes" },
    { value: "No", label: "No" },
  ];

  return (
    <>
      <OptionalField
        name={name}
        label="Homogeneity"
        fieldName="homogeneity"
        tooltip="Information about if, and how homogeneity was checked"
        initialValue={{ checked: "Yes" }}
        renderChild={({ optionalFieldName }) => {
          const actualValue = getIn(values, optionalFieldName);
          if (!actualValue) {
            return null;
          }
          return (
            <FormWrapper
              headline="Homogeneity"
              colorSchema={colorSchema}
              tooltip="Information about if, and how homogeneity was checked"
            >
              <div className="flex">
                <div className="mr-3">
                  <DynamicOptionField
                    required
                    name={optionalFieldName}
                    options={typeOptions}
                    label="Checked"
                    fieldName="checked"
                    width="w-full"
                  />
                </div>
                <div>
                  {actualValue.checked === "Yes" && (
                    <HomogeneityYes name={optionalFieldName} />
                  )}
                  {actualValue.checked === "No" && <></>}
                </div>
              </div>
            </FormWrapper>
          );
        }}
      />
    </>
  );
}

export default Purity;
