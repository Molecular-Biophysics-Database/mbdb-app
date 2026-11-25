// The OpenStreetMap marker URL for a coordinate pair: pins lat/lon and
// centers the map on them at zoom 10. Pure, so the exact format is testable.
export const mapUrl = (lat, lon) =>
  `https://www.openstreetmap.org/?mlat=${lat}&mlon=${lon}#map=10/${lat}/${lon}`;
