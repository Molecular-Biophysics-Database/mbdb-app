import React from "react";
import Tooltip from "@material-ui/core/Tooltip";
import { Typography } from "@material-ui/core";

function FormWrapper({ headline, children, colorSchema, tooltip }) {
  return (
    <>
      <div
        className={`${
          colorSchema === "light" ? "bg-primary" : "bg-white"
        } p-3 rounded-lg text-dark`}
      >
        {headline && (
          <div className="flex">
            <div className="font-JostMedium text-18px mb-2">{headline}</div>
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
