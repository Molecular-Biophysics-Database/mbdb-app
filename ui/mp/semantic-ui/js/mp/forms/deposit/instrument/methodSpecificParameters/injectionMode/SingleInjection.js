import React from "react";
import Volume from "../../../sharedComponents/Volume";

export default function SingleInjection({ name }) {
  return (
    <>
      <Volume name={`${name}.volume`} />
    </>
  );
}
