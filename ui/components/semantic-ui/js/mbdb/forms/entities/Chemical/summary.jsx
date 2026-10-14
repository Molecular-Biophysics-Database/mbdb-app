import React from "react";
import PropTypes from "prop-types";
import { hasData } from "@js/mbdb/forms/building-blocks/errors";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { useVocabularyItem } from "@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles";
import { joinParts } from "@js/mbdb/forms/entities/summary";

// The "Details" cell of a chemical entity: the title from the shared
// vocabulary cache, plus the formula when the cache knows it. The hooks live
// here, in the component summaryChemical returns — never in summaryChemical
// itself, which is a plain function called inside a map.
const ChemicalSummary = ({ value }) => {
  const basic = value.basic_information;
  const { customFields } = useVocabularyItem("chemicals", basic.id);
  return joinParts([
    <VocabularyValue key="title" vocabulary="chemicals" value={basic} />,
    customFields?.chemical_formula,
  ]);
};

ChemicalSummary.propTypes = {
  value: PropTypes.shape({
    basic_information: PropTypes.shape({ id: PropTypes.string }).isRequired,
  }).isRequired,
};

// Text of the entity table's "Details" column. "" when there is no basic
// information (SummaryItem then shows "—"). A manual chemical (no id yet)
// shows its typed title.
export const summaryChemical = (value) => {
  const basic = value?.basic_information;
  if (!hasData(basic)) return "";
  if (!basic.id) return basic.title?.en ?? "";
  return <ChemicalSummary value={value} />;
};
