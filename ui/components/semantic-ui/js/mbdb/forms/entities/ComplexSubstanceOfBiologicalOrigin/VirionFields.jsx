import React from "react";
import PropTypes from "prop-types";
import { Form } from "mbdb-semantic-ui-react";
import { FieldGroup } from "@js/mbdb/forms/building-blocks/FieldGroup";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { OrganismField } from "@js/mbdb/forms/shared/VocabularyFields";
import { VIRION_GENETIC_MATERIAL, VIRION_PARTICLE_TYPES } from "./constants";

// The fields specific to a biological substance made of virions. The three
// required characteristics have short option lists, so they are button groups;
// being required, their buttons cannot be toggled off (correct here).
export const VirionFields = ({ fieldPath }) => (
  <>
    {/* "Virion characteristics" is a UI grouping with no model field of its
        own, so its title is literal (guide §6). */}
    <FieldGroup title="Virion characteristics">
      <ButtonGroupField
        fieldPath={`${fieldPath}.genetic_material`}
        options={VIRION_GENETIC_MATERIAL}
      />
      <ButtonGroupField
        fieldPath={`${fieldPath}.capsid_type`}
        options={VIRION_PARTICLE_TYPES}
      />
      <ButtonGroupField
        fieldPath={`${fieldPath}.envelope_type`}
        options={VIRION_PARTICLE_TYPES}
      />
    </FieldGroup>
    <Form.Group widths="equal">
      <OrganismField fieldPath={`${fieldPath}.host_organism`} />
      <TextField fieldPath={`${fieldPath}.host_cell_type`} />
    </Form.Group>
  </>
);

VirionFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
