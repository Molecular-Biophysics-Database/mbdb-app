// The absolute path of the section's array, in its own module (no
// react-searchkit) so the record serializer can import it too. Guide §5: only
// the section knows the absolute path; the serializer applies the one-time id
// pass on load (design EntitiesOfInterest.md, "Legacy entities without id").
export const ENTITIES_OF_INTEREST_PATH =
  "metadata.general_parameters.entities_of_interest";
