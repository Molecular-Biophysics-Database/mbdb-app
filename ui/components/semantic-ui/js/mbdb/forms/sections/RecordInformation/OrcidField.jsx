import React, { useState } from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Button } from "mbdb-semantic-ui-react";
import { FieldShell } from "@js/mbdb/forms/building-blocks/FieldShell";
import { OrcidInput } from "@js/mbdb/forms/building-blocks/OrcidInput";
import { useFieldBinding } from "@js/mbdb/forms/building-blocks/fieldData";
import { unsetFieldValue } from "@js/mbdb/forms/building-blocks/unset";

const ORCID_API = "https://pub.orcid.org/v3.0";
const ORCID_PREFIX = "orcid:";
const ORCID_LENGTH = 16;

// The stored ORCID of a person (its identifiers array holds at most one
// "orcid:…" string): its 16 digits as box values, or 16 empty boxes.
export const storedOrcidBoxes = (identifiers) => {
  const stored = Array.isArray(identifiers)
    ? identifiers.find(
        (id) => typeof id === "string" && id.startsWith(ORCID_PREFIX)
      )
    : undefined;
  const digits = stored
    ? stored.slice(ORCID_PREFIX.length).replace(/[^0-9]/g, "")
    : "";
  return Array.from(
    { length: ORCID_LENGTH },
    (_, index) => digits[index] ?? ""
  );
};

// The digits of the boxes as one string ("0000000218250097"), or "" when any
// box is empty.
export const orcidDigits = (boxes) =>
  boxes.every((digit) => digit !== "") ? boxes.join("") : "";

// The ORCID lookup of one person (depositor, principal contact, contributor):
// the digit boxes plus a Prefill button that fetches the public ORCID API and
// fills in the person's names and identifier — what mbdb-app-rdm-12's Contact
// did. The stored shape is unchanged (identifiers: ["orcid:0000-…"]), so the
// details views and old records keep working. A failed lookup keeps the
// digits (the message says what happened); Remove clears the prefill.
export const OrcidField = ({ fieldPath }) => {
  const identifiersPath = `${fieldPath}.identifiers`;
  const f = useFieldBinding(identifiersPath);
  const { values, setFieldValue } = useFormikContext();
  const [boxes, setBoxes] = useState(() =>
    storedOrcidBoxes(getIn(values, identifiersPath))
  );
  const [error, setError] = useState();
  const [isLoading, setIsLoading] = useState(false);

  const digits = orcidDigits(boxes);
  const prefillOrcid = digits
    ? `${digits.slice(0, 4)}-${digits.slice(4, 8)}-${digits.slice(
        8,
        12
      )}-${digits.slice(12, 16)}`
    : undefined;

  const prefill = async () => {
    setError("");
    setIsLoading(true);
    try {
      const response = await fetch(`${ORCID_API}/${prefillOrcid}`, {
        headers: { Accept: "application/json" },
      });
      if (!response.ok) {
        throw new Error(
          response.status === 404
            ? `No ORCID record for ${prefillOrcid}`
            : `ORCID API responded with ${response.status}`
        );
      }
      const data = await response.json();
      const givenName = data?.person?.name?.["given-names"]?.value;
      const familyName = data?.person?.name?.["family-name"]?.value;
      // only the names the API returns are written; the user's own stay
      if (givenName) setFieldValue(`${fieldPath}.given_name`, givenName);
      if (familyName) setFieldValue(`${fieldPath}.family_name`, familyName);
      setFieldValue(identifiersPath, [`${ORCID_PREFIX}${prefillOrcid}`]);
    } catch (e) {
      setError(e.message);
    } finally {
      setIsLoading(false);
    }
  };

  const remove = () => {
    setBoxes(Array.from({ length: ORCID_LENGTH }, () => ""));
    setError("");
    // The three prefill fields go together; a per-field unset would see a
    // stale snapshot each time and leave an empty {} behind (guide §7), so
    // the remaining person (its affiliations) is written back in one go —
    // or the whole person unset when nothing else is left.
    const person = { ...(getIn(values, fieldPath) ?? {}) };
    delete person.given_name;
    delete person.family_name;
    delete person.identifiers;
    if (Object.keys(person).length > 0) setFieldValue(fieldPath, person);
    else unsetFieldValue(values, setFieldValue, fieldPath);
  };

  return (
    <FieldShell
      label={f.label}
      help={f.help}
      required={f.required}
      hasError={f.hasError}
      messages={f.messages}
    >
      <div className="mbdb-orcid-prompt">
        Use ORCID
        <img
          src="/static/images/orcid-logo.png"
          alt="ORCID iD"
          className="mbdb-orcid-logo"
        />
        to prefill your information
      </div>
      <div className="mbdb-orcid-field">
        <OrcidInput value={boxes} onChange={setBoxes} />
        {prefillOrcid && (
          <Button
            type="button"
            basic
            size="small"
            loading={isLoading}
            disabled={isLoading}
            onClick={prefill}
          >
            Prefill from ORCID
          </Button>
        )}
        {orcidDigits(storedOrcidBoxes(getIn(values, identifiersPath))) !==
          "" && (
          <Button type="button" basic size="small" onClick={remove}>
            Remove
          </Button>
        )}
        {error && <div className="mbdb-error-text">{error}</div>}
      </div>
    </FieldShell>
  );
};

OrcidField.propTypes = {
  // the person OBJECT path (`${depositorsPath}.depositor` and the like)
  fieldPath: PropTypes.string.isRequired,
};
