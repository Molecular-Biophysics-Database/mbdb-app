import React from 'react';
import { useDepositApiClient } from "@js/oarepo_ui";

export default function DeleteButton() {
  const { values: recordMetadata } = useDepositApiClient();

  if (!recordMetadata || !recordMetadata.links || !recordMetadata.links.self) {
    return <div>Record metadata is not available.</div>;
  }

  console.log(recordMetadata, 'RecordMetadata');

  async function deleteRecord(recordMetadata) {
    try {
      const response = await fetch(recordMetadata.links.self, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error(`Failed to delete file: ${response.statusText}`);
      }

      console.log('Record deleted successfully');
    } catch (error) {
      console.error('Error deleting record:', error);
    }
  }
  
  return (
    <div className="flex justify-center h-[40px] text-20px bg-accent rounded-normal text-primary hover:text-dark hover:bg-primary transition-all" role="button">
      <button 
        onClick={() => deleteRecord(recordMetadata)}
        className="px-4"
      >
        Delete
      </button>
    </div>
  );
}