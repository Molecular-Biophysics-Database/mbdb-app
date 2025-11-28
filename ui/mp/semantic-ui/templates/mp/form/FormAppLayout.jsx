import React from "react";
import { BaseFormLayout } from "@js/oarepo_ui";
import { FormValidationSchema } from "./FormValidationSchema";
import { FormProvider } from "./FormProvider";

export const FormAppLayout = () => {
  const formikProps = {
    validationSchema: FormValidationSchema,
  };
  return (
    <FormProvider>
      <BaseFormLayout formikProps={formikProps} />
    </FormProvider>
  );
};
export default FormAppLayout;