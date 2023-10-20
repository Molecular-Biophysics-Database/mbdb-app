import React, { useContext } from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import { Grid, Item, Label, List, Icon } from "semantic-ui-react";
import { withState, buildUID } from "react-searchkit";
import { SearchConfigurationContext } from "@js/invenio_search_ui/components";

import { i18next } from "@translations/mbdb_mst_ui/i18next";

const ItemHeader = ({ title, searchUrl, selfLink, id, keywords, releasedDate, givenName, familyName, affiliationsTitle, technique }) => {
  const viewLink = new URL(
    selfLink,
    new URL(searchUrl, window.location.origin)
  );

  return (
    <div className="mbdbv-search-result-item-container">
      <div className="mbdbv-search-result-item-header-container">
        <div className="mbdbv-h2-title">
          <a href={viewLink}>{title}</a>
        </div>
        <div className="mbdbv-search-result-id-container">
          <div className="mbdbv-search-result-id-text">
            ID
          </div>
          <div>
           {id}
          </div>
        </div>
      </div>
      <div className="mbdbv-search-result-container">
        <div className="mbdbv-text">
          <div className="mbdbv-search-result-item">{releasedDate}</div>
          <div className="mbdbv-affiliations-container">
            <div className="mbdbv-search-result-item">{givenName} {familyName}</div>
            <div className="mbdbv-affiliations-slash mbdbv-search-result-item">/</div>
            <div className="mbdbv-search-result-item">{affiliationsTitle}</div>
          </div>
          <div className="mbdbv-search-result-item">Technique: {technique}</div>
          <div className="mbdbv-search-result-item">Chemical enviroment (buffer):</div>
          <div className="mbdbv-search-result-item">Entities of interest:</div>
          <div className="mbdbv-search-result-item">Organism of origin:</div>
        </div>
        <div className="mbdbv-search-results-keywords">
          {keywords}
        </div>
      </div>
    </div>
  );
};

const ItemSubheader = ({keywords, id}) => {
  // just an example
  return (
    <>
      <Item.Meta>
      </Item.Meta>
    </>
  );
};

export const ResultsListItemComponent = ({
  currentQueryState,
  result,
  appName,
  ...rest
}) => {
  const searchAppConfig = useContext(SearchConfigurationContext);

  const generalParams = _get(result, "metadata.general_parameters");
  const title = _get(generalParams, "record_information.title", "<no title>");
  const keywords = _get(generalParams, "record_information.keywords", []);
  const releasedDate = _get(generalParams, "record_information.deposition_date", "");
  const technique = _get(generalParams, "technique", "");
  const id = _get(result, "id", "");
  const ownerGivenName = _get(generalParams, "record_information.project.owner.given_name", "");
  const ownerFamilyName = _get(generalParams, "record_information.project.owner.family_name", "");
  const affiliationsTitle = _get(generalParams, "record_information.project.owner.affiliations", []);

  const keyword = keywords.map(keywords => <div className="mbdbv-search-result-keyword">{keywords}</div>)

  const affiliationTitle = affiliationsTitle.map(affiliationsTitle => <div>{affiliationsTitle.title}</div>)




  return (
    <>
      <Overridable
        id={buildUID("RecordsResultsListItem.layout", "", appName)}
        result={result}
        title={title}
      >
        <div key={result.id}>
          <ItemHeader
            title={title}
            searchUrl={searchAppConfig.ui_endpoint}
            selfLink={result.id}
            keywords={keyword}
            releasedDate={releasedDate}
            technique={technique}
            id={id}
            givenName={ownerGivenName}
            familyName={ownerFamilyName}
            affiliationsTitle={affiliationTitle}
          />
          <ItemSubheader />
        </div>
      </Overridable>
    </>
  );
};

ResultsListItemComponent.propTypes = {
  currentQueryState: PropTypes.object,
  result: PropTypes.object.isRequired,
  appName: PropTypes.string,
};

ResultsListItemComponent.defaultProps = {
  currentQueryState: null,
  appName: "",
};

export const ResultsListItem = (props) => {
  return (
    <Overridable id={buildUID("ResultsListItem", "", props.appName)} {...props}>
      <ResultsListItemComponent {...props} />
    </Overridable>
  );
};

ResultsListItem.propTypes = {
  currentQueryState: PropTypes.object,
  result: PropTypes.object.isRequired,
  appName: PropTypes.string,
};

ResultsListItem.defaultProps = {
  currentQueryState: null,
  appName: "",
};

export const ResultsListItemWithState = withState(
  ({ currentQueryState, updateQueryState, result, appName }) => (
    <ResultsListItem
      currentQueryState={currentQueryState}
      updateQueryState={updateQueryState}
      result={result}
      appName={appName}
    />
  )
);

ResultsListItemWithState.propTypes = {
  currentQueryState: PropTypes.object,
  result: PropTypes.object.isRequired,
};

ResultsListItemWithState.defaultProps = {
  currentQueryState: null,
};
