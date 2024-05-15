import FormWrapper from '../buildingBlocks/FormWrapper';
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";

function Instrument( {name} ) {

  return (
    <>
        <FormWrapper headline='Instrument' tooltip='Information about the instrument being used to collect (measure) the raw data annotated by this record'>
            <div className='flex'>
                <div>
                    <VocabularySelectField
                        search={(options) => options}
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