import React from "react";
import { BodyFluidFields } from "@js/mbdb/forms/entities/ComplexSubstanceOfBiologicalOrigin";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <BodyFluidFields fieldPath={ENTITY_PATH} />;

const values = (fields) =>
  entityValues("Complex substance of biological origin", fields, {
    derived_from: "Body fluid",
  });

const story = {
  title: "BodyFluid",
  scenarios: [
    { name: "Empty", initialValues: values({}), render: Fields },
    {
      name: "Filled",
      initialValues: values({
        fluid: { id: "bf:2" },
        health_status: "Healthy",
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: values({ health_status: "Healthy" }),
      initialErrors: entityErrors("fluid", "Missing data for required field."),
      render: Fields,
    },
  ],
};

export default story;
