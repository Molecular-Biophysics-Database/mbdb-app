import CustomField from '../../buildingBlocks/CustomField';
import OptionField from '../../buildingBlocks/OptionField';
import { useFormikContext, getIn } from 'formik';
import CreateOptions from '../../buildingBlocks/CreateOptions';

function EntityInvolved( { name } ) {

    const { values } = useFormikContext();

    const entitiesValue = getIn(values, `metadata.general_parameters.entities_of_interest`);
    const entityOptions = CreateOptions(entitiesValue, 'Select Entity, if applicable');

  return (
    <>
        <div className='flex'>
            <div className="mr-3">
                <OptionField
                    name={name}
                    options={entityOptions}
                    fieldName='entity'
                    label='Entity'
                    tooltip='Name (ids) of the entity (from the entities of interest defined in the general parameters'
                />
            </div>
            <div>
                <CustomField
                    name={name}
                    fieldName='copy_number'
                    label='Copy number'
                    tooltip='Number of copies of the entity that contribute to the result, -1 if unknown (e.g. if two individual copies of a polymer binds to another, the copy number would be 2)'
                />
            </div>
        </div>
    </>
  );
}

export default EntityInvolved;
