import React from "react";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import CustomField from "../../buildingBlocks/CustomField";

export default function Location({ name, tooltip, colorSchema }) {
  return (
    <>
      <FormWrapper
        headline="Location"
        colorSchema={colorSchema}
        tooltip={tooltip}
        name={name}
      >
        <div className="flex">
          <CustomField
            name={name}
            label="Latitude"
            fieldName="latitude"
            type="number"
            required
            min={-90}
            max={90}
            width="w-40"
            tooltip="The latitude, from south to north, in degrees (decimal notation)"
          />

          <div className="mx-3">
            <CustomField
              name={name}
              label="Longitude"
              fieldName="longitude"
              type="number"
              required
              min={-180}
              max={180}
              width="w-40"
              tooltip="The longitude, from west to east, in degrees (decimal notation)"
            />
          </div>

          <CustomField
            name={name}
            label="Altitude"
            fieldName="altitude"
            type="number"
            required
            min={-6378100}
            width="w-40"
            tooltip="The altitude, in meters, above mean sea-level (negative numbers are allowed)"
          />
        </div>
      </FormWrapper>
    </>
  );
}
