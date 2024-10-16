import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import { getIn, useFormikContext } from "formik";
import SingleInjection from "./SingleInjection";
import Titration from "./Titration";
import UseDefault from "@mbdb_deposit/buildingBlocks/UseDefault";

function InjectionMode({ name, colorSchema }) {
  const { values } = useFormikContext();

  const fieldName = `${name}.type`;
  UseDefault(fieldName, "Single injection");

  const injectionOptions = [
    { value: "Single injection", label: "Single injection" },
    { value: "Titration", label: "Titration" },
  ];

  const actualValue = getIn(values, fieldName);

  return (
    <>
      <FormWrapper headline="Injection mode" colorSchema={colorSchema}>
        <div className="flex">
          <div className="mr-3">
            <OptionField
              name={fieldName}
              options={injectionOptions}
              label="type"
              required
              width="w-full"
              tooltip="The type of the injection"
            />
          </div>
          <div>
            {actualValue === "Single injection" && (
              <SingleInjection name={name} />
            )}
            {actualValue === "Titration" && <Titration name={name} />}
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default InjectionMode;
