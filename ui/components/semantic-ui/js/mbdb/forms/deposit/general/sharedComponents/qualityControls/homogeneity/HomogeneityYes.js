import CustomField from '../../../../buildingBlocks/CustomField';
import OptionField from '../../../../buildingBlocks/OptionField';

function HomogeneityYes( { name } ) {

    const methodOptions = [
        { value: 'Size exclusion chromatography', label: 'Size exclusion chromatography' },
        { value: 'Native Gel Electrophoresis', label: 'Native Gel Electrophoresis' },
        { value: 'Mass photometry', label: 'Mass photometry' },
    ];

  return (
    <>
        <div className='flex'>
            <div className='mr-3'>
                <OptionField
                    name={name}
                    fieldName='method'
                    label='Method'
                    options={methodOptions}
                    tooltip='The method used to evaluate the homogeneity'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='expected_number_of_species'
                    label='Expected number of species'
                    tooltip='The number of species that were expected to be present'
                    type='number'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='number_of_species_observed'
                    label='Number of species observed'
                    tooltip='The number of species that was observed to be present'
                    type='number'
                />
            </div>
        </div>
    </>
  );
}

export default HomogeneityYes;
