import React from "react";
import PropTypes from "prop-types";
import { Button, Icon } from "mbdb-semantic-ui-react";

// A small link to an external page, opened in a new tab. An anchor, so no
// type="button". A falsy href renders nothing, so a caller with no URL to
// point at needs no condition of its own.
export const ExternalLink = ({ href, children }) =>
  href ? (
    <Button
      basic
      size="mini"
      as="a"
      href={href}
      target="_blank"
      rel="noreferrer"
    >
      {children} <Icon name="external alternate" fitted />
    </Button>
  ) : null;

ExternalLink.propTypes = {
  href: PropTypes.string,
  children: PropTypes.node,
};
