import React from "react";
import { Table } from "mbdb-semantic-ui-react";
import { SummaryItem } from "@js/mbdb/forms/building-blocks/SummaryItem";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import { POLYMER_GROUPS } from "./DetailView.story";

const BASE = "metadata.general_parameters.entities_of_interest.0";

const Rows = () => (
  <Table celled compact>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell collapsing />
        <Table.HeaderCell>Name</Table.HeaderCell>
        <Table.HeaderCell>Type</Table.HeaderCell>
        <Table.HeaderCell>Details</Table.HeaderCell>
        <Table.HeaderCell collapsing />
      </Table.Row>
    </Table.Header>
    <Table.Body>
      <SummaryItem
        fieldPath={BASE}
        itemName="Lysozyme"
        columns={[
          (v) => v?.name,
          (v) => v?.type,
          (v) =>
            [
              v?.polymer_type,
              v?.molecular_weight &&
                `${v.molecular_weight.value} ${v.molecular_weight.unit}`,
            ]
              .filter(Boolean)
              .join(", "),
        ]}
        onEdit={() =>
          window.alert("Edit clicked (owns the modal in ModalArrayField)")
        }
        onRemove={() => {}}
        detail={
          <DetailView
            fieldPath={BASE}
            groups={POLYMER_GROUPS}
            exclude={["name", "type"]}
          />
        }
      />
    </Table.Body>
  </Table>
);

const story = {
  title: "SummaryItem",
  scenarios: [
    {
      name: "Filled",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                name: "Lysozyme",
                type: "Polymer",
                polymer_type: "polypeptide(L)",
                molecular_weight: { value: 14.3, unit: "kDa" },
              },
            ],
          },
        },
      },
      render: Rows,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ name: "Lysozyme", type: "Polymer" }],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                polymer_type: "Missing data for required field.",
                sequence: "Unknown residue at position 7.",
              },
            ],
          },
        },
      },
      render: Rows,
    },
  ],
};

export default story;
