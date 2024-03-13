import React from "react";
import ArrayField from "../buildingBlocks/ArrayField";
import CustomField from "../buildingBlocks/CustomField";
import MolecularWeight from "../components/MolecularWeight";

function ComponentsChemical( { name, molecularWeightColorSchema } ) {

  return (
    <>
        <div className='flex mb-3'>
          <div className='mr-3'>
            <CustomField
              name={name}
              label='Name'
              fieldName='name'
              width='w-[30rem]'
              tooltip='Short descriptive name (id) of the entity; must be unique within a record (e.g. Lysozyme, Serum from Patient 1). This name is referenced in the measurement description to identify the entities present in measured sample'
            />
          </div>
          <div className="mr-3">
            <CustomField
              name={name}
              label='Inchikey'
              fieldName='inchikey'
              tooltip='InChIKey identifier of the chemical. In case of chemical polymers please specify the InChIKey of the monomer and specify the specific type in the additional identifiers field (e.g. if PEG 3350 was employed, the InChiKey of ethylene glycol, i.e. LYCAIKOWRPUZTN-UHFFFAOYSA-N should be specified here)'
            />
          </div>
          <div className="mr-3">
            <CustomField
              name={name}
              label='Copy number'
              fieldName='copy_number'
              type='number'
              tooltip='Number of molecules of the component within the assembly, -1 if unknown'
            />
          </div>
        </div>
        <div className="flex mb-3 -mt-3">
            <div className="mr-3">
                <ArrayField
                    name={name}
                    label='Additional identifier'
                    fieldName='additional_identifiers'
                    tooltip='Unique and persistent identifier from an external source; options of sources are CAS number, Pubchem Compound ID, and Pubchem Substance ID'
                    renderChild={({ arrayName, index }) => (
                        <CustomField
                            name={`${arrayName}.${index}`}
                            label={`Additional identifier ${index + 1}`}
                            tooltip='Unique and persistent identifier from an external source; options of sources are CAS number, Pubchem Compound ID, and Pubchem Substance ID'
                        />
                    )}
                />
            </div>
            <div className="mr-3">
                <ArrayField
                    name={name}
                    label='Additional specification'
                    fieldName='additional_specifications'
                    tooltip='Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)'
                    renderChild={({ arrayName, index }) => (
                        <CustomField
                            name={`${arrayName}.${index}`}
                            label={`Additional specification ${index + 1}`}
                            width='w-[15rem]'
                            tooltip='Additional information about the chemical can be specified here (e.g. RNase free water, recrystallization, desalting)'
                        />
                    )}
                />
            </div>
          <div>
              <ArrayField
                  name={name}
                  label='Isotopic labeling'
                  fieldName='isotopic_labeling'
                  maxItems={1}
                  tooltip='If the isotopic composition of the chemical was altered from the naturally occurring abundances, it can be specified here (e.g. 15N, 13C)'
                  renderChild={({ arrayName, index }) => (
                      <CustomField
                          name={`${arrayName}.${index}`}
                          label={`Isotopic labeling ${index + 1}`}
                          width='w-[15rem]'
                          tooltip='If the isotopic composition of the chemical was altered from the naturally occurring abundances, it can be specified here (e.g. 15N, 13C)'
                      />
                  )}
              />
            </div>
        </div>
        <div>
            <MolecularWeight
              name={`${name}.molecular_weight`}
              colorSchema={molecularWeightColorSchema}
              tooltipHeader='The molecular weight of the chemical'
            />
        </div>
    </>
  );
}

export default ComponentsChemical;