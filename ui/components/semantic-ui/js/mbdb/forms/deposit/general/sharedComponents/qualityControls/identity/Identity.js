import React from "react";
import { getIn, useFormikContext } from "formik";
import FormWrapper from "../../../../buildingBlocks/FormWrapper";
import OptionalField from "../../../../buildingBlocks/OptionalField";
import DynamicOptionField from "../../../../buildingBlocks/DynamicOptionField";
import IdentityYes from "./IdentityYes";

function Identity({ name, colorSchema }) {
  const { values } = useFormikContext();

  const typeOptions = [
    { value: "Yes", label: "Yes" },
    { value: "No", label: "No" },
  ];

  return (
    <>
      <OptionalField
        name={name}
        label="Identity"
        fieldName="identity"
        initialValue={{ assessed: "Yes" }}
        tooltip="Information about if and how the identity was obtained"
        renderChild={({ optionalFieldName }) => {
          const actualValue = getIn(values, optionalFieldName);
          if (!actualValue) {
            return null;
          }
          return (
            <FormWrapper
              headline="Identity"
              colorSchema={colorSchema}
              tooltip="Information about if and how the identity was obtained"
            >
              <div className="mr-3">
                <DynamicOptionField
                  name={optionalFieldName}
                  required
                  options={typeOptions}
                  label="Assessed"
                  fieldName="assessed"
                  width="w-full"
                />
              </div>
              <div>
                {actualValue.assessed === "Yes" && (
                  <IdentityYes
                    name={optionalFieldName}
                    colorSchema={colorSchema === "light" ? "" : "light"}
                  />
                )}
                {actualValue.assessed === "No" && <></>}
              </div>
            </FormWrapper>
          );
        }}
      />
    </>
  );
}

export default Identity;
