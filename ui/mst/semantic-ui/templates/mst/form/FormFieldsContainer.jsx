import React from 'react'
import {useState, useEffect} from 'react'
import { useLocation } from 'react-router-dom';
import RawDataFiles from "@mst_deposit/tabs/RawDataFiles";
import EntitiesOfInterestTab from "@mst_deposit/tabs/EntitiesOfInterestTab";
import InstrumentTab from "@mst_deposit/tabs/InstrumentTab";
import ChemicalEnvironmentTab from '@mst_deposit/tabs/ChemicalEnvironmentTab'
import ResultTab from "@mst_deposit/tabs/ResultTab";
import DataAnalysisTab from "@mst_deposit/tabs/DataAnalysisTab";
import ProjectInformationTab from "@mst_deposit/tabs/ProjectInformationTab";
import MeasurementTab from "@mst_deposit/tabs/MeasurementTAb";

function FormFieldsContainer() {

    const Tabs = [
        { value: 'raw-data-files', label: 'Raw data files' },
        { value: 'project-information', label: 'Project information' },
        { value: 'entities-of-interest', label: 'Entities of interest' },
        { value: 'chemical-environment', label: 'Chemical environments' },
        { value: 'result', label: 'Results' },
        { value: 'instrument', label: 'Instrument' },
        { value: 'measurement', label: 'Measurements' },
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
        <div className='flex justify-center m-4'>
            <div className="relative top-0 left-0 mt-4 mr-3">
              {Tabs.map(tab => (
                  <div 
                  key={tab.value} 
                  className={`text-dark p-4 mb-3 rounded-lg cursor-pointer transition-all hover:bg-primary-light ${state.selected === tab.value ? 'active bg-primary' : ''}`}
                  onClick={() => setState({ selected: tab.value })}
                  >
                  {tab.label}
                  </div>
              ))}
            </div>
            <div className="w-[1200px]">
              {state.selected === 'raw-data-files' && (
                <RawDataFiles name='metadata.general_parameters' />
              )}
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
              {state.selected === 'measurement' && (
                <MeasurementTab name='metadata.method_specific_parameters' />
              )}
              {state.selected === 'data-analysis' && (
                <DataAnalysisTab name='metadata.method_specific_parameters' />
              )}
          </div>
        </div>
    </>
  );
}

export default FormFieldsContainer;
