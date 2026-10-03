import React from "react";
import { ExternalLink } from "@js/mbdb/forms/building-blocks/ExternalLink";

// A link to an external page, opened in a new tab. A falsy href renders
// nothing, so a caller with no URL needs no condition of its own.
const WithUrl = () => (
  <p>
    With a URL:{" "}
    <ExternalLink href="https://www.rcsb.org/structure/2HCO">
      Open ↗
    </ExternalLink>
  </p>
);

const WithoutUrl = () => (
  <p>
    Without a URL: <ExternalLink>Open ↗</ExternalLink> (nothing renders before
    the parenthesis)
  </p>
);

const story = {
  title: "ExternalLink",
  scenarios: [
    { name: "With a URL", initialValues: {}, render: WithUrl },
    { name: "Without a URL", initialValues: {}, render: WithoutUrl },
  ],
};

export default story;
