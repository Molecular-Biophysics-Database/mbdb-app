import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import CustomField from "../../buildingBlocks/CustomField";

function Location({ name, tooltip, colorSchema }) {
  return (
    <>
      <FormWrapper
        headline="Location"
        colorSchema={colorSchema}
        tooltip={tooltip}
      >
        <div className="flex">
          <div>
            <CustomField
                name={name}
                label="Latitude"
                fieldName="latitude"
                required
                tooltip="The latitude, from south to north, in degrees (decimal notation)"
            />
          </div>
          <div>
            <CustomField
                name={name}
                label="Longitude"
                fieldName="longitude"
                required
                tooltip="The longitude, from west to east, in degrees (decimal notation)"
            />
          </div>
          <div>
            <CustomField
                name={name}
                label="Altitude"
                fieldName="Altitude"
                required
                tooltip="The altitude, in meters, above mean sea-level (negative numbers are allowed)"
            />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default Location;
