import React from "react";
import { FieldArray, getIn, useFormikContext } from "formik";
import { Button } from "semantic-ui-react";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";
import { v4 as uuidv4 } from "uuid";

function ArrayFieldCopyPaste({
  name,
  fieldName,
  label,
  renderChild,
  required,
  maxItems,
  tooltip,
  uuid,
  method,
}) {
  const { values } = useFormikContext();

  const handlePush = (push) => {
    const array = getIn(values, arrayName);
    const previousArray = array[array.length - 1];

    const updatedObject = () => {
      if (method === "mst") {
        return {
          ...(({ position, ...rest }) => rest)(previousArray),
          id: uuidv4(),
          sample: {
            ...previousArray.sample,
            ligands: (previousArray.sample.ligands || []).map(
              ({ concentration, ...ligandRest }) => ligandRest
            ),
            targets: (previousArray.sample.targets || []).map(
              ({ concentration, ...targetRest }) => targetRest
            ),
          },
        };
      } else if (method === "bli") {
        const sample = previousArray?.sample;
        return {
          ...(({ measurement_protocol_step, ...rest }) => rest)(previousArray),
          id: uuidv4(),
          sample: sample
            ? {
                ...(({ well_position, chemical_environment, ...rest }) => rest)(
                  sample
                ),
                analytes: (sample.analytes || []).map(
                  ({ concentration, ...analyteRest }) => analyteRest
                ),
              }
            : {},
        };
      } else if (method === "spr") {
        const samples = previousArray?.samples;
        return {
          ...previousArray,
          id: uuidv4(),
          samples:
            samples && samples.length > 0
              ? [
                  {
                    ...(() => {
                      const {
                        measurement_step,
                        chemical_environment,
                        ...rest
                      } = samples[0];
                      return rest;
                    })(),
                    analytes: (samples[0].analytes || []).map(
                      ({ concentration, ...analyteRest }) => analyteRest
                    ),
                  },
                ]
              : [],
        };
      } else if (method === "file") {
        const metadata = previousArray?.metadata;
        return {
          id: uuidv4(),
          metadata: { ...metadata },
        };
      }
    };

    const newItem =
      array && array.length > 0
        ? updatedObject()
        : uuid
        ? { id: uuidv4() }
        : undefined;

    push(newItem);
  };

  const arrayName =
    fieldName !== undefined ? `${name}.${fieldName}` : `${name}`;
  const value = getIn(values, arrayName);

  return (
    <div>
      <FieldArray
        name={arrayName}
        render={({ push, remove }) => (
          <>
            {value &&
              value.map((item, index) => (
                <div key={index} className="flex mt-3">
                  <div className="mr-3">
                    {renderChild({ arrayName, name, index, item })}
                  </div>
                  {(!required || index > 0) && (
                    <Button
                      style={{ backgroundColor: "#023850", color: "white" }}
                      onClick={() => remove(index)}
                    >
                      <img
                        src="/static/images/delete.svg"
                        alt="Delete"
                        className="w-4 h-auto"
                      />
                    </Button>
                  )}
                </div>
              ))}
            {(!maxItems || !value || value.length < maxItems) &&
              (tooltip ? (
                <div className="mt-3">
                  <Tooltip
                    title={
                      <Typography style={{ color: "white", fontSize: 13 }}>
                        {tooltip}
                      </Typography>
                    }
                    arrow
                  >
                    <Button
                      style={{ backgroundColor: "#023850", color: "white" }}
                      onClick={() => handlePush(push)}
                    >
                      + {`${label}`}
                    </Button>
                  </Tooltip>
                </div>
              ) : (
                <div className="mt-3">
                  <Button
                    style={{ backgroundColor: "#023850", color: "white" }}
                    onClick={() => handlePush(push)}
                  >
                    + {`${label}`}
                  </Button>
                </div>
              ))}
          </>
        )}
      />
    </div>
  );
}

export default ArrayFieldCopyPaste;
