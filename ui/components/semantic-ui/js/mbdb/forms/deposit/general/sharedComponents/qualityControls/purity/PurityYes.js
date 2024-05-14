import OptionField from '../../../../buildingBlocks/OptionField';

function PurityYes( { name } ) {

    const methodOptions = [
        { value: 'SDS-PAGE', label: 'SDS-PAGE' },
        { value: 'Capillary Electrophoresis', label: 'Capillary Electrophoresis' },
        { value: 'Agarose Gel electrophoresis', label: 'Agarose Gel electrophoresis' },
    ];

    const purityPercentageOptions = [
        { value: '<90 %', label: '<90 %' },
        { value: '>90 %', label: '>90 %' },
        { value: '>95 %', label: '>95 %' },
        { value: '>99 %', label: '>99 %' },
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
                    tooltip='The method that was used to determine the purity'
                />
            </div>
            <div>                
                <OptionField
                    name={name}
                    fieldName='purity_percentage'
                    label='Purity percentage'
                    options={purityPercentageOptions}
                    tooltip='The obtained purity (in percent)'
                />
            </div>
        </div>
    </>
  );
}

export default PurityYes;
