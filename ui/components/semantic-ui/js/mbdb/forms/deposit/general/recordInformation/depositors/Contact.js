import React, { useState } from "react";
import ContactForm from "./ContactForm";
import { useFormikContext, getIn } from "formik";
import Spinner from "../../../buildingBlocks/Spinner";
import OrcidInfo from "./OrcidInfo";
import OrcidForm from "./OrcidForm";

function UseOrcidButton({ onClick }) {
  return (
    <button
      className="underline font-JostSemiBold hover:text-black mb-3"
      onClick={onClick}
    >
      I want to use ORCID
    </button>
  );
}

export default function Contact({ name }) {
  const { values, setFieldValue } = useFormikContext();

  const getField = (field) => getIn(values, `${name}.${field}`);

  const [givenName, setGivenName] = useState(getField("given_name") || "");
  const [familyName, setFamilyName] = useState(getField("family_name") || "");
  const [isUsingOrcid, setIsUsingOrcid] = useState(true);
  const [error, setError] = useState();
  const [isLoading, setIsLoading] = useState(false);

  const identifiers = getField("identifiers");

  const orcidNumbers = Array.isArray(identifiers)
  ? identifiers
    .filter((id) => typeof id === "string" && id.startsWith("orcid:"))
    .map((id) => id.replace("orcid:", ""))
  : [];

  const [orcid, setOrcid] = useState(orcidNumbers);

  function handleRemove() {
    setOrcid([]);
    setIsUsingOrcid((ev) => !ev);
    setGivenName("");
    setFamilyName("");
    setError("");

    setFieldValue(`${name}.given_name`, undefined);
    setFieldValue(`${name}.family_name`, undefined);
    setFieldValue(`${name}.identifiers`, undefined);
  }

  const handleSubmit = async (orcid) => {
    const url = `https://pub.orcid.org/v3.0/${orcid}`;
    setOrcid([orcid]);
    setError("");
    setIsLoading(true);

    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });

      if (!response.ok) {
        const message = `Error fetching ORCID data: ${response.status}`;
        setError(message);
        throw new Error(message);
      }

      const data = await response.json();
      const givenName = data.person.name["given-names"]?.value || "N/A";
      const familyName = data.person.name["family-name"]?.value || "N/A";

      setGivenName(givenName);
      setFamilyName(familyName);

      if (givenName && familyName) {
        setFieldValue(`${name}.given_name`, givenName);
        setFieldValue(`${name}.family_name`, familyName);
        setFieldValue(`${name}.identifiers`, [`orcid:${orcid}`]);
      }

      return { givenName, familyName };
    } catch (error) {
      console.log(error);
      setOrcid([])
    } finally {
      setIsLoading(false);
    }
  }

  const hasValidOrcid =
    Array.isArray(orcid) &&
    orcid.length === 1 &&
    typeof orcid[0] === "string" &&
    givenName &&
    familyName;

  const hasContactData =
    !!givenName ||
    !!familyName ||
    (Array.isArray(orcid) && orcid.length > 0);
  
  if(isLoading) return <Spinner/>

  if (hasValidOrcid) {
    return (
      <OrcidInfo
        orcid={orcid}
        givenName={givenName}
        familyName={familyName}
        onRemove={handleRemove}
        setUseOrcid={setIsUsingOrcid}
      />
    );
  }

  if (hasContactData) {
    return (
      <>
        <UseOrcidButton 
          onClick={() => {
            handleRemove();
            setIsUsingOrcid(true);
          }}
        />
        <ContactForm name={name} />
      </>
    );
  }

  if (isUsingOrcid) {
    return (
      <OrcidForm
        orcid={orcid}
        setHasOrcid={setIsUsingOrcid}
        handleSubmit={handleSubmit}
        onRemove={handleRemove}
        error={error}
        isLoading={isLoading}
      />
    );
  }

  return (
    <>
      <UseOrcidButton 
        onClick={() => {
          handleRemove();
          setIsUsingOrcid(true);
        }}
      />
      <ContactForm name={name} />
    </>
  );
}