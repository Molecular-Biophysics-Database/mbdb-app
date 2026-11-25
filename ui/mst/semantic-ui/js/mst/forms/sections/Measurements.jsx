import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { useReviewMode } from "mbdb-semantic-ui-react";
import {
  CHEMICAL_ENVIRONMENTS_PATH,
  ENTITY_CONCENTRATION_ITEM_SPEC,
  EntityConcentrationTable,
  FieldGroup,
  FieldRow,
  ModalArrayField,
  Protocol,
  ReferenceField,
  SelectField,
  TextField,
} from "@js/mbdb/forms";
import { MEASUREMENTS_PATH, MEASUREMENT_CONTAINERS } from "./constants";
import { nextMeasurement } from "./measurement";

const MeasurementForm = ({ fieldPath }) => {
  const sample = `${fieldPath}.sample`;
  return (
    <>
      <FieldRow widths="equal">
        <TextField fieldPath={`${fieldPath}.name`} />
        <TextField fieldPath={`${fieldPath}.position`} />
      </FieldRow>
      <FieldGroup fieldPath={sample}>
        <FieldRow widths="equal">
          <ReferenceField
            fieldPath={`${sample}.chemical_environment`}
            targetPath={CHEMICAL_ENVIRONMENTS_PATH}
            label="Chemical environment"
            help="Name (id) of the chemical environment of the sample (from the chemical environments defined in the record)"
            required
          />
          <SelectField
            fieldPath={`${sample}.measurement_container`}
            options={MEASUREMENT_CONTAINERS}
          />
        </FieldRow>
        <EntityConcentrationTable
          fieldPath={`${sample}.targets`}
          addButtonLabel="Add target"
        />
        <EntityConcentrationTable
          fieldPath={`${sample}.ligands`}
          addButtonLabel="Add ligand"
        />
        <Protocol fieldPath={`${sample}.preparation_protocol`} />
      </FieldGroup>
    </>
  );
};
MeasurementForm.propTypes = { fieldPath: PropTypes.string.isRequired };

export const MEASUREMENT_GROUPS = [
  {
    title: "Sample",
    fields: [
      {
        field: "sample",
        children: {
          targets: ENTITY_CONCENTRATION_ITEM_SPEC,
          ligands: ENTITY_CONCENTRATION_ITEM_SPEC,
        },
      },
    ],
  },
];

const [ENTITY, CONCENTRATION] = ENTITY_CONCENTRATION_ITEM_SPEC.itemColumns;
const amounts = (items) =>
  (items ?? []).map((v) => (
    <div key={v?.entity?.id}>
      {ENTITY.value(v)} {CONCENTRATION.value(v)}
    </div>
  ));

const MeasurementsSectionComponent = () => {
  const { values } = useFormikContext();
  const reviewMode = useReviewMode();
  return (
    <ModalArrayField
      key={reviewMode ? "review" : "edit"}
      fieldPath={MEASUREMENTS_PATH}
      minItems={1}
      withIds
      itemLabel={(v) => v?.name || "New measurement"}
      newItemOptions={[
        {
          label: "measurement",
          value: nextMeasurement(getIn(values, MEASUREMENTS_PATH)),
        },
      ]}
      columns={[
        { label: "Name", value: (v) => v?.name ?? "" },
        { label: "Position", value: (v) => v?.position ?? "" },
        { label: "Targets", value: (v) => amounts(v?.sample?.targets) },
        { label: "Ligands", value: (v) => amounts(v?.sample?.ligands) },
      ]}
      detailGroups={MEASUREMENT_GROUPS}
      detailProps={{ exclude: ["id", "name", "position"] }}
      crumbNoun="measurement"
      renderForm={(itemPath) => <MeasurementForm fieldPath={itemPath} />}
    />
  );
};

export const MeasurementsSection = {
  key: "measurements",
  label: "Measurements",
  component: MeasurementsSectionComponent,
  includesPaths: [MEASUREMENTS_PATH],
};
