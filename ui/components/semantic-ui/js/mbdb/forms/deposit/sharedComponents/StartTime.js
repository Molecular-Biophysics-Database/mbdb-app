import FormWrapper from "../buildingBlocks/FormWrapper";
import ValueUnit from "../buildingBlocks/ValueUnit";

function StartTime( { colorSchema, name } ) {

    const unitOptions = [
      { value: 'nanoseconds', label: 'nanoseconds' },
      { value: 'microseconds', label: 'microseconds' },
      { value: 'milliseconds', label: 'milliseconds' },
      { value: 'seconds', label: 'seconds' },
      { value: 'minutes', label: 'minutes' },
      { value: 'hours', label: 'hours' },
      { value: 'days', label: 'days' },
      { value: 'months', label: 'months' },
      { value: 'years', label: 'years' },
    ];

  return (
    <>
      <FormWrapper
        colorSchema={colorSchema}
        headline='Start time'
        tooltip='The numerical value of the start point of the measurement step relative to the beginning of the measurement in the units defined in the general parameters'>
          <ValueUnit
            options={unitOptions}
            name={name}
            tooltipValue='The numerical value of the time point or duration'
            tooltipUnit='The unit of the time duration'
          />
      </FormWrapper>
    </>
  );
}

export default StartTime;