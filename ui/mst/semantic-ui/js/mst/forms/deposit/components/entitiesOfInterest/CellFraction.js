import React from "react";
import ArrayField from "../buildingBlocks/ArrayField";
import CustomField from "../buildingBlocks/CustomField";
import FormWrapper from "../buildingBlocks/FormWrapper";
import Protocol from "../buildingBlocks/Protocol";
import Storage from "../buildingBlocks/Storage";
import OptionField from "../buildingBlocks/OptionField";

function CellFraction( { name } ) {

    const fractionOptions = [
        { value: 'Ribosome', label: 'Ribosome' },
        { value: 'Cell wall', label: 'Cell wall' },
        { value: 'VesicleCell lysate/Cytoplasm', label: 'VesicleCell lysate/Cytoplasm' },
        { value: 'Cell Membrane', label: 'Cell Membrane' },
        { value: 'Extracellular matrix', label: 'Extracellular matrix' },
        { value: 'Lysosome', label: 'Lysosome' },
        { value: 'Golgi Apparatus', label: 'Golgi Apparatus' },
        { value: 'Mitochondrion', label: 'Mitochondrion' },
        { value: 'Rough Endoplasmic Reticulum', label: 'Rough Endoplasmic Reticulum' },
        { value: 'Smooth Endoplasmic Reticulum', label: 'Smooth Endoplasmic Reticulum' },
        { value: 'Vacuole', label: 'Vacuole' },
        { value: 'Chloroplast', label: 'Chloroplast' },
    ];

  return (
    <>
        <div className=''>
            <div className="flex mb-3">
                <div className='mr-3'>
                    <CustomField
                        name={name}
                        label='Name'
                        fieldName='name'
                        tooltip='Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample'
                    />
                </div>
                <div className="mr-3">
                    <OptionField
                        name={name}
                        options={fractionOptions}
                        label='Fraction'
                        fieldName='fraction'
                        tooltip='The subcelluar component e.g. (Ribosome)'
                    />
                </div>
                <div className="mr-3">
                    <CustomField
                        name={name}
                        label='Health status'
                        fieldName='health_status'
                        tooltip='Health status of the donor organism where the cell fraction was derived from (e.g. healthy, sick, patient with Diabetes type 2)'
                    />
                </div>
                <div>
                    <CustomField
                        name={name}
                        label='Source organism'
                        fieldName='source_organism'
                        tooltip='Identification of the organism to the lowest taxonomic rank possible e.g. strain. Note that this is based on the NCBI taxonomy'
                    />
                </div>
            </div>
            <div className="flex -mt-3 mb-3">
                <div className="mr-3">
                    <ArrayField
                        name={name}
                        label='Organ'
                        fieldName='organ'
                        maxItems={1}
                        tooltip='The organ the cell fraction was derived from (e.g. heart)'
                        renderChild={({ arrayName, index }) => (
                            <CustomField
                                name={`${arrayName}.${index}`}
                                label='Organ'
                                tooltip='The organ the cell fraction was derived from (e.g. heart)'
                            />
                        )}
                    />
                </div>
                <div className="mr-3">
                    <ArrayField
                        name={name}
                        label='Tissue'
                        fieldName='tissue'
                        maxItems={1}
                        tooltip='The tissue type the cell fraction was derived from'
                        renderChild={({ arrayName, index }) => (
                            <CustomField
                                name={`${arrayName}.${index}`}
                                label='Tissue'
                                tooltip='The tissue type the cell fraction was derived from'
                            />
                        )}
                    />
                </div>
                <div>
                    <ArrayField
                        name={name}
                        label='Cell type'
                        fieldName='cell_type'
                        maxItems={1}
                        tooltip='The cell type the cell fraction was derived from'
                        renderChild={({ arrayName, index }) => (
                            <CustomField
                                name={`${arrayName}.${index}`}
                                label='Cell type'
                                tooltip='The cell type the cell fraction was derived from'
                            />
                        )}
                    />
                </div>
            </div>
        </div>
        <div className="flex -mt-3">
            <div className="mr-3">
                <ArrayField
                    name={name}
                    label='Preparation protocol'
                    fieldName='preparation_protocol'
                    tooltip='List of the steps performed during the preparation of the complex substance'
                    renderChild={({ arrayName, index }) => (
                        <FormWrapper 
                            colorSchema='light'
                            headline={`Preparation protocol ${index + 1}`}
                            tooltipHeader='List of the steps performed during the preparation of the complex substance'
                        >
                            <Protocol
                                name={`${arrayName}.${index}`}
                            />
                        </FormWrapper>
                    )}
                />
            </div>
            <div>
                <ArrayField
                    name={name}
                    label='Additional specification'
                    fieldName='additional_specifications'
                    tooltip='Additional information about the complex substance can be specified here'
                    renderChild={({ arrayName, index }) => (
                        <CustomField
                            name={`${arrayName}.${index}`}
                            label={`Additional specification ${index + 1}`}
                            width='w-[15rem]'
                            tooltip='Additional information about the complex substance can be specified here'
                        />
                    )}
                />
            </div>
        </div>
        <div>
            <ArrayField
                name={name}
                label='Storage'
                fieldName='storage'
                maxItems={1}
                tooltip='Information about how the complex substance was stored between being acquired and measured, including temperature and duration'
                renderChild={({ arrayName, index }) => (
                    <FormWrapper
                        colorSchema='light'
                        headline={`Storage ${index + 1}`}
                        tooltipHeader='Information about how the complex substance was stored between being acquired and measured, including temperature and duration'
                    >
                        <Storage
                            name={`${arrayName}.${index}`}
                        />
                    </FormWrapper>
                )}
            />
        </div>
    </>
  );
}

export default CellFraction;