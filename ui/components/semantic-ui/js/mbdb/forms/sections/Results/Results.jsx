import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import Overridable from "react-overridable";
import { buildUID } from "react-searchkit";
import { useReviewMode } from "mbdb-semantic-ui-react";
import { ButtonGroupField } from "@js/mbdb/forms/building-blocks/ButtonGroupField";
import { DiscriminatorField } from "@js/mbdb/forms/building-blocks/DiscriminatorField";
import { FieldRow } from "@js/mbdb/forms/building-blocks/FieldRow";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { SelectField } from "@js/mbdb/forms/building-blocks/SelectField";
import {
  NumberField,
  TextField,
} from "@js/mbdb/forms/building-blocks/TextField";
import { ToggleFieldGroup } from "@js/mbdb/forms/building-blocks/ToggleFieldGroup";
import { valueUnitText } from "@js/mbdb/forms/building-blocks/DetailView/values";
import {
  ENTITY_COPIES_ITEM_SPEC,
  EntityCopiesTable,
} from "@js/mbdb/forms/shared/EntityAmountTable";
import { RESULTS_PATH } from "./path";
import {
  RESULT_TYPE_ORDER,
  RESULT_UNITS,
  SIZE_RESULT_TYPE,
  SIZE_TYPES,
  resultSeed,
} from "./resultTypes";

const ValueErrorFields = ({ fieldPath }) => (
  <ToggleFieldGroup fieldPath={fieldPath}>
    <FieldRow widths="equal">
      <NumberField fieldPath={`${fieldPath}.lower`} />
      <NumberField fieldPath={`${fieldPath}.upper`} />
      <ButtonGroupField
        fieldPath={`${fieldPath}.is_relative`}
        options={[
          { value: true, text: "Yes" },
          { value: false, text: "No" },
        ]}
      />
    </FieldRow>
  </ToggleFieldGroup>
);
ValueErrorFields.propTypes = { fieldPath: PropTypes.string.isRequired };

const ResultForm = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const type = getIn(values, `${fieldPath}.type`);
  const units = RESULT_UNITS[type];
  return (
    <>
      <DiscriminatorField
        objectPath={fieldPath}
        field="type"
        options={RESULT_TYPE_ORDER}
        variant="dropdown"
        keep={["id", "name", "entities_involved"]}
        seed={resultSeed}
      />
      <TextField fieldPath={`${fieldPath}.name`} />
      {type === SIZE_RESULT_TYPE && (
        <ButtonGroupField
          fieldPath={`${fieldPath}.size_type`}
          options={SIZE_TYPES}
        />
      )}
      {units && (
        <>
          <FieldRow widths="equal">
            <NumberField fieldPath={`${fieldPath}.value`} />
            <SelectField fieldPath={`${fieldPath}.unit`} options={units} />
          </FieldRow>
          <ValueErrorFields fieldPath={`${fieldPath}.value_error`} />
        </>
      )}
      <EntityCopiesTable fieldPath={`${fieldPath}.entities_involved`} />
    </>
  );
};
ResultForm.propTypes = { fieldPath: PropTypes.string.isRequired };

export const RESULT_GROUPS = [
  {
    title: "Value",
    fields: ["size_type", "value", "unit", "value_error"],
  },
  {
    title: "Entities involved",
    fields: [{ field: "entities_involved", ...ENTITY_COPIES_ITEM_SPEC }],
  },
];

export const ResultsSectionComponent = ({ formConfig }) => {
  const reviewMode = useReviewMode();
  return (
    <Overridable id={buildUID(formConfig?.overridableIdPrefix, "Results")}>
      <React.Fragment key={reviewMode ? "review" : "edit"}>
        <ModalArrayField
          fieldPath={RESULTS_PATH}
          withIds
          itemLabel={(v) => `${v?.type ?? "Result"}: ${v?.name || "new"}`}
          newItemOptions={RESULT_TYPE_ORDER.map((type) => ({
            label: type,
            value: { type, ...resultSeed(type) },
          }))}
          columns={[
            { label: "Name", value: (v) => v?.name ?? "" },
            { label: "Type", value: (v) => v?.type ?? "" },
            { label: "Value", value: (v) => valueUnitText(v) },
          ]}
          detailGroups={RESULT_GROUPS}
          detailProps={{ exclude: ["id", "name", "type"] }}
          crumbNoun="result"
          renderForm={(itemPath) => <ResultForm fieldPath={itemPath} />}
        />
      </React.Fragment>
    </Overridable>
  );
};
ResultsSectionComponent.propTypes = { formConfig: PropTypes.object.isRequired };

export const ResultsSection = {
  key: "results",
  label: "Results",
  component: ResultsSectionComponent,
  includesPaths: [RESULTS_PATH],
};

export { RESULTS_PATH } from "./path";
