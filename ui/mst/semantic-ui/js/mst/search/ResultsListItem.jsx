import React from "react";
import PropTypes from "prop-types";

const formatDate = (date) =>
  new Date(date).toLocaleDateString(document.documentElement.lang || "en", {
    dateStyle: "medium",
    timeZone: "UTC",
  });

const Row = ({ label, children }) =>
  children ? (
    <div className="mbdb-result-row">
      <span className="mbdb-result-label">{label}:</span> {children}
    </div>
  ) : null;

Row.propTypes = {
  label: PropTypes.string.isRequired,
  children: PropTypes.node,
};

Row.defaultProps = {
  children: null,
};

// Ported from the mbdb-app-rdm-12 result list item
export const ResultsListItem = ({ result }) => {
  const {
    record_information: info = {},
    depositors,
    method,
    results = [],
    entities_of_interest: entities = [],
  } = result.metadata?.general_parameters ?? {};
  const contact = depositors?.principal_contact ?? {};
  const contactLine = [
    [contact.given_name, contact.family_name].filter(Boolean).join(" "),
    (contact.affiliations ?? []).map(({ name }) => name).filter(Boolean).join(", "),
  ].filter(Boolean);
  const names = (items) => items.map(({ name }) => name).filter(Boolean).join(", ");

  return (
    <article className="mbdb-result" data-testid="result-item">
      <div className="mbdb-result-header">
        <h2>
          <a href={result.links.self_html}>{info.title || "Untitled record"}</a>
        </h2>
        <div className="mbdb-result-id">
          <span className="mbdb-result-label">ID</span> {result.id}
        </div>
      </div>
      {info.deposition_date && (
        <div className="mbdb-result-row">{formatDate(info.deposition_date)}</div>
      )}
      {contactLine.length > 0 && (
        <div className="mbdb-result-row">{contactLine.join(" / ")}</div>
      )}
      <Row label="State">
        <span className={`mbdb-result-state mbdb-result-state-${result.state}`}>
          {result.state?.replaceAll("_", " ")}
        </span>
      </Row>
      <Row label="Method">{method}</Row>
      <Row label="Results">{names(results)}</Row>
      <Row label="Entities of interest">{names(entities)}</Row>
    </article>
  );
};

ResultsListItem.propTypes = {
  result: PropTypes.object.isRequired,
};

export default ResultsListItem;
