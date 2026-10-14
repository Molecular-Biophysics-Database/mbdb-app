import React from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";
import { buildUID } from "react-searchkit";
import { useReviewMode } from "mbdb-semantic-ui-react";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { AssociatedPublication } from "./AssociatedPublication";
import { Depositors } from "./Depositors";
import { FundingReferences } from "./FundingReferences";
import {
  RECORD_INFORMATION_PATH,
  ASSOCIATED_PUBLICATION_PATH,
  DEPOSITORS_PATH,
  FUNDING_REFERENCES_PATH,
} from "./path";

// The first section of the deposit form (design mirrors the former RDM 12
// form's Record information): the record's Title, the optional Associated
// publication behind a plus button, the Depositors (depositor, principal
// contact, contributors) and the Funding references. Review mode (design
// ReviewMode.md rule 2): the content is keyed by the mode, so switching it
// remounts the section and every part re-reads its initial state (all open);
// Formik, above, keeps the values.
export const RecordInformationSectionComponent = ({ formConfig }) => {
  const reviewMode = useReviewMode();
  return (
    <Overridable
      id={buildUID(formConfig?.overridableIdPrefix, "RecordInformation")}
    >
      <React.Fragment key={reviewMode ? "review" : "edit"}>
        <TextField
          fieldPath={`${RECORD_INFORMATION_PATH}.title`}
          help="Short descriptive title of the record"
          required
        />
        <AssociatedPublication />
        <Depositors />
        <FundingReferences />
      </React.Fragment>
    </Overridable>
  );
};

RecordInformationSectionComponent.propTypes = {
  formConfig: PropTypes.object.isRequired,
};

export const RecordInformationSection = {
  key: "record-information",
  label: "Record information",
  component: RecordInformationSectionComponent,
  includesPaths: [
    RECORD_INFORMATION_PATH,
    ASSOCIATED_PUBLICATION_PATH,
    DEPOSITORS_PATH,
    FUNDING_REFERENCES_PATH,
  ],
};

export {
  RECORD_INFORMATION_PATH,
  ASSOCIATED_PUBLICATION_PATH,
  DEPOSITORS_PATH,
  FUNDING_REFERENCES_PATH,
} from "./path";
