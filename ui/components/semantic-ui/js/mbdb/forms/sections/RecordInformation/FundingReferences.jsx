import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { ModalArrayField } from "@js/mbdb/forms/building-blocks/ModalArrayField";
import { VocabularyValue } from "@js/mbdb/forms/building-blocks/DetailView/values";
import { TextField } from "@js/mbdb/forms/building-blocks/TextField";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";
import {
  describeAffiliation,
  describeAward,
} from "@js/mbdb/forms/shared/VocabularyFields/describers";
import {
  itemLabel,
  rememberTitle,
} from "@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles";
import { FUNDING_REFERENCES_PATH } from "./path";

// The group spec of one funding reference, read by the details view (guide
// §8). Funder and award are vocabulary references, so they declare their
// vocabularies; the details show an award through its `award` formatter, so
// a custom award (no id) shows its number and title too.
export const FUNDING_REFERENCE_GROUPS = [
  {
    title: "Funding reference",
    fields: [
      { field: "funder", vocabulary: "funders" },
      { field: "award", vocabulary: "awards" },
    ],
  },
];

// The registries also match on what the option text does not show (a grant
// number, "GAČR"), so the dropdown must not filter their results by its text.
const keepAllOptions = (options) => options;

// A custom award: the RDM award relation takes either an `id` from the
// awards vocabulary or, without one, its own `number` and `title`.
const isCustomAward = (award) =>
  !!award && !award.id && (award.number !== undefined || award.title !== undefined);

// The award of one funding reference. An award is picked from the live
// OpenAIRE search (its number and title cannot be edited) and created in the
// vocabulary on save. One that is not there is added from the picker ("Add new award:"),
// which stores the typed text as its number; the number and title are then
// edited here, and "Pick from the list instead" goes back to the picker.
const AwardField = ({ fieldPath, onPicked }) => {
  const { values, setFieldValue } = useFormikContext();
  const award = getIn(values, fieldPath);

  if (isCustomAward(award)) {
    return (
      <>
        <TextField
          fieldPath={`${fieldPath}.number`}
          label="Award number"
          help="The number of the grant, as assigned by the funder"
          required
        />
        <TextField
          fieldPath={`${fieldPath}.title.en`}
          label="Award title"
          help="The title of the funded project"
        />
        <button
          type="button"
          className="mbdb-link"
          onClick={() => unsetFieldValue(values, setFieldValue, fieldPath)}
        >
          Pick the award from the list instead
        </button>
      </>
    );
  }

  return (
    <MbdbVocabularyField
      fieldPath={fieldPath}
      vocabularyName="awards"
      suggestionAPIUrl="/api/openaire/awards"
      searchQueryParamName="q"
      search={keepAllOptions}
      describe={describeAward}
      onPicked={onPicked}
      allowAdditions
      additionPosition="bottom"
      additionLabel="Add new award: "
      onAddition={(text) => setFieldValue(fieldPath, { number: text })}
    />
  );
};

AwardField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  onPicked: PropTypes.func,
};

// The form of one funding reference. Funders are searched in ROR (the proxy
// returns any organization); picking an award also sets its funder.
const FundingReferenceForm = ({ itemPath }) => {
  const { setFieldValue } = useFormikContext();
  // Remounts the funder picker when the award sets its value: the dropdown
  // reads its initial option only on mount.
  const [funderKey, setFunderKey] = React.useState(0);

  const onAwardPicked = ({ funder }) => {
    if (!funder?.id) return;
    rememberTitle("funders", funder.id, funder.name);
    setFieldValue(`${itemPath}.funder`, { id: funder.id });
    setFunderKey((key) => key + 1);
  };

  return (
    <>
      <MbdbVocabularyField
        key={funderKey}
        fieldPath={`${itemPath}.funder`}
        vocabularyName="funders"
        suggestionAPIUrl="/api/ror/affiliations"
        searchQueryParamName="q"
        search={keepAllOptions}
        describe={describeAffiliation}
      />
      <AwardField fieldPath={`${itemPath}.award`} onPicked={onAwardPicked} />
    </>
  );
};

FundingReferenceForm.propTypes = {
  itemPath: PropTypes.string.isRequired,
};

// The funding references: one row per grant in a summary table, each edited
// in a modal with the Funder picker and the award (picked, or added as a
// custom one). Label and help come from the model.
export const FundingReferences = () => (
  <ModalArrayField
    fieldPath={FUNDING_REFERENCES_PATH}
    itemLabel={() => "Funding reference"}
    newItemOptions={[{ label: "funding reference", value: {} }]}
    columns={[
      {
        label: "Funder",
        value: (v) =>
          v?.funder?.id ? (
            <VocabularyValue vocabulary="funders" value={v.funder} />
          ) : (
            ""
          ),
      },
      {
        label: "Award",
        value: (v) => {
          if (v?.award?.id)
            return <VocabularyValue vocabulary="awards" value={v.award} />;
          return isCustomAward(v?.award) ? itemLabel("awards", v.award) ?? "" : "";
        },
      },
    ]}
    detailGroups={FUNDING_REFERENCE_GROUPS}
    renderForm={(itemPath) => <FundingReferenceForm itemPath={itemPath} />}
  />
);
