import React from "react";
import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import RawMeasurementFilesTab from "@mbdb_deposit/general/generalTabs/RawMeasurementFilesTab";
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import InstrumentTab from "@mst_deposit/mstTabs/InstrumentTab";
import ChemicalEnvironmentTab from "@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab";
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import DataAnalysisTab from "@mst_deposit/mstTabs/DataAnalysisTab";
import ProjectInformationTab from "@mbdb_deposit/general/generalTabs/ProjectInformationTab";
import MeasurementTab from "@mst_deposit/mstTabs/MeasurementTab";
import { useFormikContext, Formik } from "formik";
import { useFormConfig, useDepositApiClient } from "@js/oarepo_ui";

// for testing only
const FormikStateLogger = () => {
  const state = useFormikContext();
  return <pre>{JSON.stringify(state, null, 2)}</pre>;
};

function FormFieldsContainer() {
  const Tabs = [
    { value: "raw-measurement-files", label: "Raw measurement files" },
    { value: "project-information", label: "Project information" },
    { value: "entities-of-interest", label: "Entities of interest" },
    { value: "chemical-environment", label: "Chemical environments" },
    { value: "result", label: "Results" },
    { value: "instrument", label: "Instrument" },
    { value: "measurement", label: "Measurements" },
    { value: "data-analysis", label: "Data analysis" },
  ];

  const location = useLocation();
  const [state, setState] = useState({ selected: "project-information" });
  const { save, values: recordMetadata } = useDepositApiClient();

  useEffect(() => {
    const selectedTab = location?.state?.selectedTab || "project-information";
    setState({ selected: selectedTab });
  }, [location]);
  const { files: recordFiles } = useFormConfig();
  const filesInitialState = {
    files:
      recordFiles?.entries?.length > 0
        ? recordFiles?.entries?.map((file) => (
            file
          ))
        : [{}],
  };
  return (
    <>
      <div className="flex justify-center">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[90vh]">
            <div className="bg-dark rounded-tl-normal rounded-bl-normal">
              {Tabs.map((tab) => (
                <div
                  key={tab.value}
                  className={`py-5 px-6 font-JostBold cursor-pointer rounded-tl-normal rounded-bl-normal hover:bg-primary hover:text-dark ${
                    state.selected === tab.value
                      ? "bg-primary text-dark"
                      : "text-white"
                  }`}
                  onClick={() => setState({ selected: tab.value })}
                >
                  {tab.label}
                </div>
              ))}
            </div>
            <div className="overflow-y-scroll overflow-x-hidden">
              <div className="flex flex-col w-[1200px]">
                <div className="flex text-dark font-JostBold text-24px mt-4 ml-6">
                  You are depositing MST data
                </div>
                <div className="m-6">
                  <div
                    className={`${
                      state.selected === "raw-measurement-files" ? "" : "hidden"
                    }`}
                  >
                    <Formik
                      initialValues={filesInitialState}
                    >
                      <React.Fragment>
                        <RawMeasurementFilesTab
                          name="files"
                          save={save}
                          recordMetadata={recordMetadata}
                        />
                        <FormikStateLogger />
                      </React.Fragment>
                    </Formik>
                  </div>
                  <div
                    className={
                      state.selected === "raw-measurement-files" ? "hidden" : ""
                    }
                  >
                    {state.selected === "project-information" && (
                      <ProjectInformationTab name="metadata.general_parameters" />
                    )}
                    {state.selected === "entities-of-interest" && (
                      <EntitiesOfInterestTab name="metadata.general_parameters" />
                    )}
                    {state.selected === "chemical-environment" && (
                      <ChemicalEnvironmentTab name="metadata.general_parameters" />
                    )}
                    {state.selected === "result" && (
                      <ResultTab name="metadata.general_parameters" />
                    )}
                    {state.selected === "instrument" && (
                      <InstrumentTab name="metadata.general_parameters" />
                    )}
                    {state.selected === "measurement" && (
                      <MeasurementTab name="metadata.method_specific_parameters" />
                    )}
                    {state.selected === "data-analysis" && (
                      <DataAnalysisTab name="metadata.method_specific_parameters" />
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    
      <FormikStateLogger />
      
    </>
  );
}

export default FormFieldsContainer;
