import React from "react";
import { Header, List } from "semantic-ui-react";
import _join from "lodash/join";
import { getTitleFromMultilingualObject } from "@js/oarepo_ui";

export const VocabularyItem = ({
  onSelect,
  result,
  selected,
  title,
  uriLinks,
  propValues
}) => {

  return (
    <List.Item
      onClick={() => onSelect(result)}
      className="search-external-result-item"
      active={selected}
    >
      <List.Content>
        <Header className="mb-5" size="small">
          {getTitleFromMultilingualObject(title)} {uriLinks}
        </Header>
        <List.Description>{propValues}</List.Description>
      </List.Content>
    </List.Item>
  );
};





