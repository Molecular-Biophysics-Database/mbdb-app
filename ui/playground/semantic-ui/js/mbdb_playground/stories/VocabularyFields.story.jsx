import React from "react";

import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";
import { OrganismField } from "@js/mbdb/forms/shared/VocabularyFields/OrganismField";
import { entityPath, entityValues, entityErrors } from "../fixtures";

// The dropdowns talk to the live /api/vocabularies API: the organisms,
// body-fluids and chemicals vocabularies must be loaded. Type "bacillus"
// into the empty organism and check the rank next to each option. The
// prefilled scenarios show the title fetched for a stored id.

const ORGANISM = entityPath("source_organism");
const FLUID = entityPath("fluid");

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
      // seed the entity type: a pick writes into entities_of_interest[0],
      // so the entity must start with its type or the write would build one
      // without it
      initialValues: entityValues("Polymer"),
      render: OrganismEmpty,
    },
    {
      name: "Organism, filled",
      // stored as just { id }; the title must appear — the organisms
      // vocabulary must be loaded so the title fetch finds taxid:12374
      initialValues: entityValues("Polymer", {
        source_organism: { id: "taxid:12374" },
      }),
      render: OrganismFilled,
    },
    {
      name: "Body fluid, filled",
      // bf:2 = Serum; the body-fluids vocabulary must be loaded
      initialValues: entityValues(
        "Complex substance of biological origin",
        { fluid: { id: "bf:2" } },
        { derived_from: "Body fluid" }
      ),
      render: BodyFluidFilled,
    },
    {
      name: "With errors",
      // seeded like "Organism, empty": a pick must not build a type-less
      // entity
      initialValues: entityValues("Polymer"),
      initialErrors: entityErrors(
        "source_organism",
        "Missing data for required field."
      ),
      render: OrganismEmpty,
    },
  ],
};

export default story;
