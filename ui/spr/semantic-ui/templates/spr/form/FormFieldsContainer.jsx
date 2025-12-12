import React, { useRef, useState, useEffect, useContext } from "react";
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
import FormButtons from "./FormButtons";
import { FormContext } from "./FormProvider";

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
      <div className="flex mb-2 ml-1">
        <FormButtons handleSaveMetadataAndFiles={handleSaveMetadataAndFiles} />
      </div>
      <div className="flex justify-center">
        <div className="bg-primary border-dark border-solid border-[.1px] rounded-normal">
          <div className="flex justify-center w-fit h-[75vh] max-h-[900px]">
            <div className="bg-dark flex flex-col p-2 rounded-tl-[0.2rem] rounded-bl-[0.2rem]">
              {tabs?.map((tab) => (
                <button
                  key={tab.value}
                  className={`py-3 pl-4 pr-6 mb-2 text-[.95rem] font-JostBold cursor-pointer text-left rounded-normal hover:bg-primary hover:text-dark ${
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
                  You are depositing SPR data
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
