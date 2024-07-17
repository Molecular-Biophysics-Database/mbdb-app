import React from "react";
import Volume from "../../../sharedComponents/Volume";

function SingleInjection( { name } ) {

  return (
    <>
      <Volume name={`${name}.volume`}/>
    </>
  );
}

export default SingleInjection;