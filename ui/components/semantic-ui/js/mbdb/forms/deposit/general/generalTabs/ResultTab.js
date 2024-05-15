import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import Concentration from "../result/Concentration";
import Stoichiometry from "../result/Stoichiometry";
import ConstantOfAssociationKA from "../result/ConstantOfAssociationKA";
import ConstantOfDissociationKD from "../result/ConstantOfDissociationKD";
import AssociationRateKOn from "../result/AssociationRateKOn";
import DissociationRateKOff from "../result/DissociationRateKOff";
import ChangeInEnthalpyDeltaH from "../result/ChangeInEnthalpyDeltaH";
import ChangeInEntropyDeltaS from "../result/ChangeInEntropyDeltaS";
import MolecularWeightMW from "../result/MolecularWeightMW";
import HalfMaximalEffectiveConcentrationEC50 from "../result/HalfMaximalEffectiveConcentrationEC50";
import HillCoefficient from "../result/HillCoefficient";
import { getIn, useFormikContext } from "formik";
import ChangeInGibbsFreeEnergyDeltaG from "../result/ChangeInGibbsFreeEnergyDeltaG";
import OptionField from "../../buildingBlocks/OptionField";

function ResultTab( { name } ) {

    const { values } = useFormikContext();

    const resultTabOptions = [
        { value: 'Concentration', label: 'Concentration' },
        { value: 'Stoichiometry', label: 'Stoichiometry' },
        { value: 'Constant of association KA', label: 'Constant of association KA' },
        { value: 'Constant of dissociation KD', label: 'Constant of dissociation KD' },
        { value: 'Association rate kOn', label: 'Association rate kOn' },
        { value: 'Dissociation rate kOff', label: 'Dissociation rate kOff' },
        { value: 'Change in enthalpy deltaH', label: 'Change in enthalpy deltaH' },
        { value: 'Change in entropy deltaS', label: 'Change in entropy deltaS' },
        { value: 'Change in gibbs free energy deltaG', label: 'Change in Gibbs free energy deltaG' },
        { value: 'Molecular weight MW', label: 'Molecular weight MW' },
        { value: 'Half maximal effective concentration EC50', label: 'Half maximal effective concentration EC50' },
        { value: 'Hill coefficient', label: 'Hill coefficient' },
    ];

    return (
      <>
        <div className="-mt-3">
            <ArrayField 
                name={name}
                label="Result"
                fieldName='results'
                initialValue={{type: 'Concentration'}}
                tooltip='List of the results (parameter) that were derived by analyzing the raw data and which steps were taken to obtain them'
                renderChild={({ arrayName, index }) => {
                    const actualValue = getIn(values, `${arrayName}.${index}`)
                    if (!actualValue) {return null}
                    return (
                    <FormWrapper
                        headline={`Result ${index + 1}`}
                        tooltip='List of the results (parameter) that were derived by analyzing the raw data and which steps were taken to obtain them'
                    >
                        <div className="mb-3">
                            <OptionField
                                name={`${arrayName}.${index}`}
                                options={resultTabOptions}
                                label='Type'
                                fieldName='type'
                                width='w-full'
                                tooltip='The type of physical parameter the result represents'
                            />
                        </div>
                        <div>
                            {actualValue.type === 'Concentration' && (
                                <div>
                                    <Concentration
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Stoichiometry' && (
                                <div>
                                    <Stoichiometry
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Constant of association KA' && (
                                <div>
                                    <ConstantOfAssociationKA
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Constant of dissociation KD' && (
                                <div>
                                    <ConstantOfDissociationKD
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Association rate kOn' && (
                                <div>
                                    <AssociationRateKOn
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Dissociation rate kOff' && (
                                <div>
                                    <DissociationRateKOff
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Change in enthalpy deltaH' && (
                                <div>
                                    <ChangeInEnthalpyDeltaH
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Change in entropy deltaS' && (
                                <div>
                                    <ChangeInEntropyDeltaS
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Change in gibbs free energy deltaG' && (
                                <div>
                                    <ChangeInGibbsFreeEnergyDeltaG
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Molecular weight MW' && (
                                <div>
                                    <MolecularWeightMW
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Half maximal effective concentration EC50' && (
                                <div>
                                    <HalfMaximalEffectiveConcentrationEC50
                                        name={`${arrayName}.${index}`}
                                    />
                                </div>
                            )}
                            {actualValue.type === 'Hill coefficient' && (
                                <div>
                                    <HillCoefficient
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
  
  export default ResultTab;