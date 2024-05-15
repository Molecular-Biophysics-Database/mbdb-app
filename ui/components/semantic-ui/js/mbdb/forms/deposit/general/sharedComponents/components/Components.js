import FormWrapper from "../../../buildingBlocks/FormWrapper";
import UseDefault from "../../../buildingBlocks/UseDefault";
import Polymer from "./Polymer";
import { getIn, useFormikContext } from "formik";
import ArrayField from "../../../buildingBlocks/ArrayField";
import OptionField from "../../../buildingBlocks/OptionField";
import Chemical from "./Chemical";

function Components( { name, colorSchema, tooltip } ) {

    const { values } = useFormikContext();

    const componentName = `${name}.components[0].type`;
   
    UseDefault(componentName, 'Polymer');

    const componentOptions = [
        { value: 'Polymer', label: 'Polymer' },
        { value: 'Chemical', label: 'Chemical' },
    ];

    return (
      <>
        <div>
            <ArrayField
                name={name}
                label="Component"
                fieldName='components'
                required={true}
                initialValue={{type: 'Polymer'}}
                tooltip={tooltip}
                renderChild={({ arrayName, index }) => {
                    const actualValue = getIn(values, `${arrayName}.${index}`)
                    if (!actualValue) {return null}
                    return (
                        <div>
                            <FormWrapper headline={`Component ${index + 1}`} tooltip={tooltip} colorSchema={colorSchema}>
                                <div className="mb-3">
                                    <OptionField
                                        name={`${arrayName}.${index}`}
                                        options={componentOptions}
                                        label='type'
                                        fieldName='type'
                                        width='w-full'
                                        tooltip='The type of component, options are
                                        (biological) Polymer and Chemical'
                                    />
                                </div>
                                <div>
                                    {actualValue.type === 'Polymer' && (
                                        <div>
                                            <Polymer
                                                name={`${arrayName}.${index}`}
                                                colorSchema={colorSchema === 'light' ? '' : 'light'}
                                            />
                                        </div>
                                    )}
                                    {actualValue.type === 'Chemical' && (
                                        <div>
                                            <Chemical
                                                name={`${arrayName}.${index}`}
                                            />
                                        </div>
                                    )}
                                </div>
                            </FormWrapper>
                        </div>
                )}}
            />
        </div>
      </>
    );
  }
  
  export default Components;