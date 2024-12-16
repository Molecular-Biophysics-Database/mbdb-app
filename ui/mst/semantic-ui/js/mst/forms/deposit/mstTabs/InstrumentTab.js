import React from "react";
import Instrument from "@mbdb_deposit/sharedComponents/Instrument";
import MethodSpecificParameters from "../instrument/MethodSpecificParameters";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

function InstrumentTab({ name }) {
  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>Instrument type and settings</FormWrapper>
      </div>
      <div className="mb-3">
        <Instrument name={`${name}.instrument`} />
      </div>
      <div className="mt-3">
        <MethodSpecificParameters name="metadata.method_specific_parameters" />
      </div>
    </>
  );
}

export default InstrumentTab;
