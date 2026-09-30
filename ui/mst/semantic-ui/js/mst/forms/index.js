import { DepositFormApp, parseFormAppConfig } from "@js/oarepo_ui/forms";
import React from "react";
import ReactDOM from "react-dom";
import { SaveButton } from "@js/invenio_rdm_records";
import {
  DEFAULT_HELP_MODE,
  Grid,
  HelpModeProvider,
} from "mbdb-semantic-ui-react";
import {
  EntitiesOfInterestSection,
  MbdbDepositRecordSerializer,
} from "@js/mbdb/forms";

const { rootEl, config, ...rest } = parseFormAppConfig();
const recordSerializer = new MbdbDepositRecordSerializer();

const componentOverrides = {
  [`${config.overridableIdPrefix}.TabForm.actions`]: () => (
    <Grid.Row data-testid="tab-form-actions-row">
      <div className="flex justify-end form-actions-row">
        <div>
          <SaveButton />
        </div>
      </div>
    </Grid.Row>
  ),
};

const sections = [EntitiesOfInterestSection];

ReactDOM.render(
  <HelpModeProvider mode={DEFAULT_HELP_MODE}>
    <DepositFormApp
      config={config}
      {...rest}
      sections={sections}
      recordSerializer={recordSerializer}
      componentOverrides={componentOverrides}
      useWizardForm
    />
  </HelpModeProvider>,
  rootEl
);
