import React from "react";
import FormWrapper from "../../../../buildingBlocks/FormWrapper";
import { getIn, useFormikContext } from "formik";
import PurityYes from "./PurityYes";
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
        label="Purity"
        fieldName="purity"
        initialValue={{ assessed: "Yes" }}
        tooltip="Information about if and how the purity was assessed"
        renderChild={({ optionalFieldName }) => {
          const actualValue = getIn(values, optionalFieldName);
          if (!actualValue) {
            return null;
          }
          return (
            <FormWrapper
              headline="Purity"
              colorSchema={colorSchema}
              tooltip="Information about if and how the purity was assessed"
            >
              <div className="flex">
                <div className="mr-3">
                  <DynamicOptionField
                    name={optionalFieldName}
                    required
                    options={typeOptions}
                    label="Assessed"
                    tooltip="Wether or not the purity was checked"
                    fieldName="assessed"
                    width="w-full"
                  />
                </div>
                <div>
                  {actualValue.assessed === "Yes" && (
                    <PurityYes name={optionalFieldName} />
                  )}
                  {actualValue.assessed === "No" && <></>}
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
