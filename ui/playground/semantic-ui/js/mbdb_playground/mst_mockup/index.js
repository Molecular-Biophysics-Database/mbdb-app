// The MST deposit form in its entirety, as a playground mockup
// (/playground/mst-mockup): the real DepositFormApp — the same component,
// sections and overrides as the real form in ui/mst/semantic-ui/js/mst/forms
// — with the record from sample_data/mst/MST.json as the initial draft.
// No backend: the mocked deposit services echo the saved draft back, so the
// form behaves like the real one (save button, URL update) without calls.

import React, { useState } from "react";
import PropTypes from "prop-types";
import ReactDOM from "react-dom";
import { DepositFormApp } from "@js/oarepo_ui/forms";
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
import mstRecord from "../stories/data/mst.json";

const rootEl = document.getElementById("mst-mockup-form");
const uiModel = JSON.parse(rootEl.dataset.uiModel || "{}");

// The real form's config (oarepo_ui form_config: overridableIdPrefix is
// "<application_id capitalized>.Form") plus the mst ui_model the page passes,
// so the fields get the model labels and help.
const config = {
  overridableIdPrefix: "Mst.Form",
  default_locale: "en",
  custom_fields: { ui: [], vocabularies: {} },
  ui_model: uiModel,
};

// The mocked backend: saving echoes the draft back the way the deposit API
// answers a create (an id and links), so the save button works offline.
const draftsService = {
  save: async (draft) => ({
    data: {
      ...draft,
      id: draft.id || "mst-mockup",
      links: { ...draft.links, self_html: window.location.href },
    },
  }),
};
const filesService = {
  setProgressNotifier: () => {},
};
const depositService = { drafts: draftsService, files: filesService };

// The Review toggle, the same as the real form's (design ReviewMode.md).
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
  "Mst.Form.TabForm.actions": () => (
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
        record={mstRecord}
        files={{}}
        permissions={{}}
        apiClient={{}}
        fileApiClient={{}}
        filesService={filesService}
        depositService={depositService}
        recordSerializer={new MbdbDepositRecordSerializer()}
        sections={sections}
        componentOverrides={componentOverrides}
        useWizardForm
      />
    </ReviewModeRoot>
  </HelpModeProvider>,
  rootEl
);
