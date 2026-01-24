import React, { useState } from 'react';
import apiClient from '../api/apiClient';
import { Shield, AlertTriangle, Loader2 } from 'lucide-react';

const RiskAssessment = () => {
    const [riskData, setRiskData] = useState(null);
    const [loading, setLoading] = useState(false);

    const runRiskAssessment = async () => {
        const analysisData = JSON.parse(localStorage.getItem('analysisData'));
        if (!analysisData) {
            alert("No analysis data found. Please run analysis first.");
            return;
        }

        setLoading(true);
        try {
            const response = await apiClient.post('/risk/', { analysis_output: analysisData });
            setRiskData(response.data);
            localStorage.setItem('riskData', JSON.stringify(response.data));
        } catch (error) {
            console.error("Risk assessment failed:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
                <h1 style={{ fontSize: '2rem', fontWeight: 'bold' }}>Risk Assessment</h1>
                <button className="btn btn-primary" onClick={runRiskAssessment} disabled={loading}>
                    {loading ? <Loader2 className="animate-spin" /> : "Run Risk Agent"}
                </button>
            </div>

            {riskData && (
                <>
                    <div className="card" style={{ marginBottom: '2rem', borderColor: riskData.overall_risk_score > 7 ? 'var(--error)' : 'var(--border)' }}>
                        <h2 style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>Overall Risk Score</h2>
                        <div style={{ fontSize: '3rem', fontWeight: 'bold', color: riskData.overall_risk_score > 7 ? 'var(--error)' : 'var(--warning)' }}>
                            {riskData.overall_risk_score}/10
                        </div>
                    </div>

                    <div style={{ display: 'grid', gap: '1.5rem' }}>
                        {riskData.risks?.map((risk, idx) => (
                            <div key={idx} className="card">
                                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600' }}>{risk.name}</h3>
                                    <span style={{
                                        padding: '0.25rem 0.75rem',
                                        borderRadius: '1rem',
                                        backgroundColor: risk.severity > 7 ? 'rgba(239, 68, 68, 0.2)' : 'rgba(245, 158, 11, 0.2)',
                                        color: risk.severity > 7 ? 'var(--error)' : 'var(--warning)',
                                        fontWeight: 'bold'
                                    }}>
                                        Severity: {risk.severity}
                                    </span>
                                </div>
                                <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem' }}>{risk.description}</p>
                                <div style={{ backgroundColor: 'var(--bg-primary)', padding: '1rem', borderRadius: '0.5rem' }}>
                                    <strong>Mitigation:</strong> {risk.mitigation}
                                </div>
                            </div>
                        ))}
                    </div>
                </>
            )}
        </div>
    );
};

export default RiskAssessment;
