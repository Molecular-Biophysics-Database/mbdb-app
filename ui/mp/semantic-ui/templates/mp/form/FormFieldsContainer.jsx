import React, { useRef } from "react";
import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import RawMeasurementFilesTab from "@mbdb_deposit/general/generalTabs/RawMeasurementFilesTab";
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import ChemicalEnvironmentTab from "@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab";
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import RecordInformationTab from "@mbdb_deposit/general/generalTabs/RecordInformationTab";
import InstrumentTab from "@mp_deposit/mpTabs/InstrumentTab";
import MeasurementsTab from "@mp_deposit/mpTabs/MeasurementsTab";
import DataAnalysisTab from "@mp_deposit/mpTabs/DataAnalysisTab";
import { Formik, useFormikContext } from "formik";
import { useFormConfig, useDepositApiClient } from "@js/oarepo_ui";
import { Button } from "semantic-ui-react";
import RequestOnRecordView from "@mbdb_deposit/buttons/RequestsRecordView";
import PreviewButton from "@mbdb_deposit/buttons/PreviewButton";
import CalibrantsTab from "@mp_deposit/mpTabs/CalibrantsTab";
import ModeTab from "@mp_deposit/mpTabs/ModeTab";

function FormFieldsContainer() {
  const Tabs = [
    { value: "record-information", label: "Record information" },
    { value: "entities-of-interest", label: "Entities of interest" },
    { value: "chemical-environment", label: "Chemical environments" },
    { value: "raw-measurement-files", label: "Raw measurement files" },
    { value: "instrument", label: "Instrument" },
    { value: "mode", label: "Mode" },
    { value: "calibrants", label: "Calibrants" },
    { value: "measurements", label: "Measurements" },
    { value: "result", label: "Results" },
    { value: "data-analysis", label: "Data analysis" },
  ];

  const location = useLocation();
  const [state, setState] = useState({ selected: "record-information" });
  const { save, values: recordMetadata } = useDepositApiClient();
  const { values, setErrors } = useFormikContext();

  console.log(recordMetadata);

  useEffect(() => {
    save(true);
  }, []);

  useEffect(() => {
    const selectedTab = location?.state?.selectedTab || "record-information";
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
      <div className="flex mb-4 ml-3">
        <PreviewButton />
        <Button
          style={{ backgroundColor: "#023850", color: "white" }}
          onClick={() => handleSaveMetadataAndFiles()}
        >
          Save
        </Button>
        {values.id && RequestOnRecordView(values, setErrors, save)}
      </div>
      <div className="flex justify-center">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[90vh] max-h-[900px]">
            <div className="bg-dark flex flex-col rounded-tl-normal rounded-bl-normal">
              {Tabs.map((tab) => (
                <button
                  key={tab.value}
                  className={`py-5 px-6 font-JostBold text-left cursor-pointer rounded-tl-normal rounded-bl-normal hover:bg-primary hover:text-dark ${
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
                  You are depositing MP data
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
                    className={`${
                      state.selected === "record-information" ? "" : "hidden"
                    }`}
                  >
                    <RecordInformationTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${
                      state.selected === "entities-of-interest" ? "" : "hidden"
                    }`}
                  >
                    <EntitiesOfInterestTab name="metadata.general_parameters" />
                  </div>

                  <div
                    className={`${
                      state.selected === "chemical-environment" ? "" : "hidden"
                    }`}
                  >
                    <ChemicalEnvironmentTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${state.selected === "result" ? "" : "hidden"}`}
                  >
                    <ResultTab name="metadata.general_parameters" />
                  </div>

                  <div
                    className={`${
                      state.selected === "instrument" ? "" : "hidden"
                    }`}
                  >
                    <InstrumentTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${
                      state.selected === "measurements" ? "" : "hidden"
                    }`}
                  >
                    <MeasurementsTab name="metadata.method_specific_parameters" />
                  </div>
                  <div
                    className={`${
                      state.selected === "calibrants" ? "" : "hidden"
                    }`}
                  >
                    <CalibrantsTab name="metadata.method_specific_parameters" />
                  </div>
                  <div
                    className={`${state.selected === "mode" ? "" : "hidden"}`}
                  >
                    <ModeTab name="metadata.method_specific_parameters.mode" />
                  </div>
                  <div
                    className={`${
                      state.selected === "data-analysis" ? "" : "hidden"
                    }`}
                  >
                    <DataAnalysisTab name="metadata.method_specific_parameters" />
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
