import React from 'react';

export default function PublishButton({ selfLink }) {

  return (
    <div className="flex justify-center h-10 text-20px bg-dark rounded-normal text-primary hover:text-dark hover:bg-primary transition-all" role="button">
      <button 
        className="px-4"
      >
        {selfLink}
      </button>
    </div>
  );
}