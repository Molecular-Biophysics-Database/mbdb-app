import React from 'react';
import FormWrapper from '../buildingBlocks/FormWrapper';
import ValueUnit from '../buildingBlocks/ValueUnit';

function MolecularWeight( {colorSchema, name, tooltipHeader} ) {

    const unitOptions = [
        { value: 'g / mol', label: 'g / mol' },
        { value: 'Da', label: 'Da' },
        { value: 'kDa', label: 'kDa' },
        { value: 'MDa', label: 'MDa' },
      ];

  return (
    <>
      <FormWrapper colorSchema={colorSchema} headline='Molecular weight' tooltipHeader={tooltipHeader}>
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