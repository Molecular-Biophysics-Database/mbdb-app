import React from "react";
import FormWrapper from "../buildingBlocks/FormWrapper";
import OptionField from "../buildingBlocks/OptionField";
import Article from "./Article";
import Book from "./Book";
import Thesis from "./Thesis";
import { getIn, useFormikContext } from "formik";
import ArrayField from "../buildingBlocks/ArrayField";

function AssociatedPublication( { name } ) {
    
    const { values } = useFormikContext()

    const associatedPublicationOptions = [
        { value: 'Article', label: 'Article' },
        { value: 'Book', label: 'Book' },
        { value: 'Thesis', label: 'Thesis' },
    ];

  return (
    <>
        <div>
            <ArrayField
                name={name}
                label="Associated publication"
                initialValue={{ type: 'Article'}}
                maxItems={1}
                tooltip='If the data in this record is described in published literature (article, journal, thesis), information about the literature can be specified here'
                renderChild={({ arrayName, index }) => {
                    const actualValue = getIn(values, `${arrayName}.${index}`)
                    if (!actualValue) {return null}        
                    return(
                    <FormWrapper
                        headline='Associated publication'
                        tooltipHeader='If the data in this record is described in published literature (article, journal, thesis), information about the literature can be specified here'
                    >
                        <div className="flex">
                            <div className="mr-3">
                                <OptionField
                                    name={`${arrayName}.${index}`}
                                    options={associatedPublicationOptions}
                                    label='type'
                                    fieldName='type'
                                    width='w-full'
                                    tooltip='The type of the publication'
                                />
                            </div>
                            <div>
                                {actualValue.type === 'Article' && (
                                    <Article
                                        name={`${arrayName}.${index}`}
                                    />
                                )}
                                {actualValue.type === 'Book' && (
                                    <Book
                                        name={`${arrayName}.${index}`}
                                    />
                                )}
                                {actualValue.type === 'Thesis' && (
                                    <Thesis
                                        name={`${arrayName}.${index}`}
                                    />
                                )}
                            </div>
                        </div>
                    </FormWrapper>
                )}}
            />
        </div>
    </>
  );
}

export default AssociatedPublication;