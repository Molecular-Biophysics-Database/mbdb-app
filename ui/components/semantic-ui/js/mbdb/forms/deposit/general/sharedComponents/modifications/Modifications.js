import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import Modification from "./Modification";
import FormWrapper from "../../../buildingBlocks/FormWrapper";

function Modifications({ name, colorSchema }) {
  return (
    <>
      <FormWrapper
        headline="Modifications"
        colorSchema={colorSchema}
        tooltip="If the polymer contains modifications such as non-natural amino acids, post-translational modification, or chemical modifications like labeling, it can be specified here"
      >
        <div className="-mt-3">
          <ArrayField
            name={name}
            label="Biological postprocessing"
            fieldName="biological_postprocessing"
            tooltip="Modifications of the polymer after its synthesis (e.g. post-translational modifications and DNA methylation) by the organism where the synthesis occurred"
            renderChild={({ arrayName, index }) => (
              <FormWrapper
                colorSchema={colorSchema === "light" ? "" : "light"}
                headline={`Biological postprocessing ${index + 1}`}
                tooltip="Modifications of the polymer after its synthesis (e.g. post-translational modifications and DNA methylation) by the organism where the synthesis occurred"
              >
                <Modification
                  name={`${arrayName}.${index}`}
                  colorSchema={colorSchema === "light" ? "light" : ""}
                />
              </FormWrapper>
            )}
          />
        </div>
        <div>
          <ArrayField
            name={name}
            label="Chemical"
            fieldName="chemical"
            tooltip="Modifications of the polymer introduced by chemical, biochemical, or physical means in vitro (e.g. lysine methylation, cysteine iodoacetamide labeling, deglycosylation, covalent fluorescent labeling)"
            renderChild={({ arrayName, index }) => (
              <FormWrapper
                colorSchema={colorSchema === "light" ? "" : "light"}
                headline={`Chemical ${index + 1}`}
                tooltip="Modifications of the polymer introduced by chemical, biochemical, or physical means in vitro (e.g. lysine methylation, cysteine iodoacetamide labeling, deglycosylation, covalent fluorescent labeling)"
              >
                <Modification
                  name={`${arrayName}.${index}`}
                  colorSchema={colorSchema === "light" ? "light" : ""}
                />
              </FormWrapper>
            )}
          />
        </div>
      </FormWrapper>
    </>
  );
}

export default Modifications;
