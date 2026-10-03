import React from "react";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { joinParts } from "@js/mbdb/forms/entities/summary";

// "49.1951, 16.6068"; "" unless both coordinates are present.
const coordinates = (location) =>
  location?.latitude !== undefined && location?.longitude !== undefined
    ? `${location.latitude}, ${location.longitude}`
    : "";

// Text of the entity table's "Details" column: the environment type title and
// the coordinates, e.g. `Fresh water, 49.1951, 16.6068`. Missing parts are left
// out (joinParts). VocabularyValue is a component — never a hook here.
export const summaryEnvironmentalOrigin = (value) =>
  joinParts([
    value?.environment_type?.id ? (
      <VocabularyValue
        vocabulary="environment-types"
        value={value.environment_type}
      />
    ) : (
      ""
    ),
    coordinates(value?.location),
  ]);
