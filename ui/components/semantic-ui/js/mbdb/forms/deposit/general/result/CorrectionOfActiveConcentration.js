import React from "react";
import ValueUnit from "../../buildingBlocks/ValueUnit";
import ValueError from "../../buildingBlocks/ValueError";
import OptionalField from "../../buildingBlocks/OptionalField";
import CreateUuid from "../../buildingBlocks/CreateUuid";

function CorrectionOfActiveConcentration({ name }) {
  CreateUuid(name);

  const unitOptions = [{ value: "unitless", label: "unitless" }];

  return (
    <>
      <div className="flex mb-3">
        <div>
          <ValueUnit
            options={unitOptions}
            name={name}
            valueRequired
            unitRequired
            tooltipValue="The correction of the deviations between nominal and true active concentration of the entity"
            tooltipUnit="The correction of active concentration is unitless"
          />
        </div>
      </div>
      <div>
        <OptionalField
          name={name}
          label="Value error"
          fieldName="value_error"
          tooltip="The expected error of the result in terms of a 95 % confidence interval"
          renderChild={({ optionalFieldName }) => (
            <div>
              <ValueError name={optionalFieldName} colorSchema="light" />
            </div>
          )}
        />
      </div>
    </>
  );
}

export default CorrectionOfActiveConcentration;
