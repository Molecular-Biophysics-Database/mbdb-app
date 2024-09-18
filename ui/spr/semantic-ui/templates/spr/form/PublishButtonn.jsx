import React from "react";
import { useDepositApiClient, useFormConfig } from "@js/oarepo_ui";
import { i18next } from "@translations/oarepo_ui/i18next";
import { useFormikContext } from "formik";
import { Button } from "semantic-ui-react";

export const PublishButtonn = () => {
  const { isSubmitting, save, values: recordMetadata } = useDepositApiClient();
  const { validateForm, setFieldError } = useFormikContext();
  const {
    formConfig: { permissions },
  } = useFormConfig();

  console.log(recordMetadata);
  console.log(recordMetadata.state);
  console.log(permissions);

  const submit = async () => {
    const validationErrors = await validateForm();
    await save();

    if (Object.keys(validationErrors).length === 0) {
      await save();
    } else {
      setFieldError("FEvalidationErrors", {
        errors: validationErrors,
        errorMessage: i18next.t("Please fix the errors before submitting."),
      });
    }
  };

  return (
    <div>
      <Button
        style={{
          backgroundColor: "#023850",
          color: "white",
        }}
        onClick={submit}
        disabled={isSubmitting}
      >
        {isSubmitting ? "Submitting..." : "Submit"}
      </Button>
    </div>
  );
};

export default PublishButtonn;
