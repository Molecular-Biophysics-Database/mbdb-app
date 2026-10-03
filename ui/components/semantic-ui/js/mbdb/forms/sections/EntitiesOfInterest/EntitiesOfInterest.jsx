import React from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";
import { buildUID } from "react-searchkit";
import { Message } from "mbdb-semantic-ui-react";
import { ENTITIES_OF_INTEREST_PATH } from "./path";

// Placeholder until plan step 5; the real content is designed in
// conversion_docs/poc/design/EntitiesOfInterest.md
const EntitiesOfInterestSectionComponent = ({ formConfig }) => (
  <Overridable
    id={buildUID(formConfig?.overridableIdPrefix, "EntitiesOfInterest")}
  >
    <Message info>
      <Message.Header>Entities of interest</Message.Header>
      <p>This section is under construction.</p>
    </Message>
  </Overridable>
);

EntitiesOfInterestSectionComponent.propTypes = {
  formConfig: PropTypes.object.isRequired,
};

export const EntitiesOfInterestSection = {
  key: "entities-of-interest",
  label: "Entities of interest",
  component: EntitiesOfInterestSectionComponent,
  includesPaths: [ENTITIES_OF_INTEREST_PATH],
};

export { ENTITIES_OF_INTEREST_PATH } from "./path";
