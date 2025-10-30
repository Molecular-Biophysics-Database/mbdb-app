import React, { useState } from "react";
import ContactForm from "./ContactForm";
import { useFormikContext, getIn } from "formik";
import Spinner from "../../../buildingBlocks/Spinner";
import OrcidForm from "./OrcidForm";

export default function Contact({ name }) {
  const { values, setFieldValue } = useFormikContext();

  const getField = (field) => getIn(values, `${name}.${field}`);

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

      if (givenName && familyName) {
        setFieldValue(`${name}.given_name`, givenName);
        setFieldValue(`${name}.family_name`, familyName);
        setFieldValue(`${name}.identifiers`, [`orcid:${orcid}`]);
      }

      return { givenName, familyName };
    } catch (error) {
      console.log(error);
      setOrcid([]);
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) return <Spinner />;

  return (
    <>
      <OrcidForm
        orcid={orcid}
        handleSubmit={handleSubmit}
        onRemove={handleRemove}
        error={error}
        isLoading={isLoading}
      />
      <ContactForm name={name} />
    </>
  );
}
