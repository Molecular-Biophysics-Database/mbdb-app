import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";

// The names of one or more internal relations, looked up by id in the form: a
// saved reference may hold only its id, and a renamed target shows its new name.
export const ReferenceNames = ({ value, targetPath }) => {
  const { values } = useFormikContext();
  const targets = getIn(values, targetPath) ?? [];
  const names = [value]
    .flat()
    .filter(Boolean)
    .map(
      (ref) =>
        targets.find((item) => item?.id === ref.id)?.name ?? ref.name ?? ref.id
    );
  return <span>{[...new Set(names)].join(", ")}</span>;
};

ReferenceNames.propTypes = {
  value: PropTypes.oneOfType([PropTypes.object, PropTypes.array]),
  targetPath: PropTypes.string.isRequired,
};
