import omit from "lodash/omit";

// rdm-12 behaviour: a new measurement is a copy of the last one without its
// position (the new id comes from ModalArrayField's withIds).
export const nextMeasurement = (measurements) =>
  omit(measurements?.[measurements.length - 1] ?? {}, ["id", "position"]);

// Names repeat between replicates, so the position tells them apart.
export const describeMeasurement = (measurement) =>
  [
    measurement.name,
    measurement.position && `(position ${measurement.position})`,
  ]
    .filter(Boolean)
    .join(" ");
