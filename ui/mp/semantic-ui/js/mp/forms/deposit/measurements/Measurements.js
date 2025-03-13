import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import Sample from "./Sample";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";
import Duration from "@mbdb_deposit/sharedComponents/Duration";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";
import Temperature from "@mbdb_deposit/sharedComponents/Temperature";

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

      <div className="my-3">
        <Duration name={`${name}.duration`} colorSchema="light" />
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

      <Sample name={`${name}.sample`} colorSchema="light" />
    </>
  );
}
