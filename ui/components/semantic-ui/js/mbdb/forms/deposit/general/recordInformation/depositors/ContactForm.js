import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import Identifier from "../../../buildingBlocks/Identifier";
import Affiliation from "./Affiliation";

function ContactForm({ name }) {
  const tooltips = {
    affiliation:
      "The affiliation of the person. Note that this is based on the Research Organization Registry (ROR)",
  };

  return (
    <>
      <div className="flex">
        <div className="mr-3">
          <CustomField
            name={name}
            label="Given name"
            fieldName="given_name"
            required
            tooltip="The given name(s), including middlename(s), of the person"
          />
        </div>

        <CustomField
          name={name}
          label="Family name"
          fieldName="family_name"
          required
          tooltip="The family name(s) of the person"
        />
      </div>
      <div className="flex">
        <div className="mr-3">
          <ArrayField
            name={name}
            label="identifier"
            fieldName="identifiers"
            tooltip="Persistent personal identifiers, currently only ORCIDs are allowed"
            renderChild={({ arrayName, index }) => (
              <Identifier
                name={`${arrayName}.${index}`}
                label={`Identifier ${index + 1}`}
              />
            )}
          />
        </div>

        <ArrayField
          name={name}
          label="affiliation"
          fieldName="affiliations"
          tooltip={tooltips.affiliation}
          renderChild={({ arrayName, index }) => (
            <Affiliation
              arrayName={arrayName}
              index={index}
              tooltip={tooltips.affiliation}
            />
          )}
        />
      </div>
    </>
  );
}

export default ContactForm;
