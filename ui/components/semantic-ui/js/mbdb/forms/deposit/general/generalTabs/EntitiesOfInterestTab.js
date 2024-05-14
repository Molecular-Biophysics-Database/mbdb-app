import FormWrapper from "../../buildingBlocks/FormWrapper";
import Chemical from "../entitiesOfInterest/Chemical";
import Polymer from "../entitiesOfInterest/Polymer";
import UseDefault from "../../buildingBlocks/UseDefault";
import ComplexSubstanceOfBiologicalOrigin from "../entitiesOfInterest/ComplexSubstanceOfBiologicalOrigin";
import MolecularAssembly from "../entitiesOfInterest/MolecularAssembly";
import ComplexSubstanceOfIndustrialOrigin from "../entitiesOfInterest/ComplexSubstanceOfIndustrialOrigin";
import ComplexSubstanceOfEnvironmentalOrigin from "../entitiesOfInterest/ComplexSubstanceOfEnvironmentalOrigin";
import ComplexSubstanceOfChemicalOrigin from "../entitiesOfInterest/ComplexSubstanceOfChemicalOrigin";
import ArrayField from "../../buildingBlocks/ArrayField";
import { getIn, useFormikContext } from "formik";
import OptionField from "../../buildingBlocks/OptionField";

function EntitiesOfInterestTab( { name } ) {

    const { values } = useFormikContext();

    const componentName = `${name}.entities_of_interest[0].type`;
   
    UseDefault(componentName, 'Polymer');

    const entitiesOfInterestTabOptions = [
        { value: 'Polymer', label: 'Polymer' },
        { value: 'Chemical', label: 'Chemical' },
        { value: 'Molecular assembly', label: 'Molecular assembly' },
        { value: 'Complex substance of biological origin', label: 'Complex substance of biological origin' },
        { value: 'Complex substance of environmental origin', label: 'Complex substance of environmental origin' },
        { value: 'Complex substance of chemical origin', label: 'Complex substance of chemical origin' },
        { value: 'Complex substance of industrial origin', label: 'Complex substance of industrial origin' },
    ];

    return (
      <>
        <div className="-mt-3">
            <ArrayField
                name={name}
                label="Entity of interest"
                fieldName='entities_of_interest'
                initialValue={{type: 'Polymer'}}
                required={true}
                tooltip='List of the entities that are being directly measured, as well as the entities that are being used as a variable to influence the behavior of the directly measured entities (e.g. lysozyme, NAG3,NaCl). IMPORTANT! If the pH was varied by individually prepared chemical environments these should be specified individually in chemical environments'
                renderChild={({ arrayName, index }) =>  {
                    const actualValue = getIn(values, `${arrayName}.${index}`)
                    if (!actualValue) {return null}
                    return (
                    <FormWrapper 
                        headline={`Entity of interest ${index + 1}`} 
                        tooltip='List of the entities that are being directly measured, as well as the entities that are being used as a variable to influence the behavior of the directly measured entities (e.g. lysozyme, NAG3,NaCl). IMPORTANT! If the pH was varied by individually prepared chemical environments these should be specified individually in chemical environments'
                    >
                        <div className="mb-3">
                            <OptionField
                                name={`${arrayName}.${index}`}
                                options={entitiesOfInterestTabOptions}
                                label='type'
                                fieldName='type'
                                width='w-full'
                                tooltip='The type of the entity, where the options are (biological) Polymer, Chemical, Molecular assembly (also includes all proteins composed of more than one polypeptide chain) or Complex substance. Chemical polymers such as PEG 5000 should be described as being a Chemical. Complex substance refers to substances which are not exactly specified by their exact chemical composition by the time measurement were performed, but e.g. blood, serum, plant extract'
                            />
                        </div>
                        <div>
                            {actualValue.type === 'Polymer' && (
                                <div>
                                    <Polymer
                                        name={`${arrayName}.${index}`}
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
                            {actualValue.type === 'Molecular assembly' && (
                                <div>
                                    <MolecularAssembly
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Complex substance of biological origin' && (
                                <div>
                                    <ComplexSubstanceOfBiologicalOrigin
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Complex substance of environmental origin' && (
                                <div>
                                    <ComplexSubstanceOfEnvironmentalOrigin
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Complex substance of chemical origin' && (
                                <div>
                                    <ComplexSubstanceOfChemicalOrigin
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Complex substance of industrial origin' && (
                                <div>
                                    <ComplexSubstanceOfIndustrialOrigin
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                        </div>
                    </FormWrapper>
                )}}
            />
        </div>
      </>
    );
  }
  
  export default EntitiesOfInterestTab;