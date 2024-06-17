import React, { useRef } from "react";
import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import RawMeasurementFilesTab from "@mbdb_deposit/general/generalTabs/RawMeasurementFilesTab";
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import InstrumentTab from "@bli_deposit/bliTabs/InstrumentTab";
import ChemicalEnvironmentTab from "@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab";
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import ProjectInformationTab from "@mbdb_deposit/general/generalTabs/ProjectInformationTab";
import PlatesTab from "@bli_deposit/bliTabs/PlatesTab";
import SensorsTab from "@bli_deposit/bliTabs/SensorsTab";
import MeasurementProtocolStepTab from "@bli_deposit/bliTabs/MeasurementProtocolStepTab";
import MeasurementsTab from "@bli_deposit/bliTabs/MeasurementsTab";
import DataAnalysisTab from "@bli_deposit/bliTabs/DataAnalysisTab";
import { Formik } from "formik";
import { useFormConfig, useDepositApiClient } from "@js/oarepo_ui";
import { Button } from "semantic-ui-react";

function FormFieldsContainer() {
  const Tabs = [
    { value: "raw-measurement-files", label: "Raw measurement files" },
    { value: "project-information", label: "Project information" },
    { value: "entities-of-interest", label: "Entities of interest" },
    { value: "chemical-environment", label: "Chemical environments" },
    { value: "result", label: "Results" },
    { value: "instrument", label: "Instrument" },
    { value: "plates", label: "Plates" },
    { value: "sensors", label: "Sensors" },
    { value: "measurement-protocol", label: "Measurement protocol" },
    { value: "measurements", label: "Measurements" },
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
        ? recordFiles?.entries?.map((file) => file)
        : [{}],
  };

  const fileUploaderRef = useRef(null);

  const handleUpload = async () => {
    console.log(fileUploaderRef);
    if (fileUploaderRef.current) {
      await fileUploaderRef.current.submitFiles();
    }
  };

  const handleSaveMetadataAndFiles = async () => {
    save(true);
    handleUpload();
  };

  return (
    <>
      <div className="mb-4 ml-3">
        <Button style={{ backgroundColor: "#023850", color: "white" }} onClick={() => handleSaveMetadataAndFiles()}>
          Save
        </Button>
      </div>
      <div className="flex justify-center">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[90vh]">
            <div className="bg-dark flex flex-col rounded-tl-normal rounded-bl-normal">
              {Tabs.map((tab) => (
                <button
                  key={tab.value}
                  className={`py-5 px-6 font-JostBold cursor-pointer rounded-tl-normal rounded-bl-normal hover:bg-primary hover:text-dark ${
                    state.selected === tab.value
                      ? "bg-primary text-dark"
                      : "text-white"
                  }`}
                  onClick={() => setState({ selected: tab.value })}
                >
                  {tab.label}
                </button>
              ))}
            </div>
            <div className="overflow-y-scroll overflow-x-hidden">
              <div className="flex flex-col w-[1200px]">
                <div className="flex text-dark font-JostBold text-24px mt-4 ml-6">
                  You are depositing BLI data
                </div>
                <div className="m-6">
                  <div
                    className={`${
                      state.selected === "raw-measurement-files" ? "" : "hidden"
                    }`}
                  >
                    <Formik initialValues={filesInitialState}>
                      <React.Fragment>
                        <RawMeasurementFilesTab
                          ref={fileUploaderRef}
                          name="files"
                          save={save}
                          recordMetadata={recordMetadata}
                        />
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
                    {state.selected === "plates" && (
                      <PlatesTab name="metadata.method_specific_parameters" />
                    )}
                    {state.selected === "sensors" && (
                      <SensorsTab name="metadata.method_specific_parameters" />
                    )}
                    {state.selected === "measurement-protocol" && (
                      <MeasurementProtocolStepTab name="metadata.method_specific_parameters" />
                    )}
                    {state.selected === "measurements" && (
                      <MeasurementsTab name="metadata.method_specific_parameters" />
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
    </>
  );
}

export default FormFieldsContainer;
