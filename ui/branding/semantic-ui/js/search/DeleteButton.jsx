import React from 'react';

export default function DeleteButton({ selfLink }) {

  if (!selfLink) {
    return <div>Record metadata is not available.</div>;
  }

  console.log(selfLink, 'SelfLink');

  async function deleteRecord() {
    try {
      const response = await fetch(selfLink, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error(`Failed to delete record: ${response.statusText}`);
      }

      console.log('Record deleted successfully');
    } catch (error) {
      console.error('Error deleting record:', error);
    }
  }
  
  return (
    <div className="flex justify-center h-[40px] text-20px bg-accent rounded-normal text-primary hover:text-dark hover:bg-primary transition-all" role="button">
      <button 
        onClick={deleteRecord}
        className="px-4"
      >
        Delete
      </button>
    </div>
  );
}