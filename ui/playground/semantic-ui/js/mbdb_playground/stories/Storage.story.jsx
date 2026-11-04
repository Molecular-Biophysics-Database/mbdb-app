import React from "react";
import { Storage } from "@js/mbdb/forms/shared/Storage";
import { entityErrors, entityPath, entityValues } from "../fixtures";

const PATH = entityPath("storage");

const Fields = () => <Storage fieldPath={PATH} />;

const story = {
  title: "Storage",
  scenarios: [
    {
      name: "Empty",
      initialValues: entityValues("Complex substance of industrial origin"),
      render: Fields,
    },
    {
      name: "Filled",
      // constructed (the sample records have no storage)
      initialValues: entityValues("Complex substance of industrial origin", {
        storage: {
          temperature: { value: -80, unit: "°C" },
          duration: { value: 3, unit: "months" },
          storage_preparation: [
            {
              name: "Flash freezing",
              description: "Aliquots frozen in liquid nitrogen",
            },
          ],
        },
      }),
      render: Fields,
    },
    {
      name: "With errors",
      initialValues: entityValues("Complex substance of industrial origin", {
        storage: { duration: { value: 3, unit: "months" } },
      }),
      initialErrors: entityErrors(
        "storage.temperature",
        "Missing data for required field."
      ),
      render: Fields,
    },
  ],
};

export default story;
