import CustomField from "@mbdb_deposit/buildingBlocks/CustomField";
import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";

function FColdAndHot( { name } ) {

    const unitOptions = [
        { value: 'Nanoseconds', label: 'Nanoseconds' },
        { value: 'Microseconds', label: 'Microseconds' },
        { value: 'Milliseconds', label: 'Milliseconds' },
        { value: 'Seconds', label: 'Seconds' },
        { value: 'Minutes', label: 'Minutes' },
        { value: 'Gours', label: 'Hours' },
        { value: 'Days', label: 'Days' },
        { value: 'Months', label: 'Months' },
        { value: 'Years', label: 'Years' },
    ];

  return (
    <>
        <div className='mb-3'>
            <OptionField
                name={name}
                options={unitOptions}
                label='Time unit'
                fieldName='time_unit'
                tooltip='The unit of time used for reporting measurement data'
            />
        </div>
        <div className="flex mb-3">
            <div className="mr-3">
                <CustomField
                    name={name}
                    fieldName='f_cold_start'
                    label='F cold start'
                    type='number'
                    tooltip='Numerical value of the start-point of time interval used to establish the initial fluorescence, F_cold'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='f_cold_end'
                    label='F cold end'
                    type='number'
                    tooltip='Numerical value of the end-point of time interval used to establish the initial fluorescence, F_cold'
                />
            </div>                
        </div>
        <div className="flex">
            <div className="mr-3">
                <CustomField
                    name={name}
                    fieldName='f_hot_start'
                    label='F hot start'
                    type='number'
                    tooltip='Numerical value of the start-point of time interval used to establish the fluorescence temperature induced change in fluorescence, F_hot'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='f_hot_end'
                    label='F hot end'
                    type='number'
                    tooltip='Numerical value of the end-point of time interval used to establish the fluorescence temperature induced change in fluorescence, F_hot'
                />
            </div>                
        </div>
    </>
  );
}

export default FColdAndHot;