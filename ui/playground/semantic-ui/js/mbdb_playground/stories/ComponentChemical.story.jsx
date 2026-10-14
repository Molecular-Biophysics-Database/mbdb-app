import React from "react";
import { ChemicalFields } from "@js/mbdb/forms/entities/Chemical";
import { entityErrors, entityPath, entityValues } from "../fixtures";

// A Chemical component: the same field set as the Chemical entity, rendered at
// a component item path. There is no ComponentChemical component; this story
// inspects the shared ChemicalFields in a component context.
const PATH = entityPath("components.0");

const Fields = () => <ChemicalFields fieldPath={PATH} />;

const component = (fields) =>
  entityValues("Molecular assembly", {
    components: [
      { type: "Chemical", name: "Water", copy_number: -1, ...fields },
    ],
  });

const story = {
  title: "Component: Chemical",
  scenarios: [
    { name: "Empty", initialValues: component({}), render: Fields },
    {
      name: "Filled",
      initialValues: component({
        basic_information: { id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N" },
        additional_specifications: ["HPLC grade"],
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: component({}),
      initialErrors: entityErrors(
        "components.0.basic_information",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
