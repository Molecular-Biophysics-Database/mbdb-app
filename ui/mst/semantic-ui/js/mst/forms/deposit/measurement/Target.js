import OptionField from "@mbdb_deposit/buildingBlocks/OptionField";
import Concentration from "@mbdb_deposit/sharedComponents/Concentration";
import { useFormikContext, getIn } from 'formik';
import CreateOptions from "@mbdb_deposit/buildingBlocks/CreateOptions";

function Target( { name } ) {

  const { values } = useFormikContext();
    
  const entitiesValue = getIn(values, `metadata.general_parameters.entities_of_interest`);
  const entityOptions = CreateOptions(entitiesValue, 'Select Entity, if applicable');

  return (
    <>
      <div className="flex">
        <div className="mr-3">
          <OptionField
              name={name}
              options={entityOptions}
              label='Entity'
              fieldName='entity'
              tooltip='List of names (ids), from the entities of interest defined in the general parameters, of directly measured entities'
          />
        </div>
        <div>
          <Concentration
              name={`${name}.concentration`}
              colorSchema='light'
              tooltip='Concentration of the entity'
          />
        </div>
      </div>
    </>
  );
}

export default Target;