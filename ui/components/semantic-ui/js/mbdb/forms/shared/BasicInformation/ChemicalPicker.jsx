import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Button } from "mbdb-semantic-ui-react";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";
import { useVocabularyTitle } from "@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles";
import { useOwnErrorMessages } from "@js/mbdb/forms/building-blocks/errors";
import {
  chemicalLinks,
  describeChemical,
  molecularWeightText,
} from "./chemical";

// The PubChem-backed dropdown mode of BasicInformation. A typed query that
// matches nothing can be sent to the manual form through the last option;
// RemoteSelectField reports it as an addition (see MbdbVocabularyField), so
// the write here is the manual value's seed and the mode flips by itself.
export const ChemicalPicker = ({ fieldPath }) => {
  const { values, setFieldValue } = useFormikContext();
  const value = getIn(values, fieldPath);
  const title = useVocabularyTitle("chemicals", value?.id);
  const objectMessages = useOwnErrorMessages(fieldPath);

  // The small grey meta line under the control once a term is picked.
  // Rendered only from data already at hand (the cached title, the id, and
  // any facts the server enriched into the stored value on save): the { id }
  // reference the UI writes carries no formula or molecular weight itself.
  const metaParts = [
    title,
    value?.chemical_formula,
    molecularWeightText(value?.molecular_weight),
    value?.id,
  ].filter(Boolean);

  return (
    <>
      <MbdbVocabularyField
        fieldPath={fieldPath}
        vocabularyName="chemicals"
        describe={describeChemical}
        allowAdditions
        additionLabel="Enter manually: "
        onAddition={(text) => setFieldValue(fieldPath, { title: { en: text } })}
      />
      {objectMessages.map((message) => (
        <div key={message} className="ui red text">
          {message}
        </div>
      ))}
      {value?.id && metaParts.length > 0 && (
        <div className="ui small grey text">{metaParts.join(" · ")}</div>
      )}
      {value?.id &&
        chemicalLinks({ id: value.id, title: title ?? value.title }).map(
          ({ label, href }) => (
            <Button
              key={href}
              basic
              size="mini"
              as="a"
              href={href}
              target="_blank"
              rel="noreferrer"
              type="button"
            >
              {label}
            </Button>
          )
        )}
    </>
  );
};

ChemicalPicker.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
