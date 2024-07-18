import React from "react";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import SampleInCell from "./SampleInCell";
import SampleInSyringe from "./SampleInSyringe";
import CreateUuid from "@mbdb_deposit/buildingBlocks/CreateUuid";

function Measurements({ name }) {
  CreateUuid(name);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          fieldName="name"
          label="Name"
          required
          tooltip="Name (id) of the measurement which must be unique within a record (i.e. triplicates must be named individually in the raw data file). The name must allow location of the measurement data within the raw data file as well as processed data files if these are present"
          width="w-full"
        />
      </div>
      <div className="mb-3">
        <SampleInCell name={`${name}.sample_in_cell`} colorSchema="light" />
      </div>
      <div>
        <SampleInSyringe
          name={`${name}.sample_in_syringe`}
          colorSchema="light"
        />
      </div>
    </>
  );
}

export default Measurements;
