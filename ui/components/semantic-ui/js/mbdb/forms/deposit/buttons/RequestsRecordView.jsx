import React from "react";
import {serializeErrors} from "@js/oarepo_ui";
import { RecordRequests } from "@js/oarepo_requests/components";
import { i18next } from "@translations/oarepo_ui/i18next";

function RequestOnRecordView(values, setErrors, save) {

  return (
    <RecordRequests
      record={values}
      onBeforeAction={() => save({successMessage: ""})}
      onActionError={(
        e,
        variables,
        requestModalFormik,
        modalControl
      ) => {
        if (e?.response?.data?.errors?.length > 0) {
          const errors = serializeErrors(
            e?.response?.data?.errors,
            i18next.t(
                "Action failed due to validation errors. Please correct the errors and try again:"
            )
          );
          setErrors(errors);
        }
        modalControl?.closeModal();
      }}
    />
  )
}

export default RequestOnRecordView;