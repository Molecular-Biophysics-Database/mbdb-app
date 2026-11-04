import React from "react";
import { ChemicalFields } from "@js/mbdb/forms/entities/Chemical";
import { ENTITY_PATH, entityErrors, entityValues } from "../fixtures";

const Fields = () => <ChemicalFields fieldPath={ENTITY_PATH} />;

const story = {
  review: "entity",
  title: "Chemical",
  scenarios: [
    { name: "Empty", initialValues: entityValues("Chemical"), render: Fields },
    {
      name: "Filled",
      // the chemical from draft gvfzs-t5060
      initialValues: entityValues("Chemical", {
        name: "Water",
        basic_information: { id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" },
        additional_specifications: ["HPLC grade"],
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Chemical", { name: "Water" }),
      initialErrors: entityErrors(
        "basic_information",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
