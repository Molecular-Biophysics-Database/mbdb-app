import React from "react";
import Instrument from "@mbdb_deposit/sharedComponents/Instrument";
import FormWrapper from "@mbdb_deposit/buildingBlocks/FormWrapper";
import PrimaryLaserWavelength from "../PrimaryLaserWavelength/PrimaryLaserWavelength";
import OptionalField from "@mbdb_deposit/buildingBlocks/OptionalField";

export default function InstrumentTab({ name }) {
  return (
    <>
      <div className="w-fit">
        <FormWrapper>
          Instrument type and settings as well as the experiment type
        </FormWrapper>
      </div>
      <div className="my-3 mb-3">
        <Instrument name={`${name}.instrument`} />
      </div>
      <div>
        <OptionalField
          label="Primary laser wavelength"
          name="metadata.method_specific_parameters.primary_laser_wavelength"
          tooltip="Wavelength of the laser used for measurement of the mass photometry signal"   
          renderChild={({ optionalFieldName }) => (
            <PrimaryLaserWavelength name={optionalFieldName} />
          )}
        />
      </div>
    </>
  );
}
