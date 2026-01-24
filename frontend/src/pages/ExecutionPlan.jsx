import React, { useState } from 'react';
import apiClient from '../api/apiClient';
import { Target, Calendar, User, Loader2 } from 'lucide-react';

const ExecutionPlan = () => {
    const [executionData, setExecutionData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [step, setStep] = useState(0); 

    const generatePlan = async () => {
        const analysisData = JSON.parse(localStorage.getItem('analysisData'));
        const riskData = JSON.parse(localStorage.getItem('riskData'));

        if (!analysisData || !riskData) {
            alert("Missing Analysis or Risk data. Please run previous steps.");
            return;
        }

        setLoading(true);
        try {

            const decisionRes = await apiClient.post('/decision/', {
                analysis_output: analysisData,
                risk_output: riskData,
                goals: "Maximize revenue while maintaining stability."
            });
            localStorage.setItem('decisionData', JSON.stringify(decisionRes.data));

            const executionRes = await apiClient.post('/execution/', {
                decision_output: decisionRes.data
            });
            setExecutionData(executionRes.data);
            localStorage.setItem('executionData', JSON.stringify(executionRes.data));
        } catch (error) {
            console.error("Execution planning failed:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
                <h1 style={{ fontSize: '2rem', fontWeight: 'bold' }}>Strategic Execution Plan</h1>
                <button className="btn btn-primary" onClick={generatePlan} disabled={loading}>
                    {loading ? <Loader2 className="animate-spin" /> : "Generate Strategy & Plan"}
                </button>
            </div>

            {executionData && (
                <div style={{ display: 'grid', gap: '1.5rem' }}>
                    {executionData.roadmap?.map((item, idx) => (
                        <div key={idx} className="card" style={{ display: 'flex', gap: '1.5rem' }}>
                            <div style={{
                                minWidth: '40px', height: '40px',
                                borderRadius: '50%', backgroundColor: 'var(--accent-primary)',
                                color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center',
                                fontWeight: 'bold', fontSize: '1.25rem'
                            }}>
                                {item.step}
                            </div>
                            <div style={{ flex: 1 }}>
                                <h3 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '0.5rem' }}>{item.action}</h3>
                                <div style={{ display: 'flex', gap: '2rem', color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                                    <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}><User size={16} /> {item.owner}</span>
                                    <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}><Calendar size={16} /> {item.timeline}</span>
                                    <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}><Target size={16} /> {item.kpi}</span>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default ExecutionPlan;
