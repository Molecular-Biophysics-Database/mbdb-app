import React, { useContext } from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import { Grid, Item, Label, List, Icon } from "semantic-ui-react";
import { withState, buildUID } from "react-searchkit";
import { SearchConfigurationContext } from "@js/invenio_search_ui/components";

import { i18next } from "@translations/mbdb_mst_ui/i18next";

const ItemHeader = ({ title, searchUrl, selfLink, id, keywords, releasedDate, givenName, familyName, affiliationsTitle, technique, chemicalEnviroment, entitiesOfInterest, organismOfOrigin }) => {
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
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Technique:</div>
            <div className="mbdbv-search-result-item mbdbv-search-result-item-description">{technique}</div>
          </div>
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Chemical enviroment (buffer):</div>
            <div className="mbdbv-search-result-item flex">{chemicalEnviroment}</div>
          </div>
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Entities of interest:</div>
            <div className="mbdbv-search-result-item">{entitiesOfInterest}</div>
          </div>
          <div className="flex">
            <div className="mbdbv-search-result-item mbdbv-search-result-item-title">Organism of origin:</div>
            <div className="mbdbv-search-result-item mbdbv-search-result-item-description">{organismOfOrigin}</div>
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
  const ownerGivenName = _get(generalParams, "record_information.project.owner.given_name", "[]");
  const ownerFamilyName = _get(generalParams, "record_information.project.owner.family_name", "[]");
  const affiliationsTitle = _get(generalParams, "record_information.project.owner.affiliations", "[]");
  const chemicalEnviroment = _get(generalParams, "chemical_information.chemical_environments[0].constituents", "[]");
  const entitiesOfInterestLigands = _get(result, "metadata.method_specific_parameters.measurements[0].sample.ligands", "[]");
  const entitiesOfInterestTargets = _get(result, "metadata.method_specific_parameters.measurements[0].sample.targets", "[]");
  const organismOfOrigin = _get(generalParams, "chemical_information.entities_of_interest[0].source_organism.title", "[]");

  const keyword = keywords.map(keywords => <div className="mbdbv-search-result-keyword">{keywords}</div>)

  const affiliationTitle = affiliationsTitle.map(affiliationsTitle => <div>{affiliationsTitle.title}</div>)

  const chemicalEnv = chemicalEnviroment.map((constituent) => <div className="mbdbv-chemical-name">{constituent.name}</div>)

  const entitiesOfInterestLigand = entitiesOfInterestLigands.map((ligand) => <div className="mbdbv-chemical-name">{ligand.entity.name}</div>)

  const entitiesOfInterestTarget = entitiesOfInterestTargets.map((target) => <div className="mbdbv-chemical-name">{target.entity.name}</div>)

  const entitiesOfInterest = [...entitiesOfInterestLigand, ...entitiesOfInterestTarget];

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
            chemicalEnviroment={chemicalEnv}
            entitiesOfInterest={entitiesOfInterest}
            organismOfOrigin={organismOfOrigin}
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
