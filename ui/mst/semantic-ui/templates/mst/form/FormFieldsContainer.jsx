import React, { useRef } from "react";
import { useState, useEffect, useContext } from "react";
import RawMeasurementFilesTab from "@mbdb_deposit/general/generalTabs/RawMeasurementFilesTab";
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import InstrumentTab from "@mst_deposit/mstTabs/InstrumentTab";
import ChemicalEnvironmentTab from "@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab";
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import DataAnalysisTab from "@mst_deposit/mstTabs/DataAnalysisTab";
import RecordInformationTab from "@mbdb_deposit/general/generalTabs/RecordInformationTab";
import MeasurementsTab from "@mst_deposit/mstTabs/MeasurementsTab";
import { Formik, useFormikContext } from "formik";
import { useFormConfig, useDepositApiClient } from "@js/oarepo_ui";
import { Button } from "semantic-ui-react";
import RequestOnRecordView from "@mbdb_deposit/buttons/RequestsRecordView";
import PreviewButton from "@mbdb_deposit/buttons/PreviewButton";
import { FormContext } from "./FormProvider";
import FormButtons from "./FormButtons";

const FormikStateLogger = () => {
  const state = useFormikContext();
  return <pre>{JSON.stringify(state, null, 2)}</pre>;
};

function FormFieldsContainer() {
  const community = new URLSearchParams(location.search).get('community');

  const { tabs, selectedTab, setSelectedTab } = useContext(FormContext);
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
    console.log(fileUploaderRef, "File uploadddd ref");
    if (fileUploaderRef.current) {
      await fileUploaderRef.current.submitFiles();
    }
  };

  // just for testing purposes top level handler that submits both record's files and metadata
  const handleSaveMetadataAndFiles = async () => {
    await save();
    handleUpload();
  };
  return (
    <>
      <div className="flex ml-1">
        <FormButtons handleSaveMetadataAndFiles={handleSaveMetadataAndFiles} />
      </div>
      <div className="flex justify-center">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[75vh] max-h-[900px]">
            <div className="bg-dark flex flex-col p-2 rounded-tl-[0.2rem] rounded-bl-[0.2rem]">
              {tabs.map((tab) => (
                <button
                  key={tab.value}
                  className={`py-3 pl-4 pr-6 mb-2 text-[.95rem] font-JostBold cursor-pointer rounded-normal text-left hover:bg-primary hover:text-dark ${
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
              <div className="flex flex-col w-[1019px] 3xl:w-[1217px]">
                <div className="flex text-dark font-JostBold text-20px mt-4 ml-4">
                  You are depositing MST data
                </div>
                <div className="m-4">
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
                        {/* <FormikStateLogger /> */}
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
                      selectedTab === "chemical-environments" ? "" : "hidden"
                    }`}
                  >
                    <ChemicalEnvironmentTab name="metadata.general_parameters" />
                  </div>

                  <div
                    className={`${selectedTab === "results" ? "" : "hidden"}`}
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
      {/* <FormikStateLogger /> */}
    </>
  );
}

export default FormFieldsContainer;
