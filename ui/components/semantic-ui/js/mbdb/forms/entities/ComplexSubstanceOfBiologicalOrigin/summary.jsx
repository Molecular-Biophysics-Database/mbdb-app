import React from "react";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { joinParts } from "@js/mbdb/forms/entities/summary";

// The per-sub-type part of the entity summary (the "key value"). Each returns
// "" for an empty entity.

export const summaryBodyFluid = (value) =>
  value?.fluid?.id ? (
    <VocabularyValue vocabulary="body-fluids" value={value.fluid} />
  ) : (
    ""
  );

export const summaryCellFraction = (value) =>
  value?.fraction?.id ? (
    <VocabularyValue vocabulary="cell-fractions" value={value.fraction} />
  ) : (
    ""
  );

export const summaryVirion = (value) =>
  joinParts([
    value?.capsid_type ? `${value.capsid_type} capsid` : "",
    value?.envelope_type ? `${value.envelope_type} envelope` : "",
  ]);

// `<organ>, homogenized` / `<organ>, not homogenized` / just `<organ>` when the
// answer is unset. `false` is a real answer (guide §7), so it must be shown.
export const summarySolidTissueSample = (value) => {
  const homogenized =
    value?.homogenized === true
      ? "homogenized"
      : value?.homogenized === false
      ? "not homogenized"
      : "";
  return joinParts([value?.organ ?? "", homogenized]);
};

const SUBTYPE_SUMMARY = {
  "Body fluid": summaryBodyFluid,
  "Cell fraction": summaryCellFraction,
  Virion: summaryVirion,
  "Solid tissue sample": summarySolidTissueSample,
};

// Text of the entity table's "Details" column: `<derived_from>, <source
// organism title>, <sub-type key value>`, e.g. `Body fluid, Homo sapiens,
// Serum`. Missing parts are left out (joinParts). VocabularyValue is a
// component — never a hook here (plan step 4).
export const summaryBiologicalOrigin = (value) =>
  joinParts([
    value?.derived_from,
    value?.source_organism?.id ? (
      <VocabularyValue vocabulary="organisms" value={value.source_organism} />
    ) : (
      ""
    ),
    SUBTYPE_SUMMARY[value?.derived_from]?.(value) ?? "",
  ]);
