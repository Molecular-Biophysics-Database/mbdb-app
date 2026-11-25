import { DepositFormApp, TabForm, parseFormAppConfig } from "@js/oarepo_ui/forms";
import React, { useState } from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { PreviewButton, SaveButton } from "@js/invenio_rdm_records";
import {
  Button,
  DEFAULT_HELP_MODE,
  HelpModeProvider,
  ReviewModeProvider,
  useReviewMode,
  useReviewModeToggle,
} from "mbdb-semantic-ui-react";
import {
  ChemicalEnvironmentsSection,
  EntitiesOfInterestSection,
  MbdbDepositRecordSerializer,
  RecordInformationSection,
  ResultsSection,
  entityHasField,
  requiredCompletion,
} from "@js/mbdb/forms";
import { DataAnalysisSection } from "./sections/DataAnalysis";
import { FilesQuota, FilesSection } from "./sections/Files";
import { MstFileApiClient } from "./sections/newFile";
import { InstrumentSection } from "./sections/Instrument";
import { MeasurementsSection } from "./sections/Measurements";

const { rootEl, config, ...rest } = parseFormAppConfig();
const recordSerializer = new MbdbDepositRecordSerializer();
const fileApiClient = new MstFileApiClient(
  {
    headers: {
      "vnd+json": {
        "Content-Type": "application/json",
        Accept: "application/vnd.inveniordm.v1+json",
      },
    },
  },
  config.default_transfer_type,
  config.enabled_transfer_types
);

// The Review toggle (design ReviewMode.md "Where it is switched on"): flips the
// mode held by ReviewModeRoot; the section re-reads it and remounts its content.
const ReviewToggle = () => {
  const review = useReviewMode();
  const toggle = useReviewModeToggle();
  return (
    <Button
      type="button"
      toggle
      active={review}
      content={review ? "Back to editing" : "Review"}
      onClick={toggle}
    />
  );
};

const sections = [
  RecordInformationSection,
  EntitiesOfInterestSection,
  ChemicalEnvironmentsSection,
  FilesSection,
  InstrumentSection,
  MeasurementsSection,
  ResultsSection,
  DataAnalysisSection,
].map((section) => ({
  // a tab is green only when every required field in it is filled
  sectionCompletion: (props) =>
    requiredCompletion({ ...props, belongs: entityHasField }),
  sectionCompletionThreshold: 1,
  ...section,
}));

// Above the form, as in mbdb-app-rdm-12 (dark, without icons).
const FormActions = () => (
  <div className="mbdb-form-actions">
    <SaveButton primary icon={null} labelPosition={null} content="Save" />
    <PreviewButton primary icon={null} labelPosition={null} />
    <ReviewToggle />
  </div>
);

const componentOverrides = {
  "ReactInvenioDeposit.FileUploaderToolbar.FileList.container": FilesQuota,
  [`${config.overridableIdPrefix}.WizardForm.container`]: () => (
    <>
      <FormActions />
      <TabForm sections={sections} />
    </>
  ),
  // moved above the form
  [`${config.overridableIdPrefix}.TabForm.actions`]: () => null,
};

// The review state lives above DepositFormApp (so Formik is never remounted);
// the section reads it (useReviewMode) and remounts only its own content.
const ReviewModeRoot = ({ children }) => {
  const [review, setReview] = useState(false);
  return (
    <ReviewModeProvider review={review} onToggle={() => setReview((v) => !v)}>
      {children}
    </ReviewModeProvider>
  );
};

ReviewModeRoot.propTypes = { children: PropTypes.node };

ReactDOM.render(
  <HelpModeProvider mode={DEFAULT_HELP_MODE}>
    <ReviewModeRoot>
      <DepositFormApp
        config={config}
        {...rest}
        sections={sections}
        recordSerializer={recordSerializer}
        fileApiClient={fileApiClient}
        componentOverrides={componentOverrides}
        useWizardForm
      />
    </ReviewModeRoot>
  </HelpModeProvider>,
  rootEl
);
