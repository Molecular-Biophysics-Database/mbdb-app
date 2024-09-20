import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import MolecularWeight from "../MolecularWeight";
import Modifications from "../modifications/Modifications";
import OptionField from "../../../buildingBlocks/OptionField";
import QualityControls from "../qualityControls/QualityControls";
import OptionalField from "../../../buildingBlocks/OptionalField";
import SequenceField from "../../../buildingBlocks/SequenceField";
import ExternalDatabase from "../../../buildingBlocks/ExternalDatabase";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../../../buildingBlocks/RORInstitutionResultListItem";

function Polymer({ name, colorSchema }) {
  const { getFieldData } = useFieldData();

  const polymerTypeOptions = [
    { value: "Cyclic pseudo peptide", label: "Cyclic pseudo peptide" },
    { value: "Peptide nucleic acid", label: "Peptide nucleic acid" },
    { value: "Polydeoxyribonucleotide", label: "Polydeoxyribonucleotide" },
    {
      value: "Polydeoxyribonucleotide / polyribonucleotide hybrid",
      label: "Polydeoxyribonucleotide / polyribonucleotide hybrid",
    },
    { value: "Polypeptide(D)", label: "Polypeptide(D)" },
    { value: "Polypeptide(L)", label: "Polypeptide(L)" },
    { value: "Polyribonucleotide", label: "Polyribonucleotide" },
  ];

  const expressionSourceTypeOptions = [
    { value: "Natively", label: "Natively" },
    { value: "Recombinantly", label: "Recombinantly" },
    { value: "Synthetically", label: "Synthetically" },
  ];

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
          <OptionField
            name={name}
            label="Polymer type"
            fieldName="polymer_type"
            required
            options={polymerTypeOptions}
            tooltip="The type of polymer (e.g. polypeptide(L))"
          />
        </div>
        <div className="mr-3">
          <OptionField
            name={name}
            label="Expression source"
            fieldName="expression_source_type"
            required
            options={expressionSourceTypeOptions}
            tooltip="How the polymer was produced"
          />
        </div>
        <div>
          <CustomField
            name={name}
            label="Copy number"
            fieldName="copy_number"
            required
            type="number"
            tooltip="Number of molecules of the component within the assembly, -1 if unknown"
          />
        </div>
      </div>
      <div className="mb-3">
        <OptionalField
          name={name}
          label="Sequence"
          fieldName="sequence"
          tooltip="Primary sequence of the polymer, using single letter codes (e.g. SAGRELLE, AGTTA). In case of non-natural amino acids or nucleotides, please place the monomer in brackets"
          renderChild={({ optionalFieldName }) => (
            <SequenceField
              name={optionalFieldName}
              label="Sequence"
              width="w-[50rem]"
              tooltip="Primary sequence of the polymer, using single letter codes (e.g. SAGRELLE, AGTTA). In case of non-natural amino acids or nucleotides, please place the monomer in brackets"
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
            tooltip="Descriptive name indicating differences of primary sequence of the polymer as compared to the most common form, or wildtype, including mutations, purification tags, etc. (A53T, C-terminal GFP, N-terminal 6xHis-tag)"
            renderChild={({ optionalFieldName }) => (
              <CustomField
                name={optionalFieldName}
                label="Variant"
                tooltip="Descriptive name indicating differences of primary sequence of the polymer as compared to the most common form, or wildtype, including mutations, purification tags, etc. (A53T, C-terminal GFP, N-terminal 6xHis-tag)"
              />
            )}
          />
        </div>
        <div className="mr-3">
          <OptionalField
            name={name}
            label="Source organism"
            fieldName="source_organism"
            tooltip="The biological species where the polymer naturally occurs. Note that this is based on the NCBI taxonomy"
            renderChild={({ optionalFieldName }) => (
              <FormWrapper
                headline="Source organism"
                tooltip="The biological species where the polymer naturally occurs. Note that this is based on the NCBI taxonomy"
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
        <div>
          <OptionalField
            name={name}
            label="Expression organism"
            fieldName="expression_organism"
            tooltip="The biological species that was used to express (produce) the polymer. Note that this is based on the NCBI taxonomy"
            renderChild={({ optionalFieldName }) => (
              <FormWrapper
                headline="Expression organism"
                tooltip="The biological species that was used to express (produce) the polymer. Note that this is based on the NCBI taxonomy"
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
      </div>
      <div className="flex mb-3 -mt-3">
        <div className="mr-3">
          <ExternalDatabase name={name} colorSchema={colorSchema} />
        </div>
        <div>
          <ArrayField
            name={name}
            label="Additional specification"
            fieldName="additional_specifications"
            tooltip="Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)"
            renderChild={({ arrayName, index }) => (
              <CustomField
                name={`${arrayName}.${index}`}
                label={`Additional specification ${index + 1}`}
                width="w-[15rem]"
                tooltip="Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)"
              />
            )}
          />
        </div>
      </div>
      <div className="mb-3">
        <MolecularWeight
          name={`${name}.molecular_weight`}
          tooltip="The molecular weight of the polymer"
          colorSchema={colorSchema}
        />
      </div>
      <div className="mb-3">
        <Modifications
          name={`${name}.modifications`}
          colorSchema={colorSchema}
        />
      </div>
      <div>
        <QualityControls
          name={`${name}.quality_controls`}
          colorSchema={colorSchema}
        />
      </div>
    </>
  );
}

export default Polymer;
