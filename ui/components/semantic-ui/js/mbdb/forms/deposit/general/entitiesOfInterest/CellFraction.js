import React from "react";
import ArrayField from "../../buildingBlocks/ArrayField";
import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import Protocol from "../../sharedComponents/Protocol";
import Storage from "../sharedComponents/Storage";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";
import UseDefault from "../../buildingBlocks/UseDefault";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../../buildingBlocks/RORInstitutionResultListItem";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";

function CellFraction({ name }) {
  CreateUuid(name);
  const { getFieldData } = useFieldData();

  const fieldNamePreparationProtocol = "preparation_protocol";
  UseDefault(`${name}.${fieldNamePreparationProtocol}`, [{}]);

  return (
    <>
      <div className="mb-3">
        <CustomField
          name={name}
          label="Name"
          fieldName="name"
          required
          width="w-full"
          tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
        />
      </div>
      <div className="flex mb-3">
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
          <FormWrapper
              headline="Fraction"
              colorSchema="light"
              tooltip="The sub-cellular component (e.g. Ribosome)"
          >
            <VocabularySelectField
                search={(options) => options}
                type="cell_fractions"
                label={<FieldLabel htmlFor={`${name}.fraction`} icon=""/>}
                fieldPath={`${name}.fraction`}
                placeholder="Fraction"
                clearable
            />
          </FormWrapper>
        </div>
        <div>
          <CustomField
              name={name}
              label="Health status"
              fieldName="health_status"
              required
              tooltip="Health status of the donor organism where the cell fraction was derived from (e.g. healthy, sick, patient with Diabetes type 2)"
          />
        </div>
      </div>
      <div className="flex -mt-3 mb-3">
        <div className="mr-3">
          <OptionalField
              name={name}
              label="Organ"
              fieldName="organ"
              tooltip="The organ the cell fraction was derived from (e.g. heart)"
              renderChild={({optionalFieldName}) => (
                  <CustomField
                      name={optionalFieldName}
                      label="Organ"
                      tooltip="The organ the cell fraction was derived from (e.g. heart)"
                  />
              )}
          />
        </div>
        <div className="mr-3">
          <OptionalField
              name={name}
              label="Tissue"
            fieldName="tissue"
            tooltip="The tissue type the cell fraction was derived from (e.g. epithelia, muscle)"
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Tissue"
                tooltip="The tissue type the cell fraction was derived from (e.g. epithelia, muscle)"
              />
            )}
          />
        </div>
        <div>
          <OptionalField
            name={name}
            label="Cell type"
            fieldName="cell_type"
            tooltip="The cell type the cell fraction was derived from (e.g. macrophage, sperm)"
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Cell type"
                tooltip="The cell type the cell fraction was derived from (e.g. macrophage, sperm)"
              />
            )}
          />
        </div>
      </div>
      <div className="flex -mt-3">
        <div className="mr-3">
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

export default CellFraction;
