import React from "react";
import OrcidInput from "./OrcidInput";

export default function OrcidForm({ handleSubmit, orcid, error }) {

    return (
      <>
        <div className="mb-2">
          <h3 className="font-JostSemiBold mr-2">
            Use ORCID
            <img
              src="/static/images/orcid-logo.png"
              alt="orcid logo"
              className="w-6 h-auto my-auto inline-block ml-1 mr-2 -mt-1"
            />
            to prefill your information
          </h3>
        </div>
        <div className="mb-4">
          <div className="mb-2">
            <OrcidInput length={16} orcid={orcid} onComplete={handleSubmit} />
          </div>
          <div className="text-accent font-JostSemiBold my-2">
            {error}
          </div>
        </div>
      </>
    );
}