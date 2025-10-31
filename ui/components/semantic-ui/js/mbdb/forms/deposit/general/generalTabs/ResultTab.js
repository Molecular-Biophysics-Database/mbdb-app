import React from "react";
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
import DynamicOptionField from "../../buildingBlocks/DynamicOptionField";
import CorrectionOfActiveConcentration from "../result/CorrectionOfActiveConcentration";
import SizeSphericalRepresentation from "../result/SizeSphericalRepresentation";

function ResultTab({ name }) {
  const { values } = useFormikContext();

  const tooltip =
    "List of the results (parameters) that were derived by analyzing the raw data and which steps were taken to obtain them";

  const resultTabOptions = [
    { value: "Concentration", label: "Concentration" },
    { value: "Stoichiometry", label: "Stoichiometry" },
    {
      value: "Constant of association KA",
      label: "Constant of association KA",
    },
    {
      value: "Constant of dissociation KD",
      label: "Constant of dissociation KD",
    },
    { value: "Association rate kOn", label: "Association rate kOn" },
    { value: "Dissociation rate kOff", label: "Dissociation rate kOff" },
    { value: "Change in enthalpy deltaH", label: "Change in enthalpy deltaH" },
    { value: "Change in entropy deltaS", label: "Change in entropy deltaS" },
    {
      value: "Change in gibbs free energy deltaG",
      label: "Change in Gibbs free energy deltaG",
    },
    { value: "Molecular weight", label: "Molecular weight" },
    {
      value: "Half maximal effective concentration EC50",
      label: "Half maximal effective concentration EC50",
    },
    { value: "Hill coefficient", label: "Hill coefficient" },
    {
      value: "Correction of active concentration",
      label: "Correction of active concentration",
    },
    {
      value: "Size of spherically represented entity",
      label: "Size of spherically represented entity",
    },
  ];

  return (
    <>
      <div className="mb-3 w-fit">
        <FormWrapper>
          The results derived from the measurements (e.g. MW)
        </FormWrapper>
      </div>
      <ArrayField
        name={name}
        label="Result"
        fieldName="results"
        initialValue={{ type: "Concentration" }}
        tooltip={tooltip}
        renderChild={({ arrayName, index }) => {
          const actualValue = getIn(values, `${arrayName}.${index}`);
          if (!actualValue) {
            return null;
          }
          return (
            <FormWrapper headline={`Result ${index + 1}`} tooltip={tooltip}>
              <div className="mb-3">
                <DynamicOptionField
                  name={`${arrayName}.${index}`}
                  options={resultTabOptions}
                  label="Type"
                  required
                  fieldName="type"
                  width="w-full"
                  tooltip="The type of physical parameter the result represents"
                />
              </div>
              <div>
                {actualValue.type === "Concentration" && (
                  <Concentration name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Stoichiometry" && (
                  <Stoichiometry name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Constant of association KA" && (
                  <ConstantOfAssociationKA name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Constant of dissociation KD" && (
                  <ConstantOfDissociationKD name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Association rate kOn" && (
                  <AssociationRateKOn name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Dissociation rate kOff" && (
                  <DissociationRateKOff name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Change in enthalpy deltaH" && (
                  <ChangeInEnthalpyDeltaH name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Change in entropy deltaS" && (
                  <ChangeInEntropyDeltaS name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Change in gibbs free energy deltaG" && (
                  <ChangeInGibbsFreeEnergyDeltaG
                    name={`${arrayName}.${index}`}
                  />
                )}
                {actualValue.type === "Molecular weight" && (
                  <MolecularWeightMW name={`${arrayName}.${index}`} />
                )}
                {actualValue.type ===
                  "Half maximal effective concentration EC50" && (
                  <HalfMaximalEffectiveConcentrationEC50
                    name={`${arrayName}.${index}`}
                  />
                )}
                {actualValue.type === "Hill coefficient" && (
                  <HillCoefficient name={`${arrayName}.${index}`} />
                )}
                {actualValue.type === "Correction of active concentration" && (
                  <CorrectionOfActiveConcentration
                    name={`${arrayName}.${index}`}
                  />
                )}
                {actualValue.type === "Size of spherically represented entity" && (
                  <SizeSphericalRepresentation name={`${arrayName}.${index}`} />
                )}
              </div>
            </FormWrapper>
          );
        }}
      />
    </>
  );
}

export default ResultTab;
