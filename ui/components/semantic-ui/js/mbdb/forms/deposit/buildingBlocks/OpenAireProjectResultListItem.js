import React from "react";
import _join from "lodash/join";
import { VocabularyUri } from "./VocabularyUri";
import { VocabularyItem } from "./VocabularyItem";

export const OpenAireProjectResultListItem = ({
  result,
  handleSelect = () => {},
  selected,
}) => {

  const { relatedURI, title, props } = result;
  const uriLinks = VocabularyUri(relatedURI)
  const displayProps = (({ grant_id, funder_name }) => ({ grant_id, funder_name }))(props);
  const propValues = _join(Object.values(displayProps), ", ");

  const onSelect = (result) => {
    handleSelect(result, selected);
  };

  return VocabularyItem({ onSelect, result, selected, title, uriLinks, propValues });
};
