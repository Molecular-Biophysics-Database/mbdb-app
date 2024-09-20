import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import CustomField from "../../../buildingBlocks/CustomField";
import MolecularWeight from "../../sharedComponents/MolecularWeight";
import Modifications from "../../sharedComponents/modifications/Modifications";
import Concentration from "../../../sharedComponents/Concentration";
import OptionField from "../../../buildingBlocks/OptionField";
import QualityControls from "../../sharedComponents/qualityControls/QualityControls";
import OptionalField from "../../../buildingBlocks/OptionalField";
import SequenceField from "../../../buildingBlocks/SequenceField";
import ExternalDatabase from "../../../buildingBlocks/ExternalDatabase";
import { VocabularyRemoteSelectField } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { RORInstitutionResultListItem } from "../../../buildingBlocks/RORInstitutionResultListItem";
import FormWrapper from "../../../buildingBlocks/FormWrapper";

function Polymer({ name }) {
  const { getFieldData } = useFieldData();

  const polymerTypeOptions = [
    { value: "cyclic-pseudo-peptide", label: "cyclic-pseudo-peptide" },
    { value: "peptide nucleic acid", label: "peptide nucleic acid" },
    { value: "polydeoxyribonucleotide", label: "polydeoxyribonucleotide" },
    {
      value: "polydeoxyribonucleotide/polyribonucleotidehybrid",
      label: "polydeoxyribonucleotide/polyribonucleotidehybrid",
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
            width="w-[29rem]"
            tooltip="Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample"
          />
        </div>
        <div className="mr-3">
          <OptionField
            name={name}
            label="Polymer type"
            fieldName="polymer_type"
            options={polymerTypeOptions}
            tooltip="The type of polymer (e.g. polypeptide(L))"
          />
        </div>
        <div>
          <OptionField
            name={name}
            label="Expression source"
            fieldName="expression_source_type"
            options={expressionSourceTypeOptions}
            tooltip="How the polymer was produced"
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
              width="w-[51.5rem]"
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
      <div className="flex -mt-3 mb-3">
        <div className="mr-3">
          <ExternalDatabase name={name} />
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
      <div className="flex mb-3">
        <div className="mr-3">
          <MolecularWeight
            name={`${name}.molecular_weight`}
            tooltip="The molecular weight of the polymer"
          />
        </div>
        <div>
          <Concentration
            name={`${name}.concentration`}
            tooltip="Concentration of the constituent including its relative concentration related to the collected sample or absolute concentration of the constituent"
          />
        </div>
      </div>
      <div className="mb-3">
        <Modifications name={`${name}.modifications`} />
      </div>
      <div>
        <QualityControls name={`${name}.quality_controls`} />
      </div>
    </>
  );
}

export default Polymer;
