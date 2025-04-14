import React from "react";
import OrcidInput from "./OrcidInput";

export default function OrcidForm({ handleSubmit, orcid, error, setUseOrcid, onRemove}) {

    return (
      <>
        <div className="flex items-end mb-2">
          <h3 className="font-JostSemiBold mr-2">ORCID</h3>
          <img
            src="/static/images/orcid-logo.png"
            alt="orcid logo"
            className="w-7 h-auto"
          />
        </div>
        <div className="mb-2">
          <OrcidInput length={16} orcid={orcid} onComplete={handleSubmit} />
        </div>
        <div className="text-accent font-JostSemiBold my-2">
          {error}
        </div>
        <button
          className="underline font-JostSemiBold hover:text-black"
          onClick={() => {
            onRemove();
            setUseOrcid(false);
          }}
        >
          I don't have an ORCID
        </button>
      </>
    );
}