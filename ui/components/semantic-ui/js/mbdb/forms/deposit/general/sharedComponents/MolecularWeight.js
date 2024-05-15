import FormWrapper from '../../buildingBlocks/FormWrapper';
import ValueUnit from '../../buildingBlocks/ValueUnit';

function MolecularWeight( { colorSchema, name, tooltip } ) {

    const unitOptions = [
      { value: 'g / mol', label: 'g / mol' },
      { value: 'Da', label: 'Da' },
      { value: 'kDa', label: 'kDa' },
      { value: 'MDa', label: 'MDa' },
    ];

  return (
    <>
      <FormWrapper colorSchema={colorSchema} headline='Molecular weight' tooltip={tooltip}>
          <ValueUnit
            options={unitOptions}
            name={name}
            tooltipValue='The numerical value of the molecular weight'
            tooltipUnit='The unit of the molecular weight'
          />
      </FormWrapper>
    </>
  );
}

export default MolecularWeight;