import React, { useContext } from 'react'
import PreviewButton from "@mbdb_deposit/buttons/PreviewButton";
import { Button } from "semantic-ui-react";
import { useFormikContext } from "formik";
import { useDepositApiClient } from "@js/oarepo_ui";
import RequestOnRecordView from "@mbdb_deposit/buttons/RequestsRecordView";
import { FormContext } from "./FormProvider"

export default function FormButtons({ handleSaveMetadataAndFiles }) {
    const { values, setErrors } = useFormikContext();
    const { save } = useDepositApiClient();
    const { setShowErrors } = useContext(FormContext);

    return (
        <>
            <Button
                style={{ backgroundColor: "#023850", color: "white" }}
                onClick={async () => {
                    await handleSaveMetadataAndFiles();
                    setShowErrors(true);
                }}
            >
                Save
            </Button>
            <PreviewButton />
            {values.id && RequestOnRecordView(values, setErrors, save)}
        </>
    )
}