import React from "react";
import {
  FieldGroup,
  FieldRow,
  MbdbVocabularyField,
  NumberField,
  SelectField,
  TEMPERATURE_UNITS,
  ValueUnitField,
} from "@js/mbdb/forms";
import {
  EXCITATION_LED_COLORS,
  EXPERIMENT_TYPES,
  INSTRUMENT_PATH,
  METHOD_PATH,
  SIGNAL_TYPES,
} from "./constants";

// Like rdm-12: only MST instruments (an instrument with no technique stays).
export const isMstInstrument = (option) =>
  !option.props?.technique || option.props.technique.startsWith("MST");

const InstrumentSectionComponent = () => (
  <>
    <MbdbVocabularyField
      fieldPath={INSTRUMENT_PATH}
      vocabularyName="instruments"
      optionFilter={isMstInstrument}
    />
    <FieldGroup fieldPath={METHOD_PATH}>
      <FieldRow widths="equal">
        <SelectField
          fieldPath={`${METHOD_PATH}.experiment_type`}
          options={EXPERIMENT_TYPES}
        />
        <SelectField
          fieldPath={`${METHOD_PATH}.signal_type`}
          options={SIGNAL_TYPES}
        />
        <SelectField
          fieldPath={`${METHOD_PATH}.excitation_led_color`}
          label="Excitation LED color"
          options={EXCITATION_LED_COLORS}
        />
      </FieldRow>
      <FieldRow widths="equal">
        <NumberField
          fieldPath={`${METHOD_PATH}.excitation_led_power`}
          label="Excitation LED power"
          min={0}
          max={100}
        />
        <NumberField
          fieldPath={`${METHOD_PATH}.ir_mst_laser_power`}
          label="IR MST laser power"
          min={0}
          max={100}
        />
        <ValueUnitField
          fieldPath={`${METHOD_PATH}.temperature`}
          units={TEMPERATURE_UNITS}
          defaultUnit="°C"
        />
      </FieldRow>
    </FieldGroup>
  </>
);

export const InstrumentSection = {
  key: "instrument",
  label: "Instrument",
  component: InstrumentSectionComponent,
  includesPaths: [
    INSTRUMENT_PATH,
    `${METHOD_PATH}.experiment_type`,
    `${METHOD_PATH}.signal_type`,
    `${METHOD_PATH}.excitation_led_color`,
    `${METHOD_PATH}.excitation_led_power`,
    `${METHOD_PATH}.ir_mst_laser_power`,
    `${METHOD_PATH}.temperature`,
  ],
};
