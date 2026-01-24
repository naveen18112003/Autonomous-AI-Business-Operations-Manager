import React, { useRef } from 'react';
import { UploadCloud } from 'lucide-react';

const FileUpload = ({ onFileSelect, selectedFile }) => {
    const fileInputRef = useRef(null);

    const handleDragOver = (e) => {
        e.preventDefault();
    };

    const handleDrop = (e) => {
        e.preventDefault();
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            onFileSelect(e.dataTransfer.files[0]);
        }
    };

    return (
        <div
            className="card"
            style={{
                borderStyle: 'dashed',
                borderWidth: '2px',
                borderColor: 'var(--border)',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                padding: '2rem'
            }}
            onClick={() => fileInputRef.current.click()}
            onDragOver={handleDragOver}
            onDrop={handleDrop}
        >
            <input
                type="file"
                ref={fileInputRef}
                onChange={(e) => e.target.files[0] && onFileSelect(e.target.files[0])}
                style={{ display: 'none' }}
                accept=".csv,.txt"
            />
            <UploadCloud size={32} color="var(--text-secondary)" style={{ marginBottom: '1rem' }} />
            <p style={{ color: 'var(--text-primary)', fontWeight: '500' }}>
                {selectedFile ? selectedFile.name : "Click or drag file to upload"}
            </p>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem' }}>
                Supports CSV, TXT
            </p>
        </div>
    );
};

export default FileUpload;
