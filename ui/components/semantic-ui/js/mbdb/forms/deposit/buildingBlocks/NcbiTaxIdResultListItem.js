import React from "react";
import _join from "lodash/join";
import { VocabularyUri } from "./VocabularyUri";
import { VocabularyItem } from "./VocabularyItem";

export const NcbiTaxIdResultListItem = ({
  result,
  handleSelect = () => {},
  selected,
}) => {

  const { relatedURI, title, props } = result;

  const uriLinks = VocabularyUri(relatedURI)

  const propValues = props.rank;

  const onSelect = (result) => {
    handleSelect(result, selected);
  };

  return VocabularyItem({ onSelect, result, selected, title, uriLinks, propValues });
};
