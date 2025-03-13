import React from "react";
import FlowCell from "./FlowCell";
import SampleFlowrate from "./SampleFlowrate";
import BufferFlowrate from "./BufferFlowrate";

export default function Flow({ name }) {
  return (
    <>
      <div className="mb-3">
        <FlowCell name={`${name}.flow_cell`} colorSchema="light" />
      </div>
      <div className="mb-3">
        <SampleFlowrate name={`${name}.sample_flowrate`} colorSchema="light" />
      </div>
      <BufferFlowrate name={`${name}.buffer_flowrate`} colorSchema="light" />
    </>
  );
}
