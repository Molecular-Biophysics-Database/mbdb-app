import React from "react";

import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";
import { OrganismField } from "@js/mbdb/forms/shared/VocabularyFields/OrganismField";

// The dropdowns talk to the live /api/vocabularies API (P1–P3): type
// "bacillus" into the empty organism and check the rank next to each
// option. The prefilled scenarios show the title fetched for a stored id.

const BASE = "metadata.general_parameters.entities_of_interest.0";

const ORGANISM = `${BASE}.source_organism`;
const FLUID = `${BASE}.fluid`;

const OrganismEmpty = () => <OrganismField fieldPath={ORGANISM} />;

const OrganismFilled = () => <OrganismField fieldPath={ORGANISM} />;

const BodyFluidFilled = () => (
  <MbdbVocabularyField fieldPath={FLUID} vocabularyName="body-fluids" />
);

const story = {
  title: "VocabularyFields",
  scenarios: [
    {
      name: "Organism, empty",
      initialValues: {},
      render: OrganismEmpty,
    },
    {
      name: "Organism, filled",
      // stored as just { id }; the title must appear (P4 title fetch)
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ source_organism: { id: "taxid:12374" } }],
          },
        },
      },
      render: OrganismFilled,
    },
    {
      name: "Body fluid, filled",
      // bf:2 = Serum
      initialValues: {
        metadata: {
          general_parameters: {
            entities_of_interest: [{ fluid: { id: "bf:2" } }],
          },
        },
      },
      render: BodyFluidFilled,
    },
    {
      name: "With errors",
      initialValues: {},
      initialErrors: {
        metadata: {
          general_parameters: {
            entities_of_interest: [
              { source_organism: "Missing data for required field." },
            ],
          },
        },
      },
      render: OrganismEmpty,
    },
  ],
};

export default story;
