import React from "react";
import _join from "lodash/join";
import { VocabularyUri } from "./VocabularyUri";
import { VocabularyItem } from "./VocabularyItem";


export const PubChemResultListItem = ({
  result,
  handleSelect = () => {},
  selected,
}) => {

  // in addition to the props field, chemical vocabulary also has
  // custom fields so we unpack it slight different than for other
  // vocabularies.
  const { relatedURI, title, ...props } = result;

  const uriLinks = VocabularyUri(relatedURI)

  // remove 'inchikey:'
  const inchikey = props.id.slice(9);
  // combine molecular weight value:unit pair into string
  const MW = _join(Object.values(props.molecular_weight), " ");
  const propValues = _join(Object.values({MW, inchikey}), ", ");

  const onSelect = (result) => {
    handleSelect(result, selected);
  };

  return VocabularyItem({ onSelect, result, selected, title, uriLinks, propValues });
};
