import React from "react";
import ArrayField from "../../buildingBlocks/ArrayField";
import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Protocol from "../../sharedComponents/Protocol";
import Storage from "../sharedComponents/Storage";
import OptionField from "../../buildingBlocks/OptionField";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";
import UseDefault from "../../buildingBlocks/UseDefault";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../../buildingBlocks/RORInstitutionResultListItem";

function Virion({ name }) {
  CreateUuid(name);
  const { getFieldData } = useFieldData();

  const geneticMaterialOptions = [
    { value: "No genetic material", label: "No genetic material" },
    { value: "Virus genome", label: "Virus genome" },
    { value: "Synthetic", label: "Synthetic" },
  ];

  const capsidTypeOptions = [
    { value: "None", label: "None" },
    { value: "Native", label: "Native" },
    { value: "Genetically Engineered", label: "Genetically Engineered" },
    { value: "Synthetic", label: "Synthetic" },
  ];

  const envelopeOptions = [
    { value: "None", label: "None" },
    { value: "Native", label: "Native" },
    { value: "Genetically Engineered", label: "Genetically Engineered" },
    { value: "Synthetic", label: "Synthetic" },
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
          required
          tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
        />
      </div>
      <div className="flex">
        <div className="mr-3">
          <FormWrapper
            headline="Source organism"
            colorSchema="light"
            tooltip="Identification of the organism to the lowest taxonomic rank possible e.g. strain. Note that this is based on the NCBI taxonomy"
          >
            <VocabularyRemoteSelectField
              overriddenComponents={{
                "VocabularyRemoteSelect.ext.ResultsList.item":
                  RORInstitutionResultListItem,
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
            options={geneticMaterialOptions}
            label="Genetic Material"
            fieldName="genetic_material"
            required
            tooltip="The genetic material carried by the virions (None, virus genome, synthetic)"
          />
        </div>
        <div>
          <OptionField
            name={name}
            options={capsidTypeOptions}
            label="Capsid type"
            fieldName="capsid_type"
            required
            tooltip="The type of virion capsid (e.g. genetically engineered, None"
          />
        </div>
        <div>
          <OptionField
            name={name}
            options={envelopeOptions}
            label="Envelope type"
            fieldName="envelope_type"
            required
            tooltip="The type of virion envelope (e.g. genetically engineered, None"
          />
        </div>
      </div>
      <div className="flex mb-3">
        <div className="mr-3">
          <OptionalField
            name={name}
            label="Host organism"
            fieldName="host_organism"
            tooltip="The host organism the virion was produced in. Note that information is based on the NCBI taxonomy"
            renderChild={({ optionalFieldName }) => (
              <FormWrapper
                headline="Host organism"
                colorSchema="light"
                tooltip="The host organism the virion was produced in. Note that information is based on the NCBI taxonomy"
              >
                <VocabularyRemoteSelectField
                  overriddenComponents={{
                    "VocabularyRemoteSelect.ext.ResultsList.item":
                      RORInstitutionResultListItem,
                  }}
                  vocabulary="organisms"
                  fieldPath={optionalFieldName}
                  modalHeader={
                    getFieldData({
                      fieldPath: optionalFieldName,
                      fieldRepresentation: "text",
                    }).label
                  }
                />
              </FormWrapper>
            )}
          />
        </div>
        <div className="mr-3">
          <OptionalField
            name={name}
            label="Host cell type"
            fieldName="host_cell_type"
            tooltip="The host cell type the virion was produced in (e.g. macrophage)"
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Host cell type"
                tooltip="The host cell type the virion was produced in (e.g. macrophage)"
              />
            )}
          />
        </div>
        <div>
          <ArrayField
            name={name}
            label="Additional specification"
            fieldName="additional_specifications"
            tooltip="Additional information about the complex substance can be specified here"
            renderChild={({ arrayName, index }) => (
              <CustomField
                name={`${arrayName}.${index}`}
                label={`Additional specification ${index + 1}`}
                width="w-[15rem]"
                tooltip="Additional information about the complex substance can be specified here"
              />
            )}
          />
        </div>
      </div>
      <div>
        <ArrayField
          name={name}
          label="Preparation protocol"
          fieldName={fieldNamePreparationProtocol}
          required
          tooltip="List of the steps performed during the preparation of the complex substance"
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              colorSchema="light"
              headline={`Preparation protocol step ${index + 1}`}
              tooltip="List of the steps performed during the preparation of the complex substance"
            >
              <Protocol name={`${arrayName}.${index}`} />
            </FormWrapper>
          )}
        />
      </div>
      <div>
        <OptionalField
          name={name}
          label="Storage"
          fieldName="storage"
          tooltip="Information about how the complex substance was stored between being acquired and measured, including temperature and duration"
          renderChild={({ optionalFieldName }) => (
            <FormWrapper
              colorSchema="light"
              headline="Storage"
              tooltip="Information about how the complex substance was stored between being acquired and measured, including temperature and duration"
            >
              <Storage name={optionalFieldName} />
            </FormWrapper>
          )}
        />
      </div>
    </>
  );
}

export default Virion;
