import React from "react";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import { getIn, useFormikContext } from "formik";
import Flow from "../mode/flow/Flow";
import Static from "../mode/Static";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import { useEffect } from "react";

export default function ModeTab({ name }) {
  const { values, setFieldValue } = useFormikContext();

  const tooltip = `Whether the measurement was done on a flowing sample ("Flow") or statically placed sample("Static")`;
  
  const modeTabOptions = [
    { value: "Static", label: "Static" },
    { value: "Flow", label: "Flow" },
  ];

  const actualValue = getIn(values, name);

  useEffect(() => {
    if (actualValue?.type === "Flow") {
      setFieldValue(`${name}.sample_carrier`, undefined, false);
    } else if (actualValue?.type === "Static") {
      setFieldValue(`${name}.flow_cell`, undefined, false);
      setFieldValue(`${name}.sample_flowrate`, undefined, false);
      setFieldValue(`${name}.buffer_flowrate`, undefined, false);
    }
  }, [actualValue?.type, name, setFieldValue]);

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          Information about how the data was recorded using a static or flowing
          sample
        </FormWrapper>
      </div>
      <FormWrapper headline="Mode" tooltip={tooltip}>
        <div className="mb-3">
          <OptionField
            name={name}
            options={modeTabOptions}
            label="Mode"
            required
            fieldName="type"
            width="w-full"
            tooltip={tooltip}
            initialValue="Static"
          />
        </div>

        {actualValue?.type === "Flow" && <Flow key="flow-mode" name={name} />}
        {actualValue?.type === "Static" && (
          <Static
            key="static-mode"
            name={`${name}.sample_carrier`}
            colorSchema="light"
          />
        )}
      </FormWrapper>
    </>
  );
}
