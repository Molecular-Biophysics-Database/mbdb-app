import React from "react";
import {
  PropFieldsComponent,
} from "@js/oarepo_vocabularies";
import { useFormConfig } from "@js/oarepo_ui";
import _has from "lodash/has";
import { useFormikContext } from "formik";
import { v4 as uuidv4 } from 'uuid';
import { useEffect } from "react";
import CustomField from "./CustomField";

const CustomIdField = (prefix) => {
  return (
  <>
    <div className="mb-6">
      <CustomField
        name='id'
        label='ID'
        prefix={prefix}
        required
      />
   </div>
  </>
  )
}

const VocabularyFormFields = () => {
  const {
    formConfig: { vocabularyProps },
  } = useFormConfig();
  const hasPropFields = _has(vocabularyProps, "props");
  const { values } = useFormikContext();
  const type = values.type;
  console.log(type, 'Type')
  useEffect(() => {
    if (type === "grants") {
      values.id = `oa:${uuidv4()}`
    } else if (type === "affiliations") {
      values.id = `ror:${uuidv4()}`
    }
  }, [type, values]);
  return (
    <div>
      <div className="mb-4">
        <CustomField
          name='title'
          label='Title'
          fieldName='en'
          required
        />
      </div>
      {/* generate id fields with custom prefixes */}
      {type === "chemicals" && CustomIdField("inchikey")}
      {type === "instruments" && CustomIdField("ins")}
      {type === "body_fluids" && CustomIdField("bf")}
      {type === "cell_fractions" && CustomIdField("cf")}
      {type === "environment_types" && CustomIdField("env")}
      {type === "products" && CustomIdField("prod")}
      {hasPropFields && (
        <PropFieldsComponent vocabularyProps={vocabularyProps} />
      )}
    </div>
  );
};

export default VocabularyFormFields;