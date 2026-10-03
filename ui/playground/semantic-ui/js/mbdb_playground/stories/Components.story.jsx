import React from "react";
import { Components } from "@js/mbdb/forms/shared/Components";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const PATH = entityPath("components");

const Fields = () => <Components fieldPath={PATH} />;

// From sample record 6g5wd-zxy65 ("RNA polymerase"), two of its six
// components; vocabulary values reduced to { id } as the UI stores them.
const COMPONENTS = [
  {
    type: "Polymer",
    name: "RNA polymerase alpha subunit",
    copy_number: 2,
    polymer_type: "polypeptide(L)",
    expression_source_type: "Recombinantly",
    molecular_weight: { value: 34.8, unit: "kDa" },
    external_databases: ["uniprot:P20429"],
    source_organism: { id: "taxid:1423" },
    expression_organism: { id: "taxid:469008" },
  },
  {
    type: "Polymer",
    name: "RNA polymerase beta' subunit",
    copy_number: 1,
    polymer_type: "polypeptide(L)",
    expression_source_type: "Recombinantly",
    molecular_weight: { value: 135.35, unit: "kDa" },
    external_databases: ["uniprot:P37871"],
    variant: "C-terminal 8xHis tag",
  },
];

const ASSEMBLY = {
  name: "RNA polymerase",
  molecular_weight: { value: 375.7, unit: "kDa" },
  components: COMPONENTS,
};

const story = {
  title: "Components",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Molecular assembly", {
        name: "RNA polymerase",
      }),
      // an empty components list is always an error (required, minItems 1)
      initialErrors: entityErrors(
        "components",
        "Missing data for required field."
      ),
      render: Fields,
    },
    {
      name: "Filled",
      initialValues: entityValues("Molecular assembly", ASSEMBLY),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Molecular assembly", {
        ...ASSEMBLY,
        components: [
          ...COMPONENTS,
          { type: "Chemical", name: "Zn2+", copy_number: -1 },
        ],
      }),
      initialErrors: entityErrors(
        "components.2.basic_information",
        "Missing data for required field."
      ),
      render: Fields,
    },
    {
      name: "Chemical",
      initialValues: entityValues("Molecular assembly", {
        name: "RNA polymerase",
        components: [
          {
            type: "Chemical",
            name: "Water",
            copy_number: -1,
            basic_information: {
              id: "inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N",
            },
          },
        ],
      }),
      render: Fields,
    },
  ],
};

export default story;
