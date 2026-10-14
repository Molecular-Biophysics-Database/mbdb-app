// Copied from the YAML enums in models/general_parameters-definitions-rdm.yaml
// (Size.type enum and LENGTH_UNITS); tests compare them with the same YAML
// values. μm uses the Greek letter mu (U+03BC): the visually identical micro
// sign µ (U+00B5) is a different string the server rejects. Å is U+00C5.
export const SIZE_TYPES = ["radius", "diameter", "path length"];
export const LENGTH_UNITS = ["Å", "nm", "μm", "mm", "cm", "m"];
