import React from "react";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function FormWrapper({ headline, children, colorSchema, tooltip, required, name }) {
  return (
    <>
      <div
        name={name}
        className={`${
          colorSchema === "light" ? "bg-primary" : "bg-white"
        } p-3 rounded-lg text-dark font-JostMedium`}
      >
        {headline && (
          <div className="flex">
            <div className="font-JostSemiBold text-lg mb-2">{headline}</div>
            {required && (
              <div className="text-accent ml-1">
                <Tooltip
                  title={
                    <Typography style={{ color: "white", fontSize: 13 }}>
                      This field is required and cannot be left blank or unset
                    </Typography>
                  }
                  arrow
                >
                  <span>*</span>
                </Tooltip>
              </div>
            )}
            {tooltip && (
              <div className="ml-1 -mt-1">
                <Tooltip
                  title={
                    <Typography style={{ color: "white", fontSize: 13 }}>
                      {tooltip}
                    </Typography>
                  }
                  arrow
                >
                  <span>?</span>
                </Tooltip>
              </div>
            )}
          </div>
        )}
        {children}
      </div>
    </>
  );
}

export default FormWrapper;
