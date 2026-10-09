import React from "react";
import { ComplexSubstanceOfChemicalOriginFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfChemicalOrigin";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => (
  <ComplexSubstanceOfChemicalOriginFields fieldPath={ENTITY_PATH} />
);

const FILLED = {
  name: "POPC liposomes",
  assembly_type: "Liposome",
  number_of_mono_layers: 2,
  size: { type: "diameter", unit: "nm", mean: 120, lower: 90, upper: 150 },
  components: [{ type: "Chemical", name: "POPC", copy_number: 120 }],
  preparation_protocol: [
    { name: "Extrusion", description: "21 passes through a 100 nm membrane" },
  ],
};

const story = {
  review: "entity",
  title: "ComplexSubstanceOfChemicalOrigin",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues(
        "Complex substance of chemical origin",
        {},
        { class: "Lipid assembly" }
      ),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: entityValues(
        "Complex substance of chemical origin",
        FILLED,
        { class: "Lipid assembly" }
      ),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues(
        "Complex substance of chemical origin",
        { name: "POPC liposomes" },
        { class: "Lipid assembly" }
      ),
      initialErrors: entityErrors(
        "assembly_type",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
