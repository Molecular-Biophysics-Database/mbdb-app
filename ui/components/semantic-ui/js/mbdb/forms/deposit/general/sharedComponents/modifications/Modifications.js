import React from "react";
import ArrayField from "../../../buildingBlocks/ArrayField";
import Modification from "./Modification";
import FormWrapper from "../../../buildingBlocks/FormWrapper";

export default function Modifications({ name, colorSchema }) {
  const tooltips = {
    biologicalPostprocessing:
      "Modifications of the polymer after its synthesis (e.g. post-translational modifications and DNA methylation) by the organism where the synthesis occurred",
    chemical:
      "Modifications of the polymer introduced by chemical, biochemical, or physical means in vitro (e.g. lysine methylation, cysteine iodoacetamide labeling, deglycosylation, covalent fluorescent labeling)",
  };

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
            tooltip={tooltips.biologicalPostprocessing}
            renderChild={({ arrayName, index }) => (
              <FormWrapper
                colorSchema={colorSchema === "light" ? "" : "light"}
                headline={`Biological postprocessing ${index + 1}`}
                tooltip={tooltips.biologicalPostprocessing}
              >
                <Modification
                  name={`${arrayName}.${index}`}
                  colorSchema={colorSchema === "light" ? "light" : ""}
                />
              </FormWrapper>
            )}
          />
        </div>

        <ArrayField
          name={name}
          label="Chemical"
          fieldName="chemical"
          tooltip={tooltips.chemical}
          renderChild={({ arrayName, index }) => (
            <FormWrapper
              colorSchema={colorSchema === "light" ? "" : "light"}
              headline={`Chemical ${index + 1}`}
              tooltip={tooltips.chemical}
            >
              <Modification
                name={`${arrayName}.${index}`}
                colorSchema={colorSchema === "light" ? "light" : ""}
              />
            </FormWrapper>
          )}
        />
      </FormWrapper>
    </>
  );
}
