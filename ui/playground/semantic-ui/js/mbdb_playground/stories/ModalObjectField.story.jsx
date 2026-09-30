import React from "react";
import PropTypes from "prop-types";
import { ModalObjectField } from "@js/mbdb/forms/building-blocks/ModalObjectField";
import { ValueUnitField } from "@js/mbdb/forms/building-blocks/ValueUnitField";
import { TableArrayField } from "@js/mbdb/forms/building-blocks/TableArrayField";

const TEMPERATURE_UNITS = ["K", "°C", "°F"];
const TIME_UNITS = [
  "nanoseconds",
  "microseconds",
  "milliseconds",
  "seconds",
  "minutes",
  "hours",
  "days",
  "months",
  "years",
];

const PATH = "metadata.general_parameters.entities_of_interest.0.storage";

const storageSummary = (v) =>
  v
    ? [
        v.temperature && `${v.temperature.value} ${v.temperature.unit}`,
        v.duration && `${v.duration.value} ${v.duration.unit}`,
        v.storage_preparation &&
          `${v.storage_preparation.length} preparation steps`,
      ]
        .filter(Boolean)
        .join(", ")
    : "";

// Explicit labels/helps until the ui_model has entity children (polymorphic
// Entity). Stand-in for the real StorageForm (plan step 3 builds it on this
// block); storage_preparation is an array of Step {name, description}.
const STORAGE_GROUPS = [
  { title: "Conditions", fields: ["temperature", "duration"] },
  { title: "Storage preparation", fields: ["storage_preparation"] },
];

const StorageForm = ({ fieldPath }) => (
  <>
    <ValueUnitField
      fieldPath={`${fieldPath}.temperature`}
      label="Temperature"
      units={TEMPERATURE_UNITS}
      required
    />
    <ValueUnitField
      fieldPath={`${fieldPath}.duration`}
      label="Duration"
      units={TIME_UNITS}
    />
    <TableArrayField
      fieldPath={`${fieldPath}.storage_preparation`}
      label="Storage preparation"
      addButtonLabel="Add step"
      columns={[
        { field: "name", width: 4 },
        { field: "description", type: "textarea" },
      ]}
    />
  </>
);

StorageForm.propTypes = { fieldPath: PropTypes.string.isRequired };

const Storage = () => (
  <ModalObjectField
    fieldPath={PATH}
    label="Storage"
    help="Information about how the substance was stored between being acquired and measured."
    summary={storageSummary}
    detailGroups={STORAGE_GROUPS}
    renderForm={(path) => <StorageForm fieldPath={path} />}
  />
);

const story = {
  title: "ModalObjectField",
  scenarios: [
    { name: "Absent", initialValues: {}, render: Storage },
    {
      name: "Present",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                storage: {
                  temperature: { value: 4, unit: "°C" },
                  duration: { value: 3, unit: "days" },
                  storage_preparation: [
                    {
                      name: "Flash freezing",
                      description: "In liquid nitrogen",
                    },
                  ],
                },
              },
            ],
          },
        },
      },
      render: Storage,
    },
    {
      name: "With errors",
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { storage: { temperature: { unit: "°C" } } },
            ],
          },
        },
      },
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              {
                storage: {
                  temperature: { value: "Missing data for required field." },
                },
              },
            ],
          },
        },
      },
      render: Storage,
    },
  ],
};

export default story;
