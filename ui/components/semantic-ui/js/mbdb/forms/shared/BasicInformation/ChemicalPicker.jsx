import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { ExternalLink } from "@js/mbdb/forms/building-blocks/ExternalLink";
import { MbdbVocabularyField } from "@js/mbdb/forms/shared/VocabularyFields/MbdbVocabularyField";
import { useVocabularyItem } from "@js/mbdb/forms/shared/VocabularyFields/vocabularyTitles";
import { useModelFieldData } from "@js/mbdb/forms/building-blocks/fieldData";
import {
  MANUAL_CHEMICALS_ENABLED,
  chemicalLinks,
  describeChemical,
} from "./chemical";

// The "check your chemistry" links, rendered in the label slot.
const ChemicalLinks = ({ value, item }) =>
  chemicalLinks({
    id: value?.id,
    title: item.title ?? value?.title,
  }).map(({ label, href }) => (
    <ExternalLink key={href} href={href}>
      {label}
    </ExternalLink>
  ));

ChemicalLinks.propTypes = {
  value: PropTypes.object,
  item: PropTypes.shape({
    title: PropTypes.string,
    customFields: PropTypes.object,
  }),
};

// The PubChem-backed dropdown mode of BasicInformation. Only the dropdown
// carries the object-level error (MbdbVocabularyField already shows it, so
// there is no second error block here). "Enter manually" is hidden while
// the server drops manual chemicals (chemical.js).
export const ChemicalPicker = ({ fieldPath }) => {
  const { values, setFieldValue } = useFormikContext();
  const value = getIn(values, fieldPath);
  // Whole-item cache: the title AND the custom_fields of the picked term —
  // remembered on the pick itself, otherwise fetched once per id.
  const item = useVocabularyItem("chemicals", value?.id);
  const data = useModelFieldData(fieldPath, {});

  // The small grey meta line under the control once a term is picked: the
  // facts and the id, no title (the dropdown shows that). The facts come
  // from the item cache — the { id } reference the UI writes carries none,
  // and drafts are not enriched on load.
  const meta = [
    describeChemical({ custom_fields: item.customFields }),
    value?.id,
  ]
    .filter(Boolean)
    .join(" · ");

  return (
    <>
      <MbdbVocabularyField
        fieldPath={fieldPath}
        vocabularyName="chemicals"
        describe={describeChemical}
        label={
          <>
            {data.label}{" "}
            {value?.id && <ChemicalLinks value={value} item={item} />}
          </>
        }
        {...(MANUAL_CHEMICALS_ENABLED
          ? {
              // additionPosition reaches Semantic's Dropdown through
              // restProps/RIF uiProps: "Enter manually" stays the last
              // option instead of sitting above the PubChem results.
              allowAdditions: true,
              additionPosition: "bottom",
              additionLabel: "Enter manually: ",
              onAddition: (text) =>
                setFieldValue(fieldPath, { title: { en: text } }),
            }
          : {})}
      />
      {value?.id && meta && <div className="ui small grey text">{meta}</div>}
    </>
  );
};

ChemicalPicker.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
