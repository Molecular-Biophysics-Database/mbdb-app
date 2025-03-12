import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import CellTemperature from "./methodSpecificParameters/CellTemperature";
import CellVolume from "./methodSpecificParameters/CellVolume";
import InjectionMode from "./methodSpecificParameters/injectionMode/InjectionMode";
import ReferencePower from "./methodSpecificParameters/ReferencePower";
import StirringSpeed from "./methodSpecificParameters/StirringSpeed";

function MethodSpecificParameters({ name }) {
  const tooltips = {
    methodSpecific: "The parameters of the experiment that are specific to MP",
    feedbackMode:
      "The operating mode where conditions are adjusted automatically to maintain constant temperature during heat measurements",
  };

  const feedbackModeOptions = [
    { value: "None", label: "None" },
    { value: "Low", label: "Low" },
    { value: "High", label: "High" },
  ];

  return (
    <>
      <FormWrapper
        headline="Method specific parameters"
        tooltip={tooltips.methodSpecific}
      >
        <div className="mb-3">
          <OptionField
            name={name}
            fieldName="feedback_mode"
            label="Feedback mode"
            required
            options={feedbackModeOptions}
            tooltip={tooltips.feedbackMode}
          />
        </div>
        <div className="flex mb-3">
          <InjectionMode name={`${name}.injection_mode`} colorSchema="light" />
        </div>
        <div className="flex gap-x-3 mb-3">
          <CellTemperature
            name={`${name}.cell_temperature`}
            colorSchema="light"
          />
          <CellVolume name={`${name}.cell_volume`} colorSchema="light" />
        </div>
        <div className="flex gap-x-3">
          <ReferencePower
            name={`${name}.reference_power`}
            colorSchema="light"
          />

          <StirringSpeed name={`${name}.stirring_speed`} colorSchema="light" />
        </div>
      </FormWrapper>
    </>
  );
}

export default MethodSpecificParameters;
