import { DepositFormApp, parseFormAppConfig } from "@js/oarepo_ui/forms";
import React, { useState } from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { SaveButton } from "@js/invenio_rdm_records";
import {
  Button,
  DEFAULT_HELP_MODE,
  Grid,
  HelpModeProvider,
  ReviewModeProvider,
  useReviewMode,
  useReviewModeToggle,
} from "mbdb-semantic-ui-react";
import {
  EntitiesOfInterestSection,
  MbdbDepositRecordSerializer,
} from "@js/mbdb/forms";

const { rootEl, config, ...rest } = parseFormAppConfig();
const recordSerializer = new MbdbDepositRecordSerializer();

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

const componentOverrides = {
  [`${config.overridableIdPrefix}.TabForm.actions`]: () => (
    <Grid.Row data-testid="tab-form-actions-row">
      <div className="flex justify-end form-actions-row">
        <div>
          <ReviewToggle />
          <SaveButton />
        </div>
      </div>
    </Grid.Row>
  ),
};

const sections = [EntitiesOfInterestSection];

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
        componentOverrides={componentOverrides}
        useWizardForm
      />
    </ReviewModeRoot>
  </HelpModeProvider>,
  rootEl
);
