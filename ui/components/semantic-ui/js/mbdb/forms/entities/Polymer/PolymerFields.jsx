import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { StringTableField } from "@js/mbdb/forms/building-blocks/StringTableField";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { FieldRow } from "@js/mbdb/forms/building-blocks/FieldRow";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { OrganismField } from "@js/mbdb/forms/shared/VocabularyFields";
import { Sequence } from "@js/mbdb/forms/shared/Sequence";
import { MolecularWeight } from "@js/mbdb/forms/shared/MolecularWeight";
import { ExternalDatabases } from "@js/mbdb/forms/shared/ExternalDatabases";
import { Modifications } from "@js/mbdb/forms/shared/Modifications";
import { QualityControls } from "@js/mbdb/forms/shared/QualityControls";
import { POLYMER_TYPES, EXPRESSION_SOURCE_TYPES } from "./constants";

// The content of a polymer's entity modal, after Type and Name. Composition
// only, no logic of its own; reused as a component's field set
// (ComponentPolymer), so it assumes nothing about where it sits — every path
// is built from `fieldPath`.
export const PolymerFields = ({ fieldPath }) => (
  <>
    {/* "Identification" and "Origin" are UI groupings with no model field of
        their own, so their titles are literal (guide §6: a literal is fine for
        a group that is not a field label). They match POLYMER_GROUPS. */}
    <FieldGroup title="Identification">
      <FieldRow widths="equal">
        <SelectField
          fieldPath={`${fieldPath}.polymer_type`}
          options={POLYMER_TYPES}
        />
        <ButtonGroupField
          fieldPath={`${fieldPath}.expression_source_type`}
          options={EXPRESSION_SOURCE_TYPES}
        />
      </FieldRow>
      <TextField fieldPath={`${fieldPath}.variant`} />
    </FieldGroup>
    <Sequence fieldPath={`${fieldPath}.sequence`} />
    <FieldGroup title="Origin">
      <Form.Group widths="equal">
        <OrganismField fieldPath={`${fieldPath}.source_organism`} />
        <OrganismField fieldPath={`${fieldPath}.expression_organism`} />
      </Form.Group>
    </FieldGroup>
    <MolecularWeight fieldPath={`${fieldPath}.molecular_weight`} />
    <ExternalDatabases fieldPath={`${fieldPath}.external_databases`} />
    <StringTableField
      fieldPath={`${fieldPath}.additional_specifications`}
      columnLabel="Specification"
      addButtonLabel="Add specification"
    />
    <Modifications fieldPath={`${fieldPath}.modifications`} />
    <QualityControls fieldPath={`${fieldPath}.quality_controls`} />
  </>
);

PolymerFields.propTypes = {
  // the entity item path (or a component item path)
  fieldPath: PropTypes.string.isRequired,
};
