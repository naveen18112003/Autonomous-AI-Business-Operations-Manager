import React, { useState } from 'react';
import apiClient from '../api/apiClient';
import { FileDown, Loader2 } from 'lucide-react';

const Reports = () => {
    const [loading, setLoading] = useState(false);

    const downloadReport = async () => {
        const analysisData = JSON.parse(localStorage.getItem('analysisData'));
        const riskData = JSON.parse(localStorage.getItem('riskData'));
        const decisionData = JSON.parse(localStorage.getItem('decisionData'));
        const executionData = JSON.parse(localStorage.getItem('executionData'));

        if (!analysisData || !riskData || !decisionData || !executionData) {
            alert("Incomplete data. Please complete the full workflow (Analysis -> Risk -> Execution) first.");
            return;
        }

        setLoading(true);
        try {
            const response = await apiClient.post('/report/', {
                analysis_output: analysisData,
                risk_output: riskData,
                decision_output: decisionData,
                execution_output: executionData
            }, {
                responseType: 'blob'
            });

            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'Executive_Report.pdf');
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (error) {
            console.error("Report generation failed:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ textAlign: 'center', paddingTop: '4rem' }}>
            <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', marginBottom: '1.5rem' }}>Executive PDF Report</h1>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '3rem', maxWidth: '600px', margin: '0 auto 3rem auto' }}>
                Generate a comprehensive, boardroom-ready PDF report compiling all AI insights, risks, strategic decisions, and execution roadmaps.
            </p>

            <button
                className="btn btn-primary"
                onClick={downloadReport}
                disabled={loading}
                style={{ padding: '1.5rem 3rem', fontSize: '1.25rem' }}
            >
                {loading ? (
                    <>
                        <Loader2 className="animate-spin" size={24} style={{ marginRight: '1rem' }} />
                        Generating Report...
                    </>
                ) : (
                    <>
                        <FileDown size={24} style={{ marginRight: '1rem' }} />
                        Download CEO Report
                    </>
                )}
            </button>
        </div>
    );
};

export default Reports;
