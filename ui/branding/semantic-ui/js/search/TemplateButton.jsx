import React from 'react';

// headers for HTTP request
const headers = {"Content-Type": "application/json"}

// turn Date object into a string with the yyyy-mm-dd format
function dateFormater(date, sep="-") {
  let day = date.getDate();
  // add +1 to month because getMonth() returns month from 0 to 11
  let month = date.getMonth() + 1;
  const year = date.getFullYear();

  // show date and month in two digits
  if (day < 10) {
    day = '0' + day;
  }
  if (month < 10) {
    month = '0' + month;
  }

  return year + sep + month + sep + day;
}

// changes the template record in-place for fields that needs to be updated
function updateRecord(templateRecord){
   templateRecord.metadata.general_parameters.record_information.deposition_date = dateFormater(new Date);
}

// extracts the metadata section of the record prepares it for deposition
async function getRecordMeta( {selfLink} ) {
  try {
    const response = await fetch(selfLink, {
      method: "GET",
      headers: headers,
    });

    if (!response.ok) {
      throw new Error(`Failed to get record: ${response.statusText}`);
    }
    let templateRecord = await response.json();
    updateRecord(templateRecord);
    // we want the record in a form that can be used in an HTTP request body
    return JSON.stringify({metadata: templateRecord.metadata})

  } catch (error) {
    console.error('Error fetching record:', error);
  }
}

// creates the new record and returns it's edit page
async function createRecord( {selfLink} ) {
  try {
    const body = await getRecordMeta({selfLink})

    // removing <record-id>/draft from link as it should be of the form /api/records/<model>/
    let postLink = selfLink.split("/");
    if (postLink.at(-1) === "draft"){
      postLink = postLink.slice(0,-2)
    } else {
      postLink = postLink.slice(0,-1)
    }
    postLink = postLink.join("/");

    const response = await fetch(postLink, {
      method: "POST",
      headers: headers,
      body: body
    });

    if (!response.ok) {
      throw new Error(`Failed to create new record: ${response.statusText}`);
    }

    // the newly create record is included in the response
    // from where we'll grap the UI edit link
    const newRecord = await response.json();
    return newRecord["links"]["edit_html"];

  } catch (error) {
    console.error('Error templating record:', error);
  }
}

export default function TemplateButton({ selfLink }) {
  if (!selfLink) {
    console.log('Self link is not available')
  }

  // calls the create function and redirects to it's edit link
  async function redirectRecord() {
    window.location.href = await createRecord( {selfLink} );
  }

  return (
    <div className="flex justify-center h-10 text-20px bg-dark rounded-normal text-primary hover:text-dark hover:bg-primary transition-all" role="button">
      <button
        onClick={redirectRecord}
        className="px-4"
      >
        Duplicate Record
      </button>
    </div>
  );
}