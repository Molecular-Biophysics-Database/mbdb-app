import React from "react";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import Temperature from "@mbdb_deposit/sharedComponents/Temperature";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

function MethodSpecificParameters({ name }) {
  const tooltips = {
    temperature:
      "The temperature of the sample chamber while the measurement was performed",
  };

  const experimentTypeOptions = [
    { value: "Affinity", label: "Affinity" },
    { value: "Concentration", label: "Concentration" },
    { value: "Other", label: "Other" },
  ];

  const signalTypeOptions = [
    { value: "Initial intensity", label: "Initial intensity" },
    { value: "TRIC/MST", label: "TRIC/MST" },
    { value: "Spectral shift", label: "Spectral shift" },
  ];

  const excitationLedColorOptions = [
    {
      value: "RED (ex 605-645nm, em 660-720nm)",
      label: "RED (ex 605-645nm, em 660-720nm)",
    },
    {
      value: "RED (ex 610-645nm, em 680-720nm)",
      label: "RED (ex 610-645nm, em 680-720nm)",
    },
    {
      value: "GREEN (ex 555-585nm, em 605-690nm)",
      label: "GREEN (ex 555-585nm, em 605-690nm)",
    },
    {
      value: "GREEN (ex 515-550nm, em 565-600nm)",
      label: "GREEN (ex 515-550nm, em 565-600nm)",
    },
    {
      value: "BLUE (ex 480-500nm, em 515-550nm)",
      label: "BLUE (ex 480-500nm, em 515-550nm)",
    },
    {
      value: "BLUE (ex 460-500nm, em 515-560nm)",
      label: "BLUE (ex 460-500nm, em 515-560nm)",
    },
    {
      value: "UV (ex 260-300nm, em 330-380nm)",
      label: "UV (ex 260-300nm, em 330-380nm)",
    },
    { value: "Spectral shift", label: "Spectral shift" },
  ];

  return (
    <>
      <FormWrapper
        headline="Method specific parameters"
        tooltip="The parameters of the experiment that is specific to MST/TRIC/Spectral Shift"
      >
        <div className="flex mb-3">
          <OptionField
            name={name}
            options={experimentTypeOptions}
            label="Experiment type"
            fieldName="experiment_type"
            required
            tooltip="The type of physical parameter that was sought"
          />

          <div className="mx-3">
            <OptionField
              name={name}
              options={signalTypeOptions}
              label="Signal type"
              fieldName="signal_type"
              required
              tooltip="The type of signal that was being measured"
            />
          </div>

          <OptionField
            name={name}
            options={excitationLedColorOptions}
            label="Excitation LED color"
            fieldName="excitation_led_color"
            required
            tooltip="The color of the excitation LED used for the experiment. NOTE that colors are specific to the combination in which it occurs, e.g. the GREEN in a BLUE/GREEN instrument, is not the same as the GREEN in a GREEN/RED instrument"
          />
        </div>
        <div className="flex">
          <div className="mr-3">
            <CustomField
              name={name}
              label="Excitation LED power"
              type="number"
              fieldName="excitation_led_power"
              min={0}
              max={100}
              width="w-[13rem]"
              required
              tooltip="The power, in percentage, of the excitation LED used in experiment"
            />
          </div>

          <CustomField
            name={name}
            label="IR MST laser power"
            fieldName="ir_mst_laser_power"
            type="number"
            min={0}
            max={100}
            width="w-[13rem]"
            required
            tooltip="The power of the infrared LASER used in the experiment in percentages. Even though a change in nomenclature occurred in Nanotemper's control software, the underlying data is still stored in percentages. Use the following conversion; Low = 20, Medium = 40, High = 60"
          />
        </div>

        <OptionalField
          name={name}
          label="Temperature"
          fieldName="temperature"
          tooltip={tooltips.temperature}
          renderChild={({ optionalFieldName }) => (
            <Temperature
              name={optionalFieldName}
              colorSchema="light"
              tooltip={tooltips.temperature}
            />
          )}
        />
      </FormWrapper>
    </>
  );
}

export default MethodSpecificParameters;
