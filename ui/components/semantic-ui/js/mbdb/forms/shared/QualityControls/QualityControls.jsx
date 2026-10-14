import React from "react";
import PropTypes from "prop-types";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { QualityCheck } from "./QualityCheck";
import { PurityFields } from "./PurityFields";
import { IdentityFields } from "./IdentityFields";
import { HomogeneityFields } from "./HomogeneityFields";

const CHECKS = [
  { field: "purity", Fields: PurityFields },
  { field: "identity", Fields: IdentityFields },
  { field: "homogeneity", Fields: HomogeneityFields },
];

// Three rows — Purity, Identity, Homogeneity — each a
// Not specified / Yes / No discriminator with the check's fields under Yes
// (design QualityControls).
export const QualityControls = ({ fieldPath }) => (
  <FieldGroup fieldPath={fieldPath}>
    {CHECKS.map(({ field, Fields }) => (
      <QualityCheck key={field} fieldPath={`${fieldPath}.${field}`}>
        <Fields fieldPath={`${fieldPath}.${field}`} />
      </QualityCheck>
    ))}
  </FieldGroup>
);

QualityControls.propTypes = {
  // the Quality_controls OBJECT path (`${itemPath}.quality_controls`)
  fieldPath: PropTypes.string.isRequired,
};
