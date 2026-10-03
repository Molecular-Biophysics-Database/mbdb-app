import React from "react";
import { PolymerFields } from "@js/mbdb/forms/entities/Polymer";
import { entityErrors, entityPath, entityValues } from "../fixtures";

// A Polymer component: the same field set as the Polymer entity, rendered at a
// component item path. There is no ComponentPolymer component; this story
// inspects the shared PolymerFields in a component context.
const PATH = entityPath("components.0");

const Fields = () => <PolymerFields fieldPath={PATH} />;

const component = (fields) =>
  entityValues("Molecular assembly", {
    components: [
      {
        type: "Polymer",
        name: "RNA polymerase alpha subunit",
        copy_number: 2,
        ...fields,
      },
    ],
  });

const story = {
  title: "Component: Polymer",
  scenarios: [
    { name: "Empty", initialValues: component({}), render: Fields },
    {
      name: "Filled",
      initialValues: component({
        polymer_type: "polypeptide(L)",
        expression_source_type: "Recombinantly",
        molecular_weight: { value: 34.8, unit: "kDa" },
        external_databases: ["uniprot:P20429"],
        source_organism: { id: "taxid:1423" },
        expression_organism: { id: "taxid:469008" },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: component({}),
      initialErrors: entityErrors(
        "components.0.polymer_type",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
