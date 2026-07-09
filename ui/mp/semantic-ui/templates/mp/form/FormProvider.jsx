import React, { createContext, useState, useMemo } from "react";

export const FormContext = createContext(null);

const TABS_CONFIG = [
    {
        value: "record-information",
        label: "Record information",
        fieldPaths: [
            'metadata.general_parameters.record_information',
            'metadata.general_parameters.depositors'
        ],
    },
    {
        value: "entities-of-interest",
        label: "Entities of interest",
        fieldPaths: [
            'metadata.general_parameters.entities_of_interest'
        ],
    },
    {
        value: "chemical-environments",
        label: "Chemical environments",
        fieldPaths: [
            'metadata.general_parameters.chemical_environments'
        ],
    },
    {
        value: "raw-measurement-files",
        label: "Raw measurement files",
        fieldPaths: [
            'files.enabled',
            'files'
        ],
    },
    {
        value: "instrument",
        label: "Instrument",
        fieldPaths: [
            'metadata.general_parameters.instrument',
            'metadata.method_specific_parameters.experiment_type',
        ],
    },
    {
        value: "mode",
        label: "Mode",
        fieldPaths: [
            'metadata.method_specific_parameters.mode'
        ],
    },
    {
        value: "calibrants",
        label: "Calibrants",
        fieldPaths: [
            'metadata.method_specific_parameters.calibrants'
        ],
    },
    {
        value: "measurements",
        label: "Measurements",
        fieldPaths: [
            'metadata.method_specific_parameters.measurements'
        ],
    },
    {
        value: "results",
        label: "Results",
        fieldPaths: [
            'metadata.general_parameters.results'
        ],
    },
    {
        value: "data-analysis",
        label: "Data analysis",
        fieldPaths: [
            'metadata.method_specific_parameters.data_analysis'
        ],
    },
];

export function FormProvider({ children }) {
    const [selectedTab, setSelectedTab] = useState(TABS_CONFIG[0].value);
    const [fileUploadErrors, setFileUploadErrors] = useState([]);
    const [savedAt, setSavedAt] = useState(null);
    const [isSaving, setIsSaving] = useState(false);

    const value = useMemo(() => {
        return {
            selectedTab,
            setSelectedTab,
            tabs: TABS_CONFIG,
            showErrors: savedAt !== null,
            fileUploadErrors,
            setFileUploadErrors,
            savedAt,
            setSavedAt,
            isSaving,
            setIsSaving,
        };
    }, [selectedTab, fileUploadErrors, savedAt, isSaving]);

    return (
        <FormContext.Provider value={value}>
            {children}
        </FormContext.Provider>
    )
}