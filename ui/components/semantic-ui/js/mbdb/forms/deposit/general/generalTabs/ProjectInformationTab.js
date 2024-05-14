import RecordInformation from "../projectInformation/RecordInformation";
import Depositors from "../projectInformation/depositors/Depositors";
import ArrayField from "../../buildingBlocks/ArrayField";
import { VocabularySelectField } from "@js/oarepo_vocabularies";
import { FieldLabel } from "react-invenio-forms";
import AssociatedPublication from "../projectInformation/associatedPublication/AssociatedPublication";

function ProjectInformationTab( { name } ) {

  return (
    <>
        <div className="mb-3">
            <RecordInformation name={`${name}.record_information`} />
        </div>
        <div className="mb-3">
            <AssociatedPublication name={name} />
        </div>
        <div className="mb-3">
            <Depositors name={`${name}.depositors`} />
        </div>
        <div>
            <ArrayField
                name={name}
                label='Funding reference'
                fieldName='funding_reference'
                tooltip='List of information about the grants that supported generation of the raw data annotated by this record. Note that this information is based on OpenAire Projects'
                renderChild={({ arrayName, index }) => (
                    <VocabularySelectField
                        search={(options) => options}
                        type="grants/authoritative"
                        label={
                            <FieldLabel
                                htmlFor={`${arrayName}.${index}`}
                                icon=""
                            />
                        }
                        fieldPath={`${arrayName}.${index}`}
                        placeholder={`funding reference ${index + 1}`}
                    />
                )}
            />
        </div>
    </>
  );
}

export default ProjectInformationTab;