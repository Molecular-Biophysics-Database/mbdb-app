import React from 'react'
import {useState, useEffect} from 'react'
import { useLocation } from 'react-router-dom';
import RawDataFilesTab from "@mbdb_deposit/general/generalTabs/RawDataFilesTab";
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import ChemicalEnvironmentTab from '@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab'
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import ProjectInformationTab from "@mbdb_deposit/general/generalTabs/ProjectInformationTab";
import InstrumentTab from "@spr_deposit/sprTabs/InstrumentTab";
import MeasurementProtocolTab from "@spr_deposit/sprTabs/MeasurementProtocolTab";
import MeasurementsTab from "@spr_deposit/sprTabs/MeasurementsTab";
import DataAnalysisTab from "@spr_deposit/sprTabs/DataAnalysisTab";
import SensorTab from "@spr_deposit/sprTabs/SensorTab";
import MeasurementPositionsTab from "@spr_deposit/sprTabs/MeasurementPositionsTab";

function FormFieldsContainer() {

    const Tabs = [
      { value: 'raw-data-files', label: 'Raw data files' },
      { value: 'project-information', label: 'Project information' },
      { value: 'entities-of-interest', label: 'Entities of interest' },
      { value: 'chemical-environment', label: 'Chemical environments' },
      { value: 'result', label: 'Results' },
      { value: 'instrument', label: 'Instrument' },
      { value: 'sensor', label: 'Sensor' },
      { value: 'measurement-positions', label: 'Measurement positions' },
      { value: 'measurement-protocol', label: 'Measurement protocol' },
      { value: 'measurements', label: 'Measurements' },
      { value: 'data-analysis', label: 'Data analysis' },
    ];

    const location = useLocation();
    const [state, setState] = useState({ selected: 'project-information' });
  
    useEffect(() => {
      const selectedTab = location?.state?.selectedTab || 'project-information';
      setState({ selected: selectedTab });
    }, [location]);

  return (
    <>
      <div className="flex text-dark text-24px font-bold justify-center mt-4">
        You are depositing SPR data
      </div>
      <div className='flex justify-center m-4'>
        <div className="mr-3">
          {Tabs.map(tab => (
              <div 
              key={tab.value} 
              className={`text-dark p-4 mb-3 font-bold rounded-lg cursor-pointer transition-all hover:bg-primary-light ${state.selected === tab.value ? 'active bg-primary' : ''}`}
              onClick={() => setState({ selected: tab.value })}
              >
              {tab.label}
              </div>
          ))}
        </div>
        <div className="w-[1000px]">
          <div className={`${state.selected === 'raw-data-files' ? '' : 'hidden'}`}>
            <RawDataFilesTab name='metadata.general_parameters' />
          </div>
          <div className={state.selected === 'raw-data-files' ? 'hidden' : ''}>
            {state.selected === 'project-information' && (
              <ProjectInformationTab name='metadata.general_parameters' />
            )}
            {state.selected === 'entities-of-interest' && (
              <EntitiesOfInterestTab name='metadata.general_parameters' />
            )}
            {state.selected === 'chemical-environment' && (
              <ChemicalEnvironmentTab name='metadata.general_parameters' />
            )}
            {state.selected === 'result' && (
              <ResultTab name='metadata.general_parameters'/>
            )}
            {state.selected === 'instrument' && (
              <InstrumentTab name='metadata.general_parameters' />
            )}
            {state.selected === 'sensor' && (
              <SensorTab name='metadata.method_specific_parameters' />
            )}
            {state.selected === 'measurement-positions' && (
              <MeasurementPositionsTab name='metadata.method_specific_parameters' />
            )}
            {state.selected === 'measurement-protocol' && (
              <MeasurementProtocolTab name='metadata.method_specific_parameters' />
            )}
            {state.selected === 'measurements' && (
              <MeasurementsTab name='metadata.method_specific_parameters' />
            )}
            {state.selected === 'data-analysis' && (
              <DataAnalysisTab name='metadata.method_specific_parameters' />
            )}
          </div>
        </div>
      </div>
    </>
  );
}

export default FormFieldsContainer;
