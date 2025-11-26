import React from "react";
import ArrayField from "../../buildingBlocks/ArrayField";
import CustomField from "../../buildingBlocks/CustomField";
import MolecularWeight from "../sharedComponents/MolecularWeight";
import Modifications from "../sharedComponents/modifications/Modifications";
import OptionField from "../../buildingBlocks/OptionField";
import QualityControls from "../sharedComponents/qualityControls/QualityControls";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";
import SequenceField from "../../buildingBlocks/SequenceField";
import ExternalDatabase from "../../buildingBlocks/ExternalDatabase";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { NcbiTaxIdResultListItem } from "../../buildingBlocks/NcbiTaxIdResultListItem";

function Polymer({ name }) {
  CreateUuid(name);
  const { getFieldData } = useFieldData();

  const tooltips = {
    sequence:
      "Primary sequence of the polymer using single letter codes (e.g. SAGRELLE, AGTTA). This should be the sequence of the polymer that was used in the experiment including mutations, purification tags etc. For non-canonical amino acids or nucleotides, please place the full name of the monomer in angle brackets (e.g. SAGREL<3-Sulfinoalanine>LE)",
    variant:
      "Annotation of the primary sequence can be specified here (e.g. Wildtype, C-terminal 6x-histag). Note that this also applies to polymers of unknown sequence",
    sourceOrganism:
      "The biological species where the polymer naturally occurs. Note that this is based on the NCBI taxonomy",
    expressionOrganism:
      "The biological species that was used to express (produce) the polymer. Note that this is based on the NCBI taxonomy",
    additionalSpecification:
      "Additional information about the polymer can be specified here",
  };

  const polymerTypeOptions = [
    { value: "cyclic-pseudo-peptide", label: "cyclic-pseudo-peptide" },
    { value: "peptide nucleic acid", label: "peptide nucleic acid" },
    { value: "polydeoxyribonucleotide", label: "polydeoxyribonucleotide" },
    {
      value: "polydeoxyribonucleotide/polyribonucleotide hybrid",
      label: "polydeoxyribonucleotide/polyribonucleotide hybrid",
    },
    { value: "polypeptide(D)", label: "polypeptide(D)" },
    { value: "polypeptide(L)", label: "polypeptide(L)" },
    { value: "polyribonucleotide", label: "polyribonucleotide" },
  ];

  const expressionSourceTypeOptions = [
    { value: "Natively", label: "Natively" },
    { value: "Recombinantly", label: "Recombinantly" },
    { value: "Synthetically", label: "Synthetically" },
  ];

  return (
    <>
      <div className="flex mb-3">
        <div className="mr-3">
          <CustomField
            name={name}
            label="Name"
            fieldName="name"
            required
            width="w-[29rem]"
            tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1, Ligand A). This name is referenced in the measurement description to identify the entities present in the measured sample"
          />
        </div>
        <div className="mr-3">
          <OptionField
            name={name}
            label="Polymer type"
            fieldName="polymer_type"
            required
            options={polymerTypeOptions}
            tooltip="The type of polymer (e.g. polypeptide(L))"
          />
        </div>

        <OptionField
          name={name}
          label="Expression source"
          fieldName="expression_source_type"
          required
          options={expressionSourceTypeOptions}
          tooltip="How the polymer was produced"
        />
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Sequence"
          fieldName="sequence"
          tooltip={tooltips.sequence}
          renderChild={({ optionalFieldName }) => (
            <SequenceField
              name={optionalFieldName}
              colorSchema="light"
              label="Sequence"
              width="w-[51.5rem]"
              tooltip={tooltips.sequence}
            />
          )}
        />
      </div>
      <div className="flex mb-3 -mt-3">
        <div className="mr-3">
          <OptionalField
            name={name}
            label="Variant"
            fieldName="variant"
            tooltip={tooltips.variant}
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Variant"
                tooltip={tooltips.variant}
              />
            )}
          />
        </div>
        <div className="mr-3">
          <OptionalField
            name={name}
            label="Source organism"
            fieldName="source_organism"
            tooltip={tooltips.sourceOrganism}
            renderChild={({ optionalFieldName }) => (
              <FormWrapper
                headline="Source organism"
                colorSchema="light"
                tooltip={tooltips.sourceOrganism}
              >
                <VocabularyRemoteSelectField
                  overriddenComponents={{
                    "VocabularyRemoteSelect.ext.ResultsList.item":
                      NcbiTaxIdResultListItem,
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

        <OptionalField
          name={name}
          label="Expression organism"
          fieldName="expression_organism"
          tooltip={tooltips.expressionOrganism}
          renderChild={({ optionalFieldName }) => (
            <FormWrapper
              headline="Expression organism"
              colorSchema="light"
              tooltip={tooltips.expressionOrganism}
            >
              <VocabularyRemoteSelectField
                overriddenComponents={{
                  "VocabularyRemoteSelect.ext.ResultsList.item":
                    NcbiTaxIdResultListItem,
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
      <div className="flex -mt-3 mb-3">
        <div className="mr-3">
          <ExternalDatabase name={name} colorSchema="light" />
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
      <div className="mb-3 w-fit">
        <MolecularWeight
          name={`${name}.molecular_weight`}
          colorSchema="light"
          tooltip="The molecular weight of the polymer"
        />
      </div>
      <div className="mb-3">
        <Modifications name={`${name}.modifications`} colorSchema="light" />
      </div>

      <QualityControls name={`${name}.quality_controls`} colorSchema="light" />
    </>
  );
}

export default Polymer;
