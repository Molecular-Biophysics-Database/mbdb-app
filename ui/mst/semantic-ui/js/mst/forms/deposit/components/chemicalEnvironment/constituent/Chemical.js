import React from "react";
import ArrayField from "../../buildingBlocks/ArrayField";
import CustomField from "../../buildingBlocks/CustomField";
import Concentration from "../../components/Concentration";
import MolecularWeight from "../../components/MolecularWeight";

function Chemical( { name } ) {

  return (
    <>
        <div className='flex mb-3'>
          <div className='mr-3'>
            <CustomField
              name={name}
              label='Name'
              fieldName='name'
              width='w-[25rem]'
              tooltip='Name of the chemical environment (e.g. Measurement Buffer). The name must be unique within a record as it will be referred to the in method specific section in when describing the composition of the individual samples or measurement steps'
            />
          </div>
          <div>
            <CustomField
              name={name}
              label='Inchikey'
              fieldName='inchikey'
              tooltip='InChIKey identifier of the chemical. In case of chemical polymers please specify the InChIKey of the monomer and specify the specific type in the additional identifiers field (e.g. if PEG 3350 was employed, the InChiKey of ethylene glycol, i.e. LYCAIKOWRPUZTN-UHFFFAOYSA-N should be specified here)'
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
                            width='w-[15rem]'
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
        <div className="flex">
          <div className="mr-3">
              <MolecularWeight
                name={`${name}.molecular_weight`}
                tooltipHeader='The molecular weight of the chemical'
              />
          </div>
          <div>
              <Concentration
                  name={`${name}.concentration`}
                  tooltipHeader='Concentration of the constituent including its relative concentration related to the collected sample or absolute concentration of the constituent'
              />
          </div>
        </div>
    </>
  );
}

export default Chemical;