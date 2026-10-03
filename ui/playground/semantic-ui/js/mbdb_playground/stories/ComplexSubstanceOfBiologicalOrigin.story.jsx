import React from "react";
import { ComplexSubstanceOfBiologicalOriginFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfBiologicalOrigin";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => (
  <ComplexSubstanceOfBiologicalOriginFields fieldPath={ENTITY_PATH} />
);

// One scenario per sub-type (design ComplexSubstanceOfBiologicalOrigin). The
// "Human serum" fixture is the sample record (draft gvfzs-t5060).
const BIOLOGICAL = "Complex substance of biological origin";
const values = (fields, derivedFrom) =>
  entityValues(BIOLOGICAL, fields, { derived_from: derivedFrom });

const story = {
  title: "ComplexSubstanceOfBiologicalOrigin",
  scenarios: [
    { name: "Empty", initialValues: entityValues(BIOLOGICAL), render: Fields },
    {
      name: "Body fluid",
      initialValues: values(
        {
          name: "Human serum",
          source_organism: { id: "taxid:9606" },
          fluid: { id: "bf:2" },
          health_status: "Healthy",
          preparation_protocol: [
            {
              name: "Centrifugation",
              description:
                "Tubes were centrifuged for 10 min at 1,300g at 4°C within 2 hours of collection",
            },
            {
              name: "Aliquotation",
              description:
                "The supernatant was distributed among 0.5 mL cryostorage tubes",
            },
          ],
          storage: { temperature: { value: -80.0, unit: "°C" } },
          additional_specifications: [
            "Blood was drawn after 12 hours of fasting",
          ],
        },
        "Body fluid"
      ),
      render: Fields,
    },
    {
      name: "Cell fraction",
      initialValues: values(
        {
          name: "Liver ribosomes",
          source_organism: { id: "taxid:9606" },
          fraction: { id: "cf:1" },
          health_status: "healthy",
          organ: "liver",
          preparation_protocol: [
            { name: "Ultracentrifugation", description: "100,000 g, 2 h" },
          ],
        },
        "Cell fraction"
      ),
      render: Fields,
    },
    {
      name: "Virion",
      initialValues: values(
        {
          name: "AAV2 particles",
          source_organism: { id: "taxid:9606" },
          genetic_material: "Virus genome",
          capsid_type: "Native",
          envelope_type: "None",
          preparation_protocol: [
            { name: "Purification", description: "Iodixanol gradient" },
          ],
        },
        "Virion"
      ),
      render: Fields,
    },
    {
      name: "Solid tissue sample",
      initialValues: values(
        {
          name: "Liver biopsy",
          source_organism: { id: "taxid:9606" },
          organ: "liver",
          health_status: "healthy",
          homogenized: false,
          preparation_protocol: [
            {
              name: "Homogenization",
              description: "Not homogenized; cut into 1 mm slices",
            },
          ],
        },
        "Solid tissue sample"
      ),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: values({ name: "Human serum" }, "Body fluid"),
      initialErrors: entityErrors(
        "source_organism",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
