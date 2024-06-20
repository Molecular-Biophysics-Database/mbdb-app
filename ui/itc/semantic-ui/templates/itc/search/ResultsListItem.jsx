import React, { useContext } from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import { withState, buildUID } from "react-searchkit";
import { SearchConfigurationContext } from "@js/invenio_search_ui/components";

const ItemHeader = ({ title, searchUrl, selfLink, id, releasedDate, givenName, familyName, affiliationsTitle, technique, entitiesOfInterest, results}) => {
  return (
    <div className="lg:max-w-[1024px] lg:m-auto xl:max-w-[1280px] 2xl:max-w-[1440px] !my-10 !mx-6 pb-10 text-dark border-b-dark border-b-[.1px] first:!mt-16 md:!mx-12">
      <div className="flex justify-between flex-col lg:flex-row">
        <div className="font-JostMedium text-32px">
          <a href={selfLink}>{title}</a>
        </div>
        <div className="flex text-24px font-JostMedium">
          <div className="mr-3 font-bold text-accent-secondary">
            ID
          </div>
          <div>
           {id}
          </div>
        </div>
      </div>
      <div className="flex justify-between flex-col lg:flex-row">
        <div className="text-20px my-4">
          <div className="my-2">{releasedDate}</div>
          <div className="flex">
            <div className="my-2">{givenName} {familyName}</div>
            <div className="my-auto mx-2">/</div>
            <div className="my-2">{affiliationsTitle}</div>
          </div>
          <div className="flex">
            <div className="my-2 font-JostMedium text-accent-secondary">Technique:</div>
            <div className="my-2 !ml-2">{technique}</div>
          </div>
          <div className="flex">
            <div className="my-2 font-JostMedium text-accent-secondary">Results:</div>
            <div className="my-2 flex">{results}</div>
          </div>
          <div className="flex">
            <div className="my-2 font-JostMedium text-accent-secondary">Entities of interest:</div>
            <div className="my-2">{entitiesOfInterest}</div>
          </div>
        </div>
      </div>
    </div>
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
  const releasedDate = _get(generalParams, "record_information.deposition_date", "");
  const technique = _get(generalParams, "technique", "");
  const id = _get(result, "id", "");
  const contactGivenName = _get(generalParams, "depositors.principal_contact.given_name", "");
  const contactFamilyName = _get(generalParams, "depositors.principal_contact.family_name", "");
  const affiliations = _get(generalParams, "depositors.principal_contact.affiliations", []);
  const entitiesOfInterest =  _get(generalParams, "entities_of_interest", []);
  const results =  _get(generalParams, "results", []);

  const affiliationTitle = affiliations.map(affiliations => <div>{affiliations.title}</div>)
  const entitiesOfInterestNames = entitiesOfInterest.map((eoi) => <div className="mbdbv-chemical-name inline ml-2">{eoi.name}</div>)
  const resultNames = results.map((result) => <div className="mbdbv-chemical-name inline ml-2">{result.name}</div>)


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
            selfLink={result.links.self_html}
            releasedDate={releasedDate}
            technique={technique}
            id={id}
            givenName={contactGivenName}
            familyName={contactFamilyName}
            affiliationsTitle={affiliationTitle}
            entitiesOfInterest={entitiesOfInterestNames}
            results={resultNames}
          />
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