import React, { useRef } from "react";
import { useState, useEffect } from "react";
import RawMeasurementFilesTab from "@mbdb_deposit/general/generalTabs/RawMeasurementFilesTab";
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import ChemicalEnvironmentTab from "@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab";
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import RecordInformationTab from "@mbdb_deposit/general/generalTabs/RecordInformationTab";
import InstrumentTab from "@spr_deposit/sprTabs/InstrumentTab";
import MeasurementProtocolTab from "@spr_deposit/sprTabs/MeasurementProtocolTab";
import MeasurementsTab from "@spr_deposit/sprTabs/MeasurementsTab";
import DataAnalysisTab from "@spr_deposit/sprTabs/DataAnalysisTab";
import SensorTab from "@spr_deposit/sprTabs/SensorTab";
import MeasurementPositionsTab from "@spr_deposit/sprTabs/MeasurementPositionsTab";
import { Formik, useFormikContext } from "formik";
import { useFormConfig, useDepositApiClient } from "@js/oarepo_ui";
import { Button } from "semantic-ui-react";
import RequestOnRecordView from "@mbdb_deposit/buttons/RequestsRecordView";
import PreviewButton from "@mbdb_deposit/buttons/PreviewButton";

function FormFieldsContainer() {
  const community = new URLSearchParams(location.search).get('community');
  
  const Tabs = [
    { value: "record-information", label: "Record information" },
    { value: "entities-of-interest", label: "Entities of interest" },
    { value: "chemical-environment", label: "Chemical environments" },
    { value: "raw-measurement-files", label: "Raw measurement files" },
    { value: "instrument", label: "Instrument" },
    { value: "sensor", label: "Sensor" },
    { value: "measurement-positions", label: "Measurement positions" },
    { value: "measurement-protocol", label: "Measurement protocol" },
    { value: "measurements", label: "Measurements" },
    { value: "result", label: "Results" },
    { value: "data-analysis", label: "Data analysis" },
  ];

  const [selectedTab, setSelectedTab] = useState("record-information");
  const { save, values: recordMetadata } = useDepositApiClient();
  const { values, setErrors } = useFormikContext();

  useEffect(() => {
    if(recordMetadata.id === "") {
      recordMetadata.parent.communities.default = community
    }
    save({ saveWithoutDisplayingValidationErrors: true });
  }, []);

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
    await save(true);
    handleUpload();
  };

  return (
    <>
      <div className="flex mb-4 ml-3">
        <Button
          style={{ backgroundColor: "#023850", color: "white" }}
          onClick={() => handleSaveMetadataAndFiles()}
        >
          Save
        </Button>
        <PreviewButton />
        {values.id && RequestOnRecordView(values, setErrors, save)}
      </div>
      <div className="flex justify-center">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[90vh] max-h-[900px]">
            <div className="bg-dark flex flex-col rounded-tl-normal rounded-bl-normal">
              {Tabs.map((tab) => (
                <button
                  key={tab.value}
                  className={`py-5 px-6 font-JostBold cursor-pointer text-left rounded-tl-normal rounded-bl-normal hover:bg-primary hover:text-dark ${
                    selectedTab === tab.value
                      ? "bg-primary text-dark"
                      : "text-white"
                  }`}
                  onClick={() => setSelectedTab(tab.value)}
                >
                  {tab.label}
                </button>
              ))}
            </div>
            <div className="overflow-y-scroll overflow-x-hidden">
              <div className="flex flex-col w-[1200px]">
                <div className="flex text-dark font-JostBold text-24px mt-4 ml-6">
                  You are depositing SPR data
                </div>
                <div className="m-6">
                  <div
                    className={`${
                      selectedTab === "raw-measurement-files" ? "" : "hidden"
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
                      selectedTab === "record-information" ? "" : "hidden"
                    }`}
                  >
                    <RecordInformationTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${
                      selectedTab === "entities-of-interest" ? "" : "hidden"
                    }`}
                  >
                    <EntitiesOfInterestTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${
                      selectedTab === "chemical-environment" ? "" : "hidden"
                    }`}
                  >
                    <ChemicalEnvironmentTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${selectedTab === "result" ? "" : "hidden"}`}
                  >
                    <ResultTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${
                      selectedTab === "instrument" ? "" : "hidden"
                    }`}
                  >
                    <InstrumentTab name="metadata.general_parameters" />
                  </div>
                  <div
                    className={`${selectedTab === "sensor" ? "" : "hidden"}`}
                  >
                    <SensorTab name="metadata.method_specific_parameters" />
                  </div>

                  <div
                    className={`${
                      selectedTab === "measurement-positions" ? "" : "hidden"
                    }`}
                  >
                    <MeasurementPositionsTab name="metadata.method_specific_parameters" />
                  </div>

                  <div
                    className={`${
                      selectedTab === "measurement-protocol" ? "" : "hidden"
                    }`}
                  >
                    <MeasurementProtocolTab name="metadata.method_specific_parameters" />
                  </div>

                  <div
                    className={`${
                      selectedTab === "measurements" ? "" : "hidden"
                    }`}
                  >
                    <MeasurementsTab name="metadata.method_specific_parameters" />
                  </div>

                  <div
                    className={`${
                      selectedTab === "data-analysis" ? "" : "hidden"
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
