import React from "react";
import { Icon, Label } from "semantic-ui-react";

// As oarepo's labels and icons, which cover only oarepo's own request types
export const PublishApprovedLabel = () => (
  <Label horizontal className="primary theme-secondary" size="small">
    Publish
  </Label>
);

export const PublishApprovedIcon = () => (
  <Icon name="cloud upload" className="neutral" />
);
