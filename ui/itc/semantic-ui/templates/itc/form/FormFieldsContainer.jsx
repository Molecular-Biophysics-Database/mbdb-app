import React from 'react'
import {useState, useEffect} from 'react'
import { useLocation } from 'react-router-dom';
import RawMeasurementFilesTab from '@mbdb_deposit/general/generalTabs/RawMeasurementFilesTab';
import EntitiesOfInterestTab from "@mbdb_deposit/general/generalTabs/EntitiesOfInterestTab";
import ChemicalEnvironmentTab from '@mbdb_deposit/general/generalTabs/ChemicalEnvironmentTab'
import ResultTab from "@mbdb_deposit/general/generalTabs/ResultTab";
import ProjectInformationTab from "@mbdb_deposit/general/generalTabs/ProjectInformationTab";
import InstrumentTab from "@itc_deposit/itcTabs/InstrumentTab";
import MeasurementsTab from "@itc_deposit/itcTabs/MeasurementsTab";
import DataAnalysisTab from "@itc_deposit/itcTabs/DataAnalysisTab";

function FormFieldsContainer() {

    const Tabs = [
      { value: 'raw-measurement-files', label: 'Raw measurement files' },
      { value: 'project-information', label: 'Project information' },
      { value: 'entities-of-interest', label: 'Entities of interest' },
      { value: 'chemical-environment', label: 'Chemical environments' },
      { value: 'result', label: 'Results' },
      { value: 'instrument', label: 'Instrument' },
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
      <div className='flex justify-center'>
        <div className='bg-primary border-dark border-solid border-[.1px] rounded-normal'>
          <div className='flex justify-center w-fit h-[90vh]'>
            <div className="bg-dark rounded-tl-normal rounded-bl-normal">
              {Tabs.map(tab => (
                  <div 
                    key={tab.value} 
                    className={`py-5 px-6 font-JostBold cursor-pointer rounded-tl-normal rounded-bl-normal hover:bg-primary hover:text-dark ${state.selected === tab.value ? 'bg-primary text-dark' : 'text-white'}`}
                    onClick={() => setState({ selected: tab.value })}
                  >
                  {tab.label}
                  </div>
              ))}
            </div>
            <div className='overflow-y-scroll overflow-x-hidden'>
              <div className="flex flex-col w-[1200px]">
                <div className="flex text-dark font-JostBold text-24px mt-4 ml-6">
                  You are depositing ITC data
                </div>
                <div className='m-6'>
                  <div className={`${state.selected === 'raw-measurement-files' ? '' : 'hidden'}`}>
                    <RawMeasurementFilesTab name='metadata.general_parameters' />
                  </div>
                  <div className={state.selected === 'raw-measurement-files' ? 'hidden' : ''}>
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
                    {state.selected === 'measurements' && (
                        <MeasurementsTab name='metadata.method_specific_parameters' />
                    )}
                    {state.selected === 'data-analysis' && (
                      <DataAnalysisTab name='metadata.method_specific_parameters' />
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
