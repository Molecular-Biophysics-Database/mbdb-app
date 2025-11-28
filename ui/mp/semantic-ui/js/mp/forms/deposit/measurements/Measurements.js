import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import Sample from "./Sample";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";
import Duration from "@mbdb_deposit/sharedComponents/Duration";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import Temperature from "@mbdb_deposit/sharedComponents/Temperature";
import SampleDilution from "./SampleDilution";

export default function Measurements({ name }) {
  CreateUuid(name);

  const tooltips = {
    temperature: "The temperature the measurement was performed at",
  };

  return (
    <>
      <CustomField
        name={name}
        fieldName="name"
        label="Name"
        required
        tooltip="Name (id) of the measurement which must be unique within a record (i.e. triplicates must be named individually in the raw data file). The name must allow location of the measurement data within the raw data file as well as processed data files if these are present"
        width="w-full"
      />

      <div className="my-3 w-fit">
        <Duration name={`${name}.duration`} colorSchema="light" tooltip="Specify the duration of this measurement" />
      </div>

      <div className="mb-3">
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
      </div>

      <div className="mb-3">
        <Sample name={`${name}.sample`} colorSchema="light" />
      </div>

      <OptionalField
        name={name}
        fieldName="sample_dilution"
        label="Sample dilution"
        tooltip="Parameters describing how the sample was diluted within the measurement in flow mode"
        renderChild={({ optionalFieldName }) => (
          <SampleDilution name={optionalFieldName} colorSchema="light" />
        )}
      />
    </>
  );
}
