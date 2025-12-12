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
            'files.enabled'
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
        value: "sensor",
        label: "Sensor",
        fieldPaths: [
            'metadata.method_specific_parameters.sensor'
        ],
    },
    {
        value: "measurement-positions",
        label: "Measurement positions",
        fieldPaths: [
            "metadata.method_specific_parameters.measurement_positions"
        ],
    },
    {
        value: "measurement-protocol",
        label: "Measurement protocol",
        fieldPaths: [
            'metadata.method_specific_parameters.measurement_protocol'
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
    const [showErrors, setShowErrors] = useState(false);

    const value = useMemo(() => {
        return {
            selectedTab,
            setSelectedTab,
            tabs: TABS_CONFIG,
            showErrors,
            setShowErrors
        };
    }, [selectedTab, showErrors]);

    return (
        <FormContext.Provider value={value}>
            {children}
        </FormContext.Provider>
    )
}