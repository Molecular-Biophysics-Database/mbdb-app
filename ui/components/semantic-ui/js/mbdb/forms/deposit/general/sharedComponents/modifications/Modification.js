import React from "react";
import CustomField from "../../../buildingBlocks/CustomField";
import Protocol from "../../../sharedComponents/Protocol";
import ArrayField from "../../../buildingBlocks/ArrayField";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import OptionalField from "../../../buildingBlocks/OptionalField";

export default function Modification({ name, colorSchema }) {
  const tooltips = {
    position:
      "The position in the primary sequence where the modification occurs (e.g. 23). Please indicate if the numbering differs from that implied by the sequence field",
    protocol: "List of steps that led to the modification taking place",
  };

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            required
            fieldName="type"
            label="Type"
            tooltip="The common name/type of the modification"
          />
        </div>
        <div className="-mt-3">
          <OptionalField
            name={name}
            fieldName="position"
            label="Position"
            tooltip={tooltips.position}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Position"
                tooltip={tooltips.position}
              />
            )}
          />
        </div>
      </div>

      <ArrayField
        name={name}
        label="Protocol"
        fieldName="protocol"
        tooltip={tooltips.protocol}
        renderChild={({ arrayName, index }) => (
          <FormWrapper
            headline={`Protocol ${index + 1}`}
            colorSchema={colorSchema}
            tooltip={tooltips.protocol}
          >
            <Protocol name={`${arrayName}.${index}`} />
          </FormWrapper>
        )}
      />
    </>
  );
}
