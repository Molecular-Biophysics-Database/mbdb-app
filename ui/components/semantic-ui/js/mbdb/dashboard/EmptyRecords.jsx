import React from "react";
import PropTypes from "prop-types";
import { Button, Header, Segment } from "semantic-ui-react";

// The link in the dashboard header (templates/oarepo/invenio_app_rdm/users/header.html)
const depositUrl = () => document.querySelector(".mbdb-dashboard-new")?.href;

export const EmptyRecords = ({
  queryString,
  userSelectionFilters,
  resetQuery,
}) => {
  const searching = queryString !== "" || userSelectionFilters?.length > 0;
  return (
    <Segment padded="very" textAlign="center">
      <Header as="h2">
        {searching ? "No matching records" : "You have no records yet"}
      </Header>
      {searching ? (
        <Button onClick={resetQuery} content="Clear search" />
      ) : (
        <Button as="a" href={depositUrl()} content="New deposition" />
      )}
    </Segment>
  );
};

EmptyRecords.propTypes = {
  queryString: PropTypes.string.isRequired,
  userSelectionFilters: PropTypes.array,
  resetQuery: PropTypes.func.isRequired,
};

EmptyRecords.defaultProps = {
  userSelectionFilters: [],
};
