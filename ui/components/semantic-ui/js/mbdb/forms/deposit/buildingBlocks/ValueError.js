import React from "react";
import CustomField from "./CustomField";
import FormWrapper from "./FormWrapper";
import RelativeErrors from "./RelativeErrors";

function ValueError({ colorSchema, name }) {
  return (
    <>
      <div className="flex">
        <FormWrapper
          headline="Value error"
          tooltip="The expected error of the result in terms of a 95 % confidence interval"
          colorSchema={colorSchema}
        >
          <div className="flex">
            <div className="mr-3">
              <CustomField
                name={name}
                fieldName="lower"
                type="number"
                label="Lower"
                tooltip="The lower error, i.e. the number that should be subtracted from the value to get the lower bound of the 95 % confidence interval. The same unit as the value being described is assumed. If relative errors are provided, please provide them in fractional form (e.g.  0.01 for 1 %)"
                width="w-[8rem]"
              />
            </div>
            <div className="mr-3">
              <CustomField
                name={name}
                fieldName="upper"
                type="number"
                label="Upper"
                tooltip="The upper error, i.e. the number that should be added to the value to get the upper bound of the 95 % confidence interval. The same unit as the value being described is assumed. If relative errors are provided, please provide them in fractional form (e.g.  0.01 for 1 %)"
                width="w-[8rem]"
              />
            </div>
            <RelativeErrors name={name} />
          </div>
        </FormWrapper>
      </div>
    </>
  );
}

export default ValueError;
