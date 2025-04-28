import React from "react";

export default function OrcidInfo({ orcid, givenName, familyName, onRemove, setUseOrcid }) {
    return (
      <div className="flex">
        <img
          src="/static/images/orcid-logo.png"
          alt="orcid logo"
          className="w-6 h-auto mr-2"
        />
        <div className="font-JostMedium mr-2">
          {orcid} / {givenName} {familyName}
        </div>
        <button
          className="bg-dark text-primary rounded-normal px-1 hover:bg-dark/85 transition-all"
          onClick={() => {
            onRemove();
            setUseOrcid(true);
          }}
        >
          <img src="/static/images/delete.svg" alt="edit" className="w-4 h-auto" />
        </button>
      </div>
    );
}