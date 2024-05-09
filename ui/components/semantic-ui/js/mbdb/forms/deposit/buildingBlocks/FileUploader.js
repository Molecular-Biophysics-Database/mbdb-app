import { useState, useRef } from "react";

const FileUploader = () => {
    const [dragging, setDragging] = useState(false);
    const [droppedFiles, setDroppedFiles] = useState([]);
    const fileInputRef = useRef(null);
  
    const handleDragOver = (e) => {
      e.preventDefault();
      setDragging(true);
    };
  
    const handleDragEnter = (e) => {
      e.preventDefault();
      setDragging(true);
    };
  
    const handleDragLeave = (e) => {
      e.preventDefault();
      setDragging(false);
    };
  
    const handleDrop = (e) => {
      e.preventDefault();
      setDragging(false);
      const files = Array.from(e.dataTransfer.files);
      // Handle the dropped files
      console.log(files);
    };

    const handleDroppedFiles = (files) => {
        setDroppedFiles(files);
      };

      const handleClick = () => {
        fileInputRef.current.click();
      };
    
      const handleFileInputChange = (e) => {
        handleDroppedFiles(Array.from(e.target.files));
      };
  
    return (
      <div
        onClick={handleClick}
        onDragOver={handleDragOver}
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDrop={(e) => {
            handleDrop(e);
            handleDroppedFiles(Array.from(e.dataTransfer.files));
          }}
        style={{ border: `2px dashed ${dragging ? 'blue' : 'black'}`, padding: '20px' }}
      >
        {droppedFiles.length === 0 ? (
            <div>
            <h3>Drag & Drop Files Here</h3>
            <input
                type="file"
                ref={fileInputRef}
                style={{ display: 'none' }}
                onChange={handleFileInputChange}
                multiple
            />
            </div>
        ) : (
            <ul>
                {droppedFiles.map((file, index) => (
                    <li key={index}>{file.name}</li>
                ))}
            </ul>
        )}
      </div>
    );
  };
  
  export default FileUploader;