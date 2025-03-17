import React from "react";
import SampleFlowrate from "./SampleFlowrate";
import BufferFlowrate from "./BufferFlowrate";
import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";

export default function Flow({ name }) {
  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          label="Flow cell"
          fieldName="flow_cell"
          required
          tooltip="Type (description) of the flow cell"
        />
      </div>
      <div className="flex">
        <div className="mr-3">
          <SampleFlowrate
            name={`${name}.sample_flowrate`}
            colorSchema="light"
          />
        </div>
        <BufferFlowrate name={`${name}.buffer_flowrate`} colorSchema="light" />
      </div>
    </>
  );
}
