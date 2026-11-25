import React from "react";
import PropTypes from "prop-types";
import { useReviewMode } from "mbdb-semantic-ui-react";
import {
  FieldRow,
  ModalArrayField,
  NumberField,
  RESULTS_PATH,
  ReferenceField,
  ReferenceNames,
  SelectField,
  TIME_UNITS,
  TextField,
  ToggleFieldGroup,
} from "@js/mbdb/forms";
import {
  DATA_ANALYSIS_PATH,
  MEASUREMENTS_PATH,
  QUALITY_TYPES,
} from "./constants";
import { describeMeasurement } from "./measurement";

export const ProcessingStepForm = ({ fieldPath }) => (
  <>
    <FieldRow widths="equal">
      <TextField fieldPath={`${fieldPath}.name`} />
      <TextField fieldPath={`${fieldPath}.description`} />
    </FieldRow>
    <FieldRow widths="equal">
      <TextField fieldPath={`${fieldPath}.software_name`} />
      <TextField fieldPath={`${fieldPath}.software_version`} />
      <TextField fieldPath={`${fieldPath}.link_to_source_code`} />
    </FieldRow>
  </>
);
ProcessingStepForm.propTypes = { fieldPath: PropTypes.string.isRequired };

export const PROCESSING_COLUMNS = [
  { field: "name", label: "Name", value: (v) => v?.name ?? "" },
  {
    field: "description",
    label: "Description",
    value: (v) => v?.description ?? "",
  },
  {
    field: "software_name",
    label: "Software",
    value: (v) => v?.software_name ?? "",
  },
];
export const PROCESSING_GROUPS = [
  {
    title: "Software",
    fields: ["software_name", "software_version", "link_to_source_code"],
  },
];

const DataAnalysisForm = ({ fieldPath }) => {
  const timeWindow = `${fieldPath}.f_cold_and_hot`;
  const fitting = `${fieldPath}.data_fitting`;
  return (
    <>
      <ReferenceField
        fieldPath={`${fieldPath}.measurements`}
        targetPath={MEASUREMENTS_PATH}
        describe={describeMeasurement}
        multiple
      />
      <ReferenceField
        fieldPath={`${fieldPath}.results`}
        targetPath={RESULTS_PATH}
        multiple
      />
      <ToggleFieldGroup fieldPath={timeWindow}>
        <SelectField fieldPath={`${timeWindow}.time_unit`} options={TIME_UNITS} />
        <FieldRow widths="equal">
          <NumberField fieldPath={`${timeWindow}.f_cold_start`} min={-100} />
          <NumberField fieldPath={`${timeWindow}.f_cold_end`} min={-100} />
          <NumberField fieldPath={`${timeWindow}.f_hot_start`} min={0} />
          <NumberField fieldPath={`${timeWindow}.f_hot_end`} min={0} />
        </FieldRow>
      </ToggleFieldGroup>
      <ToggleFieldGroup fieldPath={fitting}>
        <FieldRow widths="equal">
          <TextField fieldPath={`${fitting}.model`} />
          <TextField fieldPath={`${fitting}.software_name`} />
          <TextField fieldPath={`${fitting}.software_version`} />
        </FieldRow>
        <FieldRow widths="equal">
          <NumberField fieldPath={`${fitting}.quality`} />
          <SelectField
            fieldPath={`${fitting}.quality_type`}
            options={QUALITY_TYPES}
          />
        </FieldRow>
      </ToggleFieldGroup>
      <ModalArrayField
        fieldPath={`${fieldPath}.data_processing`}
        itemLabel={(v) => v?.name || "New processing step"}
        newItemOptions={[{ label: "processing step", value: {} }]}
        columns={PROCESSING_COLUMNS}
        detailGroups={PROCESSING_GROUPS}
        detailProps={{ exclude: ["name", "description"] }}
        crumbNoun="processing step"
        renderForm={(itemPath) => <ProcessingStepForm fieldPath={itemPath} />}
      />
    </>
  );
};
DataAnalysisForm.propTypes = { fieldPath: PropTypes.string.isRequired };

export const DATA_ANALYSIS_GROUPS = [
  { title: "Links", fields: ["measurements", "results"] },
  { title: "F cold and hot", fields: ["f_cold_and_hot"] },
  { title: "Data fitting", fields: ["data_fitting"] },
  {
    title: "Data processing",
    fields: [
      {
        field: "data_processing",
        itemColumns: PROCESSING_COLUMNS,
        itemGroups: PROCESSING_GROUPS,
      },
    ],
  },
];

const count = (items) => items?.length ?? 0;

const DataAnalysisSectionComponent = () => {
  const reviewMode = useReviewMode();
  return (
    <ModalArrayField
      key={reviewMode ? "review" : "edit"}
      fieldPath={DATA_ANALYSIS_PATH}
      itemLabel={(v) => v?.data_fitting?.model || "Data analysis"}
      newItemOptions={[{ label: "data analysis", value: {} }]}
      columns={[
        { label: "Measurements", value: (v) => count(v?.measurements) },
        {
          label: "Results",
          value: (v) => (
            <ReferenceNames value={v?.results} targetPath={RESULTS_PATH} />
          ),
        },
        { label: "Model", value: (v) => v?.data_fitting?.model ?? "" },
      ]}
      detailGroups={DATA_ANALYSIS_GROUPS}
      crumbNoun="data analysis"
      renderForm={(itemPath) => <DataAnalysisForm fieldPath={itemPath} />}
    />
  );
};

export const DataAnalysisSection = {
  key: "data-analysis",
  label: "Data analysis",
  component: DataAnalysisSectionComponent,
  includesPaths: [DATA_ANALYSIS_PATH],
};
