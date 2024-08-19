import React from "react";
import ByIntactMass from "./ByIntactMass";
import BySequencing from "./BySequencing";
import ByFingerprinting from "./ByFingerprinting";
import OptionalField from "../../../../buildingBlocks/OptionalField";

function IdentityYes({ name, colorSchema }) {
  return (
    <>
      <div>
        <OptionalField
          name={name}
          label="By intact mass"
          fieldName="by_intact_mass"
          tooltip="How identity was determined by intact mass, if applicable"
          renderChild={({ optionalFieldName }) => (
            <ByIntactMass name={optionalFieldName} colorSchema={colorSchema} />
          )}
        />
      </div>
      <div>
        <OptionalField
          name={name}
          label="By sequencing"
          fieldName="by_sequencing"
          tooltip="How identity was assessed by sequencing, if applicable"
          renderChild={({ optionalFieldName }) => (
            <BySequencing name={optionalFieldName} colorSchema={colorSchema} />
          )}
        />
      </div>
      <div>
        <OptionalField
          name={name}
          label="By fingerprinting"
          fieldName="by_fingerprinting"
          tooltip="How identity was determined by fingerprinting, if applicable"
          renderChild={({ optionalFieldName }) => (
            <ByFingerprinting
              name={optionalFieldName}
              colorSchema={colorSchema}
            />
          )}
        />
      </div>
    </>
  );
}

export default IdentityYes;
