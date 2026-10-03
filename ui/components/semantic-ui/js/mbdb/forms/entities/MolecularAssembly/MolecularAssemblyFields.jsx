import React from "react";
import PropTypes from "prop-types";
import { StringArrayField } from "mbdb-react-invenio-forms";
import { MolecularWeight } from "@js/mbdb/forms/shared/MolecularWeight";
import { Components } from "@js/mbdb/forms/shared/Components";
import { ExternalDatabases } from "@js/mbdb/forms/shared/ExternalDatabases";
import { ModificationTable } from "@js/mbdb/forms/shared/Modifications";
import { QualityControls } from "@js/mbdb/forms/shared/QualityControls";

// The content of a molecular assembly's entity modal, after Type and Name:
// the molecular weight, the components table (each component edited in a
// second-level modal), reference databases, deliberate chemical modifications,
// quality controls and free-text specifications. Composition only, no logic of
// its own; reused as a component's field set nowhere today, but every path is
// built from `fieldPath` anyway.
export const MolecularAssemblyFields = ({ fieldPath }) => (
  <>
    <MolecularWeight fieldPath={`${fieldPath}.molecular_weight`} />
    <Components fieldPath={`${fieldPath}.components`} />
    <ExternalDatabases fieldPath={`${fieldPath}.external_databases`} />
    {/* the assembly has one modification list (chemical_modifications), not the
        polymer's modifications object, so the shared table is used directly */}
    <ModificationTable fieldPath={`${fieldPath}.chemical_modifications`} />
    <QualityControls fieldPath={`${fieldPath}.quality_controls`} />
    <StringArrayField fieldPath={`${fieldPath}.additional_specifications`} />
  </>
);

MolecularAssemblyFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
