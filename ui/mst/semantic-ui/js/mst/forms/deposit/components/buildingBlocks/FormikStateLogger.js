import React from "react";
import { useFormikContext } from "formik";
import PropTypes from "prop-types";

// component to visualize formik state on screen during development
export const FormikStateLogger = ({ render = true }) => {
  const state = useFormikContext();
  if (process.env.NODE_ENV !== "development") {
    return;
  }

  if (render) {
    return (
        <pre>{JSON.stringify(state.values, null, 2)}</pre>
    );
  }

  console.debug("[form state]: ", state, "\n[form values]:", state.values);
  return <></>;
};

FormikStateLogger.propTypes = {
  render: PropTypes.bool,
};

export default FormikStateLogger;