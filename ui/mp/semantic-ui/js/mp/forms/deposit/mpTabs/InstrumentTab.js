import React from "react";
import Instrument from "@mbdb_deposit/sharedComponents/Instrument";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";

export default function InstrumentTab({ name }) {
  return (
    <>
      <div className="w-fit">
        <FormWrapper>
          Instrument type and settings as well as the experiment type
        </FormWrapper>
      </div>
      <div className="my-3">
        <Instrument name={`${name}.instrument`} />
      </div>
    </>
  );
}
