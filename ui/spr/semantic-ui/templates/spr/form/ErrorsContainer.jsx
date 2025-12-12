import React, { useContext, useState, useEffect, useMemo } from 'react';
import { useFormikContext } from "formik";
import { FormContext } from "./FormProvider"
import { useDepositApiClient } from "@js/oarepo_ui";
import RequestOnRecordView from "@mbdb_deposit/buttons/RequestsRecordView";

function formatFieldPath(path, tabs) {
    const parts = path.split(".");

    if (parts[0] === "files") return parts[0];

    const sliced = parts.slice(2);
    const tab = sliced[0];

    const cleanParts = sliced.map((part) => {
        const replaced = part.replace(/_/g, " ");
        const num = Number(part);
        return isNaN(num) ? replaced : num + 1;
    });

    const tabKeys = [
        ...(tabs ?? []).map(tab => tab.value.replace(/-/g, "_")),
        'depositors',
    ];

    return tabKeys.includes(tab)
        ? cleanParts.join(" / ")
        : cleanParts[cleanParts.length - 1];
}

export default function ErrorsContainer() {
    const { values } = useFormikContext();
    const { selectedTab, setSelectedTab, tabs, showErrors } = useContext(FormContext);
    
    const [openDropdown, setOpenDropdown] = useState(false);
    const [focusField, setFocusField] = useState(null);
    
    const errors = values.errors;
    
    const fields = useMemo(() => {
        if (!errors) return [];
        return errors.map((e) => ({
            fieldPath: e.field,
            fieldLabel: formatFieldPath(e.field, tabs),
            message: e.messages
        }));
    }, [errors]);
    
    useEffect(() => {
        if (!errors || !showErrors) return;

        document
            .querySelectorAll('.field-highlight')
            .forEach((el) => el.classList.remove('field-highlight'));

        fields.map(({ fieldPath }) => {
            const el = document.querySelector(`[name="${fieldPath}"]`);
            if (el) el.classList.add("field-highlight");
        })

    }, [errors, selectedTab, showErrors, fields]);

    useEffect(() => {
        if (!focusField) return;
        
        const el = document.querySelector(`[name="${focusField}"]`);

        if (el) {
            el.focus({ preventScroll: true });
            el.scrollIntoView({ behavior: "smooth", block: "center" });
        }

        setFocusField(null);
    }, [focusField])


    function navigateToForm(field) {
        const pathToTab = field.split(".", 3).join(".");
        
        const matchingTab = tabs.find((tab) => tab.fieldPaths?.includes(pathToTab));

        if (matchingTab) {
            setSelectedTab(matchingTab.value);
            setFocusField(field);
            setOpenDropdown(false);
        }
    }
    
    if (!errors?.length || !showErrors) return null;

    return (
        <>
            <div className='cursor-pointer flex w-fit bg-[#FEF6E8] border-[.1rem] border-[#EFE4D2] ml-1 mb-2 py-2 px-4 mx-3 rounded-normal font-bold' onClick={() => setOpenDropdown((state) => !state)}>
                <div className='mr-2 my-auto'>
                    Record saved with validation errors. Please correct the issues and try again.
                </div>
                <button className='px-2 py-1 rounded-normal bg-[#ee930d] text-white hover:bg-[#ee930d]/80 transition-colors'>
                    Show errors
                </button>
            </div>
            {openDropdown && (
                <div className="fixed top-0 right-0 w-full h-full z-[100] bg-black/60">
                    <div className="absolute top-0 right-0 bg-white w-2/5 h-full p-4 pt-30 overflow-y-scroll">
                        <div className='flex justify-between mb-4'>
                            <div className='font-bold'>Validation errors</div>
                            <button onClick={() => setOpenDropdown(false)}>
                                <img className='w-5' src="/static/images/close.svg" />
                            </button>
                        </div>
                        <div className='mb-2'>Please correct the following issues. Click the box to navigate to the respective field</div>
                        {fields.map(({ fieldPath, fieldLabel, message }) => (
                            <div
                                key={fieldPath}
                                className='flex justify-between cursor-pointer bg-[#FEF6E8] border-[.1rem] rounded-normal border-[#EFE4D2] mb-2 p-2 first-letter:uppercase text-sm hover:underline hover:decoration-[#ee930d]'
                                onClick={(e) => {
                                    e.stopPropagation();
                                    navigateToForm(fieldPath);
                                }}
                            >
                                <div className='flex'>
                                    <img className='w-4 mr-2' src="/static/images/error.svg" />
                                    <p>{fieldLabel}: {message}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </>
    )
}