import React from "react";
import OptionField from "../buildingBlocks/OptionField";
import Concentration from "../components/Concentration";
import { useFormikContext, getIn } from 'formik';

function Ligand( { name } ) {

  const { values } = useFormikContext()
      
  const entitiesValue = getIn(values, `metadata.general_parameters.entities_of_interest`)

  let entityOptions = [];

  if (entitiesValue && entitiesValue.length > 0) {
        entityOptions = entitiesValue.map(entity => ({
            value: entity.name,
            label: entity.name,
        }));
    } else {
        entityOptions = [{ label: 'Select Entity, if applicable' }];
    }

  return (
    <>
        <div className="flex">
          <div className="mr-3">
            <OptionField
                name={name}
                options={entityOptions}
                label='Entity'
                fieldName='entity'
            />
          </div>
          <div>
            <Concentration
                name={`${name}.concentration`}
                colorSchema='light'
                tooltipHeader='Concentration of the entity'
            />
          </div>
        </div>
    </>
  );
}

export default Ligand;