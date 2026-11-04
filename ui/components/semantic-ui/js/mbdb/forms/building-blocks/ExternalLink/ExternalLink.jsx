import React from "react";
import PropTypes from "prop-types";
import { Button, Icon } from "mbdb-semantic-ui-react";

// A small link to an external page, opened in a new tab. `plain` renders a bare
// anchor (a link, not a button — design DetailView §2b rule 7); the default is
// a small basic button. A falsy href renders nothing, so a caller with no URL to
// point at needs no condition of its own.
export const ExternalLink = ({ href, children, plain }) => {
  if (!href) return null;
  const content = (
    <>
      {children} <Icon name="external alternate" fitted />
    </>
  );
  const props = { href, target: "_blank", rel: "noreferrer" };
  return plain ? (
    <a className="mbdb-link" {...props}>
      {content}
    </a>
  ) : (
    <Button basic size="mini" as="a" {...props}>
      {content}
    </Button>
  );
};

ExternalLink.propTypes = {
  href: PropTypes.string,
  children: PropTypes.node,
  plain: PropTypes.bool,
};
