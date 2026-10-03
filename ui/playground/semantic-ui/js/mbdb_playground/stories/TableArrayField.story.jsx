import React from "react";
import PropTypes from "prop-types";
import { Divider } from "mbdb-semantic-ui-react";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";
import { ENTITY_PATH, entityValues, entityErrors } from "../fixtures";

const BASE = ENTITY_PATH;

const EXTERNAL_DB_REGEX = /^([^:]*):(.*)$/;

// external_databases is stored as an array of "prefix:id" strings; the story
// deserializes to a { database, id } row and writes back on every change.
const ExternalDatabases = ({ fieldPath }) => (
  <TableArrayField
    fieldPath={fieldPath}
    label="External databases"
    addButtonLabel="Add database"
    serialize={({ database = "", id = "" }) =>
      !database && !id ? "" : `${database}:${id}`
    }
    deserialize={(item) => {
      const m = EXTERNAL_DB_REGEX.exec(String(item ?? ""));
      return { database: m[1], id: m[2] };
    }}
    defaultNewValue=""
    rowHint={({ database, id }) =>
      (!database && id) || (database && !id) ? "Incomplete" : null
    }
    columns={[
      {
        field: "database",
        type: "select",
        options: ["pdb", "uniprot"],
        allowAdditions: true,
        width: 4,
      },
      { field: "id", label: "ID" },
    ]}
  />
);

ExternalDatabases.propTypes = { fieldPath: PropTypes.string.isRequired };

const Modifications = ({ fieldPath }) => (
  <TableArrayField
    fieldPath={fieldPath}
    label="Modifications"
    addButtonLabel="Add modification"
    renderExpanded={(itemPath) => (
      <TableArrayField
        fieldPath={`${itemPath}.protocol`}
        label="Protocol"
        addButtonLabel="Add step"
        columns={[
          { field: "name", width: 4 },
          { field: "description", type: "textarea" },
        ]}
      />
    )}
    expandToggle={(row) => `${row.protocol?.length ?? 0} steps`}
    columns={[
      { field: "position", label: "Position", width: 3 },
      { field: "rate", type: "number", width: 3 },
    ]}
  />
);

Modifications.propTypes = { fieldPath: PropTypes.string.isRequired };

const Protocol = () => (
  <>
    <TableArrayField
      fieldPath={`${BASE}.preparation_protocol`}
      label="Preparation protocol"
      required
      minItems={1}
      addButtonLabel="Add step"
      columns={[
        { field: "name", width: 4 },
        { field: "description", type: "textarea" },
      ]}
    />
    <Divider />
    <ExternalDatabases fieldPath={`${BASE}.external_databases`} />
    <Divider />
    <Modifications fieldPath={`${BASE}.modifications`} />
  </>
);

const story = {
  title: "TableArrayField",
  scenarios: [
    { name: "Empty (min 1 row)", initialValues: {}, render: Protocol },
    {
      name: "Filled",
      initialValues: entityValues("Polymer", {
        preparation_protocol: [
          {
            name: "Centrifugation",
            description: "10 min at 4000 g, supernatant kept",
          },
          { name: "Filtration", description: "0.22 µm filter" },
        ],
        external_databases: ["pdb:1GWD", "uniprot:"],
        modifications: [
          {
            position: "C-terminal",
            rate: 0.5,
            protocol: [{ name: "Digestion", description: "Trypsin, 2 h" }],
          },
        ],
      }),
      render: Protocol,
    },
    {
      name: "With errors",
      initialValues: entityValues("Polymer", {
        preparation_protocol: [{ name: "Centrifugation", description: "" }],
        external_databases: ["emdb:1234"],
        modifications: [
          { position: "N1", protocol: [{ name: "", description: "" }] },
        ],
      }),
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                preparation_protocol: [
                  { description: "Missing data for required field." },
                ],
                external_databases: { 0: "Unknown prefix." },
                modifications: [
                  {
                    protocol: [{ name: "Missing data for required field." }],
                  },
                ],
              },
            ],
          },
        },
      },
      render: Protocol,
    },
    {
      name: "List-level error",
      initialValues: entityValues("Polymer"),
      initialErrors: entityErrors(
        "preparation_protocol",
        "Shorter than minimum length 1."
      ),
      render: Protocol,
    },
  ],
};

export default story;
