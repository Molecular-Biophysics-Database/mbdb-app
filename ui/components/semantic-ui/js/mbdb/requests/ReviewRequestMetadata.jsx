import React, { useEffect, useRef } from "react";
import PropTypes from "prop-types";
import RequestMetadata from "@js/invenio_requests/request/RequestMetadata";

// The upstream component, not the overridden one, which would be this file again
const OriginalMetadata = RequestMetadata.originalComponent;

/**
 * Upstream links to /records/<id>, which does not exist for drafts, under the
 * request's title. The page header has the right link (macros/record_title.html);
 * without it the request is not a review one or its record cannot be read.
 */
export const ReviewRequestMetadata = ({ request, ...props }) => {
  const link = document.querySelector(".mbdb-request-record");
  const ref = useRef(null);

  // upstream's link takes no props, copy the new tab attributes onto it
  useEffect(() => {
    const recordLink = ref.current?.querySelector('a[href^="/records/"]');
    if (!recordLink) return;
    ["target", "rel", "title"].forEach((name) =>
      recordLink.setAttribute(name, link.getAttribute(name))
    );
  }, [link]);

  if (!link) return <OriginalMetadata request={request} {...props} />;

  // the receiver is the role of the reviewers listed above it
  // eslint-disable-next-line no-unused-vars
  const { receiver, ...expanded } = request.expanded;
  return (
    <div ref={ref}>
      <OriginalMetadata
        {...props}
        request={{
          ...request,
          title: link.textContent.trim(),
          topic: { record: `${request.topic.record}${link.search}` },
          expanded,
        }}
      />
    </div>
  );
};

ReviewRequestMetadata.propTypes = {
  request: PropTypes.object.isRequired,
};
