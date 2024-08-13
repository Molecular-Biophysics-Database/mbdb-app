import React, { useState, useEffect } from 'react';

export default function DeleteButton({ selfLink }) {
  const [showPopup, setShowPopup] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);

  useEffect(() => {
    if (showPopup || showSuccess) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    
    return () => {
      document.body.style.overflow = '';
    };
  }, [showPopup, showSuccess]);

  if (!selfLink) {
    console.log('Self link is not available')
  }

  const popUp = () => {
    setShowPopup(true);
  }

  async function deleteRecord() {
    try {
      const response = await fetch(selfLink, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error(`Failed to delete record: ${response.statusText}`);
      }

      console.log('Record deleted successfully');
      setShowPopup(false);
      setShowSuccess(true);

      setTimeout(() => {
        window.location.href = '/';
      }, 1500); // 1.5 seconds delay

    } catch (error) {
      console.error('Error deleting record:', error);
    }
  }

  return (
    <div className="flex justify-center h-10 text-20px bg-accent rounded-normal text-primary hover:text-dark hover:bg-primary transition-all" role="button">
      <button 
        onClick={popUp}
        className="px-4"
      >
        Delete
      </button>

      {showPopup && (
        <div className="fixed top-0 left-0 w-screen h-screen overflow-hidden flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded-normal">
            <div className="mb-4">Are you sure you want to delete your record? This action cannot be undone.</div>
            <div className="flex justify-between">
              <button 
                onClick={deleteRecord}
                className="bg-accent text-white px-4 h-10 rounded-normal hover:text-dark hover:bg-primary transition-all"
              >
                Yes
              </button>
              <button 
                onClick={() => setShowPopup(false)}
                className="bg-dark text-primary px-4 h-10 rounded-normal hover:text-dark hover:bg-primary transition-all"
              >
                No
              </button>
            </div>
          </div>
        </div>
      )}

      {showSuccess && (
        <div className="fixed top-0 left-0 w-screen h-screen overflow-hidden flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded-normal">
            <div className="text-lime-600 text-20px">Your record was removed successfully.</div>
          </div>
        </div>
      )}
    </div>
  );
}