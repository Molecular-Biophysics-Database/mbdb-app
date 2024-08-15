import React from 'react';

export default function TemplateButton({ selfLink }) {

  if (!selfLink) {
    console.log('Self link is not available')
  }

  async function getRecord() {
    try {
      const response = await fetch(selfLink, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error(`Failed to get record: ${response.statusText}`);
      }
      const templateRecord = await response.json();
      // we want the record in a form that can be used in an HTTP request body
      return JSON.stringify(templateRecord)

    } catch (error) {
      console.error('Error fetching record:', error);
    }
  }

  async function postRecord() {
    try {
      // removing <record-id>/ from link as it should be of the form /api/records/<model>/
      const postLink = selfLink.split("/").slice(0,-2).join("/")
      const body = await getRecord()
      const response = await fetch(postLink, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: body
      });

      if (!response.ok) {
        throw new Error(`Failed to create new record: ${response.statusText}`);
      }

      // the newly create record is included in the response
      // from where we'll grap the UI edit link
      const newRecord = await response.json();
      const editLink = newRecord["links"]["edit_html"]

      window.location.href = editLink;

    } catch (error) {
      console.error('Error templating record:', error);
    }
  }

  return (
    <div className="flex justify-center h-10 text-20px bg-dark rounded-normal text-primary hover:text-dark hover:bg-primary transition-all" role="button">
      <button
        onClick={postRecord}
        className="px-4"
      >
        Duplicate Record
      </button>
    </div>
  );
}