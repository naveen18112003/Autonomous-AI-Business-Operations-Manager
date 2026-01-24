import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FileUpload from '../components/FileUpload';
import apiClient from '../api/apiClient';
import { ArrowRight, Loader2 } from 'lucide-react';

const Overview = () => {
    const [file, setFile] = useState(null);
    const [notes, setNotes] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleAnalyze = async () => {
        if (!file && !notes) return;

        setLoading(true);
        const formData = new FormData();
        if (file) formData.append('file', file);
        if (notes) formData.append('text_input', notes);

        try {
            const response = await apiClient.post('/analyze/', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });

            localStorage.setItem('analysisData', JSON.stringify(response.data));
            navigate('/insights');
        } catch (error) {
            console.error("Analysis failed:", error);
            const errorMessage = error.response?.data?.detail || error.message || "Analysis failed. Please check backend connection.";
            alert(`Error: ${errorMessage}`);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '1rem', color: 'var(--text-primary)' }}>Overview</h1>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
                Welcome to **Autonomous AI Business Operations Manager**. Upload your data to get started.
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
                <div className="card">
                    <h2 style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>1. Upload Data</h2>
                    <FileUpload onFileSelect={setFile} selectedFile={file} />
                </div>

                <div className="card">
                    <h2 style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>2. Operational Notes</h2>
                    <textarea
                        className="input-field"
                        rows="6"
                        placeholder="Enter specific challenges, goals, or context..."
                        value={notes}
                        onChange={(e) => setNotes(e.target.value)}
                    ></textarea>
                </div>
            </div>

            <div style={{ marginTop: '2rem', textAlign: 'right' }}>
                <button
                    className="btn btn-primary"
                    onClick={handleAnalyze}
                    disabled={loading || (!file && !notes)}
                    style={{ opacity: (loading || (!file && !notes)) ? 0.5 : 1, padding: '1rem 2rem', fontSize: '1.1rem' }}
                >
                    {loading ? (
                        <>
                            <Loader2 className="animate-spin" size={20} style={{ marginRight: '0.5rem' }} />
                            Analyzing...
                        </>
                    ) : (
                        <>
                            Run AI Analysis
                            <ArrowRight size={20} style={{ marginLeft: '0.5rem' }} />
                        </>
                    )}
                </button>
            </div>
        </div>
    );
};

export default Overview;
