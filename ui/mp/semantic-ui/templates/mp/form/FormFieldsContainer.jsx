import React, { useRef, useState, useEffect, useContext, useCallback } from "react";
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
import CalibrantsTab from "@mp_deposit/mpTabs/CalibrantsTab";
import ModeTab from "@mp_deposit/mpTabs/ModeTab";
import FormButtons from "./FormButtons";
import { FormContext } from "./FormProvider";

function FormFieldsContainer() {
  const community = new URLSearchParams(location.search).get('community');

  const { tabs, selectedTab, setSelectedTab, setFileUploadErrors, setSavedAt, setIsSaving } = useContext(FormContext);
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

  const handleUpload = useCallback(async () => {
    if (fileUploaderRef.current) {
      await fileUploaderRef.current.submitFiles();
    }
  }, []);

  const handleSaveMetadataAndFiles = useCallback(async () => {
    await handleUpload();
    await save();
  }, [save, handleUpload]);

  useEffect(() => {
    const handleKeyDown = async (e) => {
      if (e.key !== "Enter") return;
      
      const target = e.target;
      const tag = target?.tagName?.toLowerCase();
      if (tag === "textarea" || target?.isContentEditable) return;
      
      e.preventDefault();
      setIsSaving(true);
      await handleSaveMetadataAndFiles();
      setSavedAt(Date.now());
      setIsSaving(false);
    };

    window.addEventListener("keydown", handleKeyDown);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [handleSaveMetadataAndFiles, setSavedAt, setIsSaving]);

  return (
    <>
      <div className="flex ml-1">
        <FormButtons handleSaveMetadataAndFiles={handleSaveMetadataAndFiles} />
      </div>

      <div
          className="mt-3 mb-4 ml-1 mr-1 rounded-normal border border-yellow-300 bg-yellow-50 px-4 py-3 text-sm text-yellow-900">
        <div className="font-JostBold mb-1">
          Do not forget to SAVE
        </div>
        <div>
          Please save your draft regularly while filling in the form, especially before switching tabs, uploading files, leaving the page, and before you submit for review.
        </div>
      </div>

      <div className="flex justify-center -mb-16">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[75vh] max-h-[900px]">
            <div className="bg-dark flex flex-col p-2 rounded-tl-[0.2rem] rounded-bl-[0.2rem]">
              {tabs?.map((tab) => (
                <button
                  key={tab.value}
                  className={`py-3 pl-4 pr-6 mb-2 text-[.95rem] font-JostBold text-left cursor-pointer rounded-normal hover:bg-primary hover:text-dark ${
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
                  You are depositing MP data
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
                          recordMetadata={recordMetadata}
                          setFileUploadErrors={setFileUploadErrors}
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
                      selectedTab === "calibrants" ? "" : "hidden"
                    }`}
                  >
                    <CalibrantsTab name="metadata.method_specific_parameters" />
                  </div>
                  <div className={`${selectedTab === "mode" ? "" : "hidden"}`}>
                    <ModeTab name="metadata.method_specific_parameters.mode" />
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
