import React, { useContext } from 'react'
import PreviewButton from "@mbdb_deposit/buttons/PreviewButton";
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
            <button
                className="transition-all bg-dark text-white px-6 h-[36px] rounded-normal mr-1 font-JostMedium hover:bg-dark/75"
                onClick={async () => {
                    await handleSaveMetadataAndFiles();
                    setShowErrors(true);
                }}
            >
                Save
            </button>
            <div className="mr-1">
                <PreviewButton />
            </div>
            {values.id && RequestOnRecordView(values, setErrors, save)}
        </>
    )
}