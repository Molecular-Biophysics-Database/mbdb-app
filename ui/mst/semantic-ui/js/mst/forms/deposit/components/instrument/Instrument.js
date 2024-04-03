import React from 'react';
import FormWrapper from '../buildingBlocks/FormWrapper';
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";

function Instrument( {name} ) {

  return (
    <>
        <FormWrapper headline='Instrument' tooltipHeader='Information about the instrument being used to collect (measure) the raw data annotated by this record'>
            <div className='flex'>
                <div>
                    <VocabularySelectField
                        type="instruments"
                        label={
                          <FieldLabel
                            htmlFor={name}
                            icon=""
                          />
                        }
                        fieldPath={name}
                        placeholder="Instrument"
                        clearable
                    />
                </div>
            </div>
        </FormWrapper>
    </>
  );
}

export default Instrument;