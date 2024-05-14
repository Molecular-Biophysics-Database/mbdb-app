import { getIn, useFormikContext } from "formik";
import UseDefault from "../../buildingBlocks/UseDefault";
import BodyFluid from "./BodyFluid";
import CellFraction from "./CellFraction";
import Virion from "./Virion";
import OptionField from "../../buildingBlocks/OptionField";

function ComplexSubstanceOfBiologicalOrigin( { name } ) {

    const { values } = useFormikContext();

    const componentName = `${name}.derived_from`;
   
    UseDefault(componentName, 'Body fluid');

    const actualValue = getIn(values, componentName);

    const complexSubstanceOfBiologicalOriginOptions = [
        { value: 'Body fluid', label: 'Body fluid' },
        { value: 'Cell fraction', label: 'Cell fraction' },
        { value: 'Virion', label: 'Virion' },
    ];

  return (
    <>
        <div className="mb-3">
            <OptionField
                name={name}
                options={complexSubstanceOfBiologicalOriginOptions}
                label='Derived from'
                fieldName='derived_from'
                width='w-full'
                tooltip='The biological substance the complex substance is derived from'
            />
        </div>

        {actualValue === 'Body fluid' && (
            <>
                <BodyFluid name={name} />
            </>
        )}
        {actualValue === 'Cell fraction' && (
            <>
                <CellFraction name={name} />
            </>
        )}
        {actualValue === 'Virion' && (
            <>
                <Virion name={name} />
            </>
        )}
    </>
  );
}

export default ComplexSubstanceOfBiologicalOrigin;