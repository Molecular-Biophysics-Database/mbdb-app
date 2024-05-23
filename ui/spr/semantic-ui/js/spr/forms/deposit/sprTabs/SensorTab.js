import React from "react";
import Sensor from "../sensor/Sensor";

function SensorTab( { name } ) {

    return (
      <>
        <Sensor name={`${name}.sensor`}/>
      </>
    );
  }
  
  export default SensorTab;