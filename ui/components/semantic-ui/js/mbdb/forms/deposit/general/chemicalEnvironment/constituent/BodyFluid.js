import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import OptionField from "../../../buildingBlocks/OptionField";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import Protocol from "../../../sharedComponents/Protocol";
import Storage from "../../sharedComponents/Storage";
import Concentration from "../../../sharedComponents/Concentration";
import OptionalField from "../../../buildingBlocks/OptionalField";
import UseDefault from "../../../buildingBlocks/UseDefault";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { NcbiTaxIdResultListItem } from "../../../buildingBlocks/NcbiTaxIdResultListItem";

function BodyFluid({ name }) {
  const { getFieldData } = useFieldData();

  const tooltips = {
    preparationProtocol:
      "List of the steps performed during the preparation of the complex substance",
    additionalSpecification:
      "Additional information about the complex substance can be specified here",
    storage:
      "Information about how the complex substance was stored between being acquired and measured, including temperature and duration",
  };

  const fluidOptions = [
    { value: "Blood", label: "Blood" },
    { value: "Fecal matter", label: "Fecal matter" },
    { value: "Milk", label: "Milk" },
    { value: "Plasma", label: "Plasma" },
    { value: "Saliva", label: "Saliva" },
    { value: "Serum", label: "Serum" },
    { value: "Urine", label: "Urine" },
    { value: "Plant extract", label: "Plant extract" },
  ];

  const fieldNamePreparationProtocol = "preparation_protocol";
  UseDefault(`${name}.${fieldNamePreparationProtocol}`, [{}]);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          label="Name"
          fieldName="name"
          width="w-full"
          tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
        />
      </div>
      <div className="flex mb-3">
        <div className="mr-3">
          <FormWrapper
            headline="Source organism"
            tooltip="Identification of the organism to the lowest taxonomic rank possible e.g. strain. Note that this is based on the NCBI taxonomy"
          >
            <VocabularyRemoteSelectField
              overriddenComponents={{
                "VocabularyRemoteSelect.ext.ResultsList.item":
                  NcbiTaxIdResultListItem,
              }}
              vocabulary="organisms"
              fieldPath={`${name}.source_organism`}
              modalHeader={
                getFieldData({
                  fieldPath: `${name}.source_organism`,
                  fieldRepresentation: "text",
                }).label
              }
            />
          </FormWrapper>
        </div>
        <div className="mr-3">
          <OptionField
            name={name}
            options={fluidOptions}
            label="Fluid"
            fieldName="fluid"
            tooltip="The body fluid the complex substance is derived from"
          />
        </div>

        <CustomField
          name={name}
          label="Health status"
          fieldName="health_status"
          tooltip="Health status of the donor organism where the body fluid was derived from (e.g. healthy, sick, patient with Diabetes type 2)"
        />
      </div>
      <div className="mb-3">
        <Concentration name={`${name}.concentration`} />
      </div>
      <div className="flex -mt-3">
        <div className="mr-3">
          <ArrayField
            name={name}
            label="Preparation protocol"
            fieldName={fieldNamePreparationProtocol}
            required
            tooltip={tooltips.preparationProtocol}
            renderChild={({ arrayName, index }) => (
              <FormWrapper
                headline={`Preparation protocol step ${index + 1}`}
                tooltip={tooltips.preparationProtocol}
              >
                <Protocol name={`${arrayName}.${index}`} />
              </FormWrapper>
            )}
          />
        </div>

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

      <OptionalField
        name={name}
        label="Storage"
        fieldName="storage"
        tooltip={tooltips.storage}
        renderChild={({ optionalFieldName }) => (
          <FormWrapper headline="Storage" tooltip={tooltips.storage}>
            <Storage name={optionalFieldName} colorSchema="light" />
          </FormWrapper>
        )}
      />
    </>
  );
}

export default BodyFluid;
