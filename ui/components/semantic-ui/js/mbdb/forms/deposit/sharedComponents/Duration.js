import ValueUnit from '../buildingBlocks/ValueUnit';
import FormWrapper from '../buildingBlocks/FormWrapper';

function Duration( {name, tooltip, colorSchema } ) {

    const unitOptions = [
        { value: 'miliseconds', label: 'miliseconds' },
        { value: 'seconds', label: 'seconds' },
        { value: 'minutes', label: 'minutes' },
        { value: 'hours', label: 'hours' },
        { value: 'days', label: 'days' },
        { value: 'months', label: 'months' },
        { value: 'years', label: 'years' },
      ];

  return (
    <>
        <FormWrapper colorSchema={colorSchema} headline='Duration' tooltip={tooltip}>
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

export default Duration;
