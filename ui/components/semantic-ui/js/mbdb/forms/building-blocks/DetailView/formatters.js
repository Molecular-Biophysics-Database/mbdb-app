/* The external-references list is positional and never reorders, so the index
   is a legitimate key (carries meaning, not identity). See collect.js/Rows.jsx. */
/* eslint-disable react/no-array-index-key */
import React, { useState } from "react";
import PropTypes from "prop-types";
import { Label } from "mbdb-semantic-ui-react";
import { ExternalLink } from "@js/mbdb/forms/building-blocks/ExternalLink";
import { isEmptyValue } from "@js/mbdb/forms/building-blocks/errors";
// The shared helpers below are pure and reach this folder anyway through
// values.js (the vocabulary-title cache); they keep the details and the edit
// blocks formatting a value the same way.
import { useVocabularyItem } from "@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles";
import {
  describeChemical,
  isManualChemical,
} from "@js/mbdb/forms/shared/BasicInformation/chemical";
import { parseRef, refUrl } from "@js/mbdb/forms/shared/ExternalDatabases/refs";
import { mapUrl } from "@js/mbdb/forms/shared/Location/mapUrl";

// Path-suffix formatters for DetailView. The key is matched against the leaf
// name of a field path; add one only when the generic output is poor
// (design/building-blocks/DetailView.md §3). Everything not listed here —
// {value, unit} objects, {id} vocabularies, locations, booleans, arrays — is
// handled generically by DetailView.

const WRAP = 60;

// Monospace, first 60 characters, plus the residue count. [Show all] expands
// to the full sequence wrapped at 60 characters (design §3).
const SequenceValue = ({ value }) => {
  const [all, setAll] = useState(false);
  const shown = all
    ? value.match(new RegExp(`.{1,${WRAP}}`, "g"))?.join("\n") ?? value
    : value.slice(0, WRAP);
  return (
    <span className="mbdb-sequence">
      <code className={all ? "mbdb-pre-line" : undefined}>{shown}</code>{" "}
      {`(${value.length} residues)`}{" "}
      {value.length > WRAP && (
        <button
          type="button"
          className="mbdb-link"
          onClick={() => setAll((prev) => !prev)}
        >
          {all ? "[Show less]" : "[Show all]"}
        </button>
      )}
    </span>
  );
};

SequenceValue.propTypes = {
  value: PropTypes.string.isRequired,
};

// A chemical's basic information: the title, then its facts — formula,
// molecular weight, the InChIKey id — in grey. The facts come from the
// vocabulary item cache (the stored reference is `{ id }`) or from the
// record's own keys when it carries them; a manual chemical (no id) shows its
// typed title and the grey hint (design §3). Without this the details show
// only the id or the title, hiding the formula and the molecular weight.
const ChemicalValue = ({ value }) => {
  const { title, customFields } = useVocabularyItem("chemicals", value?.id);
  const facts = [
    describeChemical({
      custom_fields: {
        chemical_formula:
          value?.chemical_formula ?? customFields?.chemical_formula,
        molecular_weight:
          value?.molecular_weight ?? customFields?.molecular_weight,
      },
    }),
    value?.id,
  ].filter((part) => !isEmptyValue(part));
  const shownTitle = title ?? value?.title?.en ?? value?.title;
  return (
    <>
      {!isEmptyValue(shownTitle) && <span>{shownTitle} </span>}
      {facts.length > 0 && (
        <span className="mbdb-muted-text">{facts.join(" · ")}</span>
      )}
      {isManualChemical(value) && (
        <Label basic size="mini" content="Manual entry" />
      )}
    </>
  );
};

ChemicalValue.propTypes = { value: PropTypes.object.isRequired };

// External references stored as "prefix:id": a known prefix becomes a plain
// link with the external icon, an unknown one stays plain text; links are
// separated by spaces (design §2b rule 7: links, not buttons joined with ", ").
const ExternalDatabasesValue = ({ value }) => (
  <>
    {value.map((ref, i) => {
      const url = refUrl(parseRef(ref));
      return (
        <React.Fragment key={`${ref}-${i}`}>
          {i > 0 ? " " : ""}
          {url ? (
            <ExternalLink plain href={url}>
              {ref}
            </ExternalLink>
          ) : (
            ref
          )}
        </React.Fragment>
      );
    })}
  </>
);

ExternalDatabasesValue.propTypes = { value: PropTypes.array.isRequired };

// Coordinates as one line, plus the map link when both numbers are present
// (design §3): `49.1951, 16.6068, 237 m [Show on map ↗]`.
const LocationValue = ({ value }) => {
  const parts = [
    value?.latitude,
    value?.longitude,
    typeof value?.altitude === "number" ? `${value.altitude} m` : undefined,
  ].filter((part) => part !== undefined && part !== null);
  const hasPair =
    typeof value?.latitude === "number" && typeof value?.longitude === "number";
  return (
    <>
      {parts.join(", ")}
      {hasPair && (
        <>
          {" "}
          <ExternalLink href={mapUrl(value.latitude, value.longitude)}>
            Show on map ↗
          </ExternalLink>
        </>
      )}
    </>
  );
};

LocationValue.propTypes = { value: PropTypes.object.isRequired };

// Each entry is a formatter component: (value) => JSX.
export const formatters = {
  sequence: (value) => <SequenceValue value={value} />,
  external_databases: (value) => <ExternalDatabasesValue value={value} />,
  location: (value) => <LocationValue value={value} />,
  basic_information: (value) => <ChemicalValue value={value} />,
};
