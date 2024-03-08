import React, { useContext } from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import {Item } from "semantic-ui-react";
import { withState, buildUID } from "react-searchkit";
import { SearchConfigurationContext } from "@js/invenio_search_ui/components";

const ItemHeader = ({ title, searchUrl, selfLink, id, keywords, releasedDate, givenName, familyName, affiliationsTitle, technique, entitiesOfInterest, results}) => {
  const viewLink = new URL(
    selfLink,
    new URL(searchUrl, window.location.origin)
  );

  return (
    <div className="mbdbv-search-result-item-container mbdbv-max-width">
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
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Technique:</div>
            <div className="mbdbv-search-result-item mbdbv-search-result-item-description">{technique}</div>
          </div>
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Results:</div>
            <div className="mbdbv-search-result-item flex">{results}</div>
          </div>
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Entities of interest:</div>
            <div className="mbdbv-search-result-item">{entitiesOfInterest}</div>
          </div>
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
  ...rest
}) => {

  const searchAppConfig = useContext(SearchConfigurationContext);

  const generalParams = _get(result, "metadata.general_parameters");
  const title = _get(generalParams, "record_information.title", "<no title>");
  const keywords = _get(generalParams, "record_information.keywords", []);
  const releasedDate = _get(generalParams, "record_information.deposition_date", "");
  const technique = _get(generalParams, "technique", "");
  const id = _get(result, "id", "");
  const contactGivenName = _get(generalParams, "depositors.principal_contact.given_name", "");
  const contactFamilyName = _get(generalParams, "depositors.principal_contact.family_name", "");
  const affiliations = _get(generalParams, "depositors.principal_contact.affiliations", []);
  const entitiesOfInterest =  _get(generalParams, "entities_of_interest", []);
  const results =  _get(generalParams, "results", []);

  const keyword = keywords.map(keywords => <div className="mbdbv-search-result-keyword">{keywords}</div>)
  const affiliationTitle = affiliations.map(affiliations => <div>{affiliations.title}</div>)
  const entitiesOfInterestNames = entitiesOfInterest.map((eoi) => <div className="mbdbv-chemical-name">{eoi.name}</div>)
  const resultNames = results.map((result) => <div className="mbdbv-chemical-name">{result.name}</div>)


  return (
    <>
      <Overridable
        id={buildUID("RecordsResultsListItem.layout", "", searchAppConfig.appName)}
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
            givenName={contactGivenName}
            familyName={contactFamilyName}
            affiliationsTitle={affiliationTitle}
            entitiesOfInterest={entitiesOfInterestNames}
            results={resultNames}
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
};

ResultsListItemComponent.defaultProps = {
  currentQueryState: null,
};

export const ResultsListItem = (props) => {
  const { appName } = useContext(SearchConfigurationContext);
  return (
    <Overridable id={buildUID("ResultsListItem", "", appName)} {...props}>
      <ResultsListItemComponent {...props} />
    </Overridable>
  );
};

ResultsListItem.propTypes = {
  currentQueryState: PropTypes.object,
  result: PropTypes.object.isRequired,
};

ResultsListItem.defaultProps = {
  currentQueryState: null,
};

export const ResultsListItemWithState = withState(
  ({ currentQueryState, updateQueryState, result }) => (
    <ResultsListItem
      currentQueryState={currentQueryState}
      updateQueryState={updateQueryState}
      result={result}
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

export default ResultsListItemWithState