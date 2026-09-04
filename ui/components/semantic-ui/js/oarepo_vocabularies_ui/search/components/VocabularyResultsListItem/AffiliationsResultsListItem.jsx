import React, { useContext } from "react";
import PropTypes from "prop-types";
import { Item } from "semantic-ui-react";
import Overridable from "react-overridable";
import { AppContext } from "react-searchkit";
import { I18nString } from "@js/oarepo_ui";
import { VocabularyItemIdentifiers } from "./VocabularyItemIdentifiers";

export const AffiliationsResultsListItem = ({ result }) => {
  const { buildUID } = useContext(AppContext);
  const {
    id,
    title,
    identifiers,
    links: { self_html },
  } = result;

  return (
    <Overridable
      id={buildUID("AffiliationsResultsListItem.layout")}
      result={result}
    >
      <Item key={id}>
        <Item.Content>
          <Item.Header as="h3">
            <a href={self_html}>
              <I18nString value={title} />
            </a>
          </Item.Header>
          <Item.Meta>
            <VocabularyItemIdentifiers identifiers={identifiers} />
          </Item.Meta>
        </Item.Content>
      </Item>
    </Overridable>
  );
};

AffiliationsResultsListItem.propTypes = {
  result: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title: PropTypes.oneOfType([PropTypes.string, PropTypes.object]).isRequired,
    identifiers: PropTypes.arrayOf(
      PropTypes.shape({
        identifier: PropTypes.string.isRequired,
        scheme: PropTypes.string.isRequired,
      })
    ),
    links: PropTypes.shape({
      self: PropTypes.string,
      self_html: PropTypes.string,
    }).isRequired,
    props: PropTypes.object,
  }).isRequired,
};
