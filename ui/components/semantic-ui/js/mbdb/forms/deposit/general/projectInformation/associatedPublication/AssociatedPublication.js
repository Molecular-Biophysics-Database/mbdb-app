import React from "react";
import FormWrapper from "../../../buildingBlocks/FormWrapper";
import Article from "./Article";
import Book from "./Book";
import Thesis from "./Thesis";
import { getIn, useFormikContext } from "formik";
import OptionalField from "../../../buildingBlocks/OptionalField";
import DynamicOptionField from "../../../buildingBlocks/DynamicOptionField";

function AssociatedPublication({ name }) {
  const { values } = useFormikContext();

  const associatedPublicationOptions = [
    { value: "Article", label: "Article" },
    { value: "Book", label: "Book" },
    { value: "Thesis", label: "Thesis" },
  ];

  return (
    <>
      <div>
        <OptionalField
          name={name}
          label="Associated publication"
          fieldName="associated_publication"
          initialValue={{ type: "Article" }}
          tooltip="If the data in this record is described in published literature (article, journal, thesis), information about the literature can be specified here"
          renderChild={({ optionalFieldName }) => {
            const actualValue = getIn(values, optionalFieldName);
            if (!actualValue) {
              return null;
            }
            return (
              <FormWrapper
                headline="Associated publication"
                tooltip="If the data in this record is described in published literature (article, journal, thesis), information about the literature can be specified here"
              >
                <div className="flex">
                  <div className="mr-3">
                    <DynamicOptionField
                      name={optionalFieldName}
                      options={associatedPublicationOptions}
                      label="type"
                      required
                      fieldName="type"
                      width="w-full"
                      tooltip="The type of the publication"
                    />
                  </div>
                  <div>
                    {actualValue.type === "Article" && (
                      <Article name={optionalFieldName} />
                    )}
                    {actualValue.type === "Book" && (
                      <Book name={optionalFieldName} />
                    )}
                    {actualValue.type === "Thesis" && (
                      <Thesis name={optionalFieldName} />
                    )}
                  </div>
                </div>
              </FormWrapper>
            );
          }}
        />
      </div>
    </>
  );
}

export default AssociatedPublication;
