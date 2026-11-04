import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Header } from "mbdb-semantic-ui-react";
import { DetailView } from "@js/mbdb/forms/building-blocks/DetailView";
import { ENTITY_TYPES } from "./entityTypes";

// A single entity read-only, for review mode (design ReviewMode.md): a
// "<name> · <type>" heading and the entity's DetailView, grouped by its type.
// Lives next to entityTypes.js (the one place that knows all types), so no
// entities/ -> sections/ import is created. `exclude` drops the row's own
// columns (id, type, name), never repeating them in the details.
export const EntityDetails = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const value = getIn(values, fieldPath) ?? {};
  const type = value.type;
  const groups = ENTITY_TYPES[type]?.groups(value) ?? [];
  return (
    <>
      <Header as="h4">{`${value.name ?? ""} · ${type ?? ""}`}</Header>
      <DetailView
        fieldPath={fieldPath}
        groups={groups}
        exclude={["id", "type", "name"]}
      />
    </>
  );
};

EntityDetails.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
