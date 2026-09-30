import React from "react";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import { Header } from "mbdb-semantic-ui-react";

const BASE = "metadata.general_parameters.entities_of_interest.0";

// Declared next to the block in real usage; the form's FieldGroups and the
// details both use it (design/building-blocks/DetailView.md §2).
export const POLYMER_GROUPS = [
  {
    title: "Identification",
    fields: ["polymer_type", "expression_source_type", "variant"],
  },
  { title: "Sequence", fields: ["sequence"] },
  { title: "Origin", fields: ["source_organism", "expression_organism"] },
  {
    title: "Molecular data",
    fields: ["molecular_weight", "additional_specifications"],
  },
];

const Details = () => (
  <>
    <Header size="small">
      Read-only details of the entity below (expand ▸ in SummaryItem /
      ModalArrayField stories to see it inline)
    </Header>
    <DetailView
      fieldPath={BASE}
      groups={POLYMER_GROUPS}
      exclude={["name", "type"]}
    />
  </>
);

const story = {
  title: "DetailView",
  scenarios: [
    {
      name: "Empty object",
      initialValues: {
        metadata: { general_parameters: { entities_of_interest: [{}] } },
      },
      render: Details,
    },
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                name: "RNA polymerase alpha subunit",
                type: "Polymer",
                polymer_type: "polypeptide(L)",
                expression_source_type: "Recombinantly",
                sequence:
                  "MIEIEKPKIETVEISDDAKFGKFVVEPLERGYGTTLGNSLRRILLSSLPGAAVRNLQRALTGDDVEVTVQVKGVTLSLALLDVVQQLRVR",
                source_organism: { id: "taxid:1423" },
                molecular_weight: { value: 34.8, unit: "kDa" },
                additional_specifications: ["RNase-free water", "desalted"],
              },
            ],
          },
        },
      },
      render: Details,
    },
    {
      name: "Missing + errors",
      initialValues: {
        metadata: {
          general_parameters: { entities_of_interest: [{ type: "Polymer" }] },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { polymer_type: "Missing data for required field." },
            ],
          },
        },
      },
      render: () => (
        <DetailView
          fieldPath={BASE}
          groups={POLYMER_GROUPS}
          exclude={["name", "type"]}
          requiredPaths={["polymer_type"]}
        />
      ),
    },
  ],
};

export default story;
