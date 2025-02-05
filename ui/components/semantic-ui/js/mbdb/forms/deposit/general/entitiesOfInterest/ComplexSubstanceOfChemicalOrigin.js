import React from "react";
import CustomField from "../../buildingBlocks/CustomField";
import ArrayField from "../../buildingBlocks/ArrayField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Protocol from "../../sharedComponents/Protocol";
import Storage from "../sharedComponents/Storage";
import Details from "../sharedComponents/Details";
import OptionField from "../../buildingBlocks/OptionField";
import UseDefault from "../../buildingBlocks/UseDefault";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";

function ComplexSubstanceOfChemicalOrigin({ name }) {
  CreateUuid(name);

  const classOptions = [{ value: "Lipid assembly", label: "Lipid assembly" }];

  const tooltips = {
    preparationProtocol:
      "List of the steps performed during the preparation of the complex substance",
    additionalSpecification:
      "Additional information about the complex substance can be specified here",
    storage:
      "Information about how the complex substance was stored between being acquired and measured, including temperature and duration",
  };

  const fieldNamePreparationProtocol = "preparation_protocol";
  UseDefault(`${name}.${fieldNamePreparationProtocol}`, [{}]);

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            label="Name"
            fieldName="name"
            required
            width="w-[44.5rem]"
            tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
          />
        </div>
        <OptionField
          name={name}
          options={classOptions}
          label="Class"
          fieldName="class"
          required
          tooltip="The chemical origin where the complex substance was derived from"
        />
      </div>
      <div className="flex -mt-3">
        <ArrayField
          name={name}
          label="Preparation protocol"
          fieldName={fieldNamePreparationProtocol}
          required
          tooltip={tooltips.preparationProtocol}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              colorSchema="light"
              headline={`Preparation protocol step ${index + 1}`}
              tooltip={tooltips.preparationProtocol}
            >
              <Protocol name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
        <ArrayField
          name={name}
          label="Additional specification"
          fieldName="additional_specifications"
          tooltip={tooltips.additionalSpecification}
          renderChild={({ arrayName, index }) => (
            <CustomField
              name={`${arrayName}.${index}`}
              label={`Additional specification ${index + 1}`}
              width="w-[15rem]"
              tooltip={tooltips.additionalSpecification}
            />
          )}
        />
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Storage"
          fieldName="storage"
          tooltip={tooltips.storage}
          renderChild={({ optionalFieldName }) => (
            <FormWrapper
              colorSchema="light"
              headline="Storage"
              tooltip={tooltips.storage}
            >
              <Storage name={optionalFieldName} />
            </FormWrapper>
          )}
        />
      </div>
      <Details
        name={`${name}.details`}
        colorSchema="light"
        molecularWeightColorSchema="light"
        colorSchemaProtocol="light"
        colorSchemaHeadline="light"
      />
    </>
  );
}

export default ComplexSubstanceOfChemicalOrigin;
