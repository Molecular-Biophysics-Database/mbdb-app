import React from "react";
import { VirionFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfBiologicalOrigin";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <VirionFields fieldPath={ENTITY_PATH} />;

const values = (fields) =>
  entityValues("Complex substance of biological origin", fields, {
    derived_from: "Virion",
  });

const story = {
  title: "Virion",
  scenarios: [
    { name: "Empty", initialValues: values({}), render: Fields },
    {
      name: "Filled",
      initialValues: values({
        genetic_material: "Virus genome",
        capsid_type: "Native",
        envelope_type: "None",
        host_organism: { id: "taxid:9606" },
        host_cell_type: "macrophage",
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: values({ capsid_type: "Native" }),
      initialErrors: entityErrors(
        "genetic_material",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
