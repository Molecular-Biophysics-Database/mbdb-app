import React from "react";
import PropTypes from "prop-types";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";
import { ExternalLink } from "@js/mbdb/forms/building-blocks/ExternalLink";
import { KNOWN_DATABASES, parseRef, formatRef, refUrl } from "./refs";

// Opens the record in the external database. Renders nothing when the
// reference does not resolve to a URL (unknown prefixes have nowhere to
// point at, so there is no dead link).
const OpenLink = ({ row }) => (
  <ExternalLink href={refUrl(row)}>Open ↗</ExternalLink>
);
OpenLink.propTypes = { row: PropTypes.object.isRequired };

// References to records in external databases, stored as "prefix:id" strings,
// edited as a two-column table. `database`/`id` are row keys this block
// invents — there are no model fields behind them, so the columns carry an
// explicit `label` (guide §6: model text where it exists, overrides here
// because the model has none for a row we made up).
export const ExternalDatabases = ({ fieldPath }) => (
  <TableArrayField
    fieldPath={fieldPath}
    addButtonLabel="Add database"
    defaultNewValue=""
    deserialize={parseRef}
    serialize={formatRef}
    rowHint={({ database, id }) => (!!database !== !!id ? "Incomplete" : null)}
    columns={[
      {
        field: "database",
        label: "Database",
        type: "select",
        width: 4,
        options: Object.keys(KNOWN_DATABASES),
        allowAdditions: true, // real data has prefixes we do not know
      },
      { field: "id", label: "ID" },
      { field: "open", label: "", render: (row) => <OpenLink row={row} /> },
    ]}
  />
);

ExternalDatabases.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
