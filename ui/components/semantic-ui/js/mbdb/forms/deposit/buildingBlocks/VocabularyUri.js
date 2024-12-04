import React from "react";
import { Icon, Label } from "semantic-ui-react";


export const VocabularyUri = (relatedURI) => {
  return (
    relatedURI &&
    Object.entries(relatedURI).map(([name, value]) => {
      return (
        <Label key={name} basic size="mini">
          <a
            onClick={(e) => e.stopPropagation()}
            href={value}
            target="_blank"
            rel="noopener noreferrer"
          >
            <Icon name="external alternate" />
            {name}
          </a>
        </Label>
      );
    })
  );
};