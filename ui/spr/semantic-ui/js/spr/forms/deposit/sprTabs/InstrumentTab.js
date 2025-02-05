import React from "react";
import Instrument from "@mbdb_deposit/sharedComponents/Instrument";
import MethodSpecificParameters from "../instrument/MethodSpecificParameters";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

export default function InstrumentTab({ name }) {
  return (
    <>
      <div className="w-fit">
        <FormWrapper>Instrument type and experiment type</FormWrapper>
      </div>
      <div className="my-3">
        <Instrument name={`${name}.instrument`} />
      </div>
      <MethodSpecificParameters name="metadata.method_specific_parameters" />
    </>
  );
}
