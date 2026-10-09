import React from "react";
import PropTypes from "prop-types";
import { useFormikContext, getIn } from "formik";
import { ExternalLink } from "@js/mbdb/forms/building-blocks/ExternalLink";
import { mapUrl } from "./mapUrl";

// Opens OpenStreetMap at the entered coordinates, to check them visually.
// Shown only once both latitude and longitude are numbers: the map needs
// both, and an error string would make a broken URL.
export const MapLink = ({ fieldPath }) => {
  const { values } = useFormikContext();
  const lat = getIn(values, `${fieldPath}.latitude`);
  const lon = getIn(values, `${fieldPath}.longitude`);
  if (typeof lat !== "number" || typeof lon !== "number") return null;
  return <ExternalLink href={mapUrl(lat, lon)}>Show on map ↗</ExternalLink>;
};

MapLink.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
