import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Message } from "mbdb-semantic-ui-react";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { OrganismField } from "@js/mbdb/forms/shared/VocabularyFields";
import { ComplexSubstanceCommonFields } from "@js/mbdb/forms/entities/ComplexSubstanceCommon";
import { BodyFluidFields } from "./BodyFluidFields";
import { CellFractionFields } from "./CellFractionFields";
import { VirionFields } from "./VirionFields";
import { SolidTissueSampleFields } from "./SolidTissueSampleFields";
import { DERIVED_FROM } from "./constants";

// A plain lookup of the derived_from value to the sub-form (guide §8). The four
// sub-types live in this folder and are used nowhere else.
const SUBTYPE_FIELDS = {
  "Body fluid": BodyFluidFields,
  "Cell fraction": CellFractionFields,
  Virion: VirionFields,
  "Solid tissue sample": SolidTissueSampleFields,
};

// The content of a complex substance of biological origin's modal, after Type
// and Name: the "Derived from" discriminator picks the sub-type; the source
// organism and the common complex-substance block follow it (the same for all
// sub-types). Until a sub-type is picked, only the discriminator and the hint
// show. `derived_from` keeps `name` on change (lead decision 2026-10-03).
export const ComplexSubstanceOfBiologicalOriginFields = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const derivedFrom = getIn(values, `${fieldPath}.derived_from`);
  const SubtypeFields = SUBTYPE_FIELDS[derivedFrom];
  return (
    <>
      <DiscriminatorField
        objectPath={fieldPath}
        field="derived_from"
        options={DERIVED_FROM}
        variant="buttons"
        // keep the fields every sub-type shares (base type): a mis-picked
        // sub-type then costs only the sub-type fields, and the confirm
        // dialog ("The type-specific data will be removed.") is literally true
        // (plan 4R, Y1)
        keep={[
          "id",
          "type",
          "name",
          "source_organism",
          "preparation_protocol",
          "storage",
          "additional_specifications",
        ]}
      />
      {SubtypeFields ? (
        <>
          <OrganismField fieldPath={`${fieldPath}.source_organism`} />
          <SubtypeFields fieldPath={fieldPath} />
          <ComplexSubstanceCommonFields fieldPath={fieldPath} />
        </>
      ) : (
        <Message info content="Select what the substance is derived from" />
      )}
    </>
  );
};

ComplexSubstanceOfBiologicalOriginFields.propTypes = {
  // the entity item path
  fieldPath: PropTypes.string.isRequired,
};
