import React, { useEffect, useState } from 'react';
import MetricCard from '../components/MetricCard';
import { AlertCircle, CheckCircle } from 'lucide-react';

const AIInsights = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const savedData = localStorage.getItem('analysisData');
        if (savedData) {
            setData(JSON.parse(savedData));
        }
    }, []);

    if (!data) return <div className="p-4">No analysis data found. Please run analysis from Overview.</div>;

    const { metric_summary, key_trends, anomalies, root_causes } = data;

    return (
        <div>
            <h1 style={{ fontSize: '2rem', fontWeight: 'bold', marginBottom: '2rem' }}>AI Insights</h1>


            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
                {Object.entries(metric_summary || {}).map(([key, value]) => (
                    <MetricCard
                        key={key}
                        title={key.replace(/_/g, ' ').toUpperCase()}
                        value={value}
                        trend="up"
                    />
                ))}
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
                <div className="card">
                    <h2 style={{ fontSize: '1.25rem', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <CheckCircle color="var(--success)" size={20} /> Key Trends
                    </h2>
                    <ul style={{ listStyleType: 'disc', paddingLeft: '1.5rem', color: 'var(--text-secondary)' }}>
                        {key_trends?.map((trend, i) => (
                            <li key={i} style={{ marginBottom: '0.5rem' }}>{trend}</li>
                        ))}
                    </ul>
                </div>

                <div className="card">
                    <h2 style={{ fontSize: '1.25rem', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <AlertCircle color="var(--warning)" size={20} /> Anomalies Detected
                    </h2>
                    <ul style={{ listStyleType: 'disc', paddingLeft: '1.5rem', color: 'var(--text-secondary)' }}>
                        {anomalies?.map((anomaly, i) => (
                            <li key={i} style={{ marginBottom: '0.5rem' }}>{anomaly}</li>
                        ))}
                    </ul>
                </div>
            </div>

            <div className="card" style={{ marginTop: '2rem' }}>
                <h2 style={{ fontSize: '1.25rem', marginBottom: '1rem' }}>Root Cause Analysis</h2>
                <ul style={{ listStyleType: 'disc', paddingLeft: '1.5rem', color: 'var(--text-secondary)' }}>
                    {root_causes?.map((cause, i) => (
                        <li key={i} style={{ marginBottom: '0.5rem' }}>{cause}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default AIInsights;
