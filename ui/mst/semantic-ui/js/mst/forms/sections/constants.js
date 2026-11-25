export const INSTRUMENT_PATH = "metadata.general_parameters.instrument";
export const METHOD_PATH = "metadata.method_specific_parameters";
export const MEASUREMENTS_PATH = `${METHOD_PATH}.measurements`;
export const DATA_ANALYSIS_PATH = `${METHOD_PATH}.data_analysis`;

// Copied from the enums in models/mst/mst-definitions.yaml
export const EXPERIMENT_TYPES = ["Affinity", "Concentration", "Other"];
export const SIGNAL_TYPES = ["Initial intensity", "TRIC/MST", "Spectral shift"];
export const EXCITATION_LED_COLORS = [
  "RED (ex 605-645nm, em 660-720nm)",
  "RED (ex 610-645nm, em 680-720nm)",
  "GREEN (ex 555-585nm, em 605-690nm)",
  "GREEN (ex 515-550nm, em 565-600nm)",
  "BLUE (ex 480-500nm, em 515-550nm)",
  "BLUE (ex 460-500nm, em 515-560nm)",
  "UV (ex 260-300nm, em 330-380nm)",
  "Spectral shift",
];
export const MEASUREMENT_CONTAINERS = [
  "Monolith Standard Capillary",
  "Monolith Premium Capillary",
  "Monolith LabelFree Capillary",
  "Monolith LabelFree Premium Capillary",
  "Monolith NT.Automated Capillary Chip",
  "Monolith NT.Automated Premium Capillary Chip",
  "Monolith NT.Automated LabelFree Capillary Chip",
  "Monolith NT.Automated LabelFree Premium Capillary Chip",
  "384-well plate",
  "other",
];
export const QUALITY_TYPES = [
  "R^2",
  "SEM",
  "red. Chi^2",
  "1sigma",
  "2sigma",
  "3sigma",
  "5sigma",
  "Skewness",
];

// Copied from models/mst/files.py
export const FILE_CONTENT_TYPES = ["Text", "Binary", "Text and binary"];
export const FILE_CONTEXTS = [
  "Raw measurement data",
  "Derived measurement data",
  "Quality control report",
];
export const FILE_ORIGINS = ["Instrument software", "User", "MBDB"];
