import React from "react";
import PropTypes from "prop-types";

import { Grid, Header, Button, Icon, Segment } from "semantic-ui-react";

export const EmptyResultsElement = ({
  queryString,
  searchPath,
  resetQuery,
}) => {

  const handleClick = () => {
    resetQuery();
    window.location.href = '/';
  };

  return (
    <Grid>
      <Grid.Row centered>
        <Grid.Column width={12} textAlign="center">
          <Header as="h2">
            We couldn't find any matches for
            {(queryString && `'${queryString}'`) || "your search"}
          </Header>
        </Grid.Column>
      </Grid.Row>
      <Grid.Row centered>
        <Grid.Column width={8} textAlign="center">
          <Button primary onClick={handleClick}>
            <Icon name="search" />
            Start over
          </Button>
        </Grid.Column>
      </Grid.Row>
      <Grid.Row centered>
        <Grid.Column width={12}>
          <Segment secondary padded size="large">
            <Header as="h3" size="small">
              ProTip!
            </Header>
            <p>
              <a
                href={`${searchPath}?q=metadata.publication_date:[2017-01-01 TO *]`}
              >
                metadata.publication_date:[2017-01-01 TO *]
              </a>{" "}
              will give you all the publications from 2017 until today.
            </p>
            <p>
              For more tips, check out our
              <a href="/help/search" title="Search guide">
                search guide
              </a>
               for defining advanced search queries.
            </p>
          </Segment>
        </Grid.Column>
      </Grid.Row>
    </Grid>
  );
};

EmptyResultsElement.propTypes = {
  queryString: PropTypes.string.isRequired,
  resetQuery: PropTypes.func.isRequired,
  searchPath: PropTypes.string,
};

EmptyResultsElement.defaultProps = {
  searchPath: "",
};
