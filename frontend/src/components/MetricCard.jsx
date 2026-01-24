import React from 'react';

const MetricCard = ({ title, value, change, trend }) => {
    const isPositive = trend === 'up';

    return (
        <div className="card">
            <h3 style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', marginBottom: '0.5rem' }}>{title}</h3>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: '0.5rem' }}>
                <span style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--text-primary)' }}>{value}</span>
                {change && (
                    <span style={{
                        fontSize: '0.875rem',
                        color: isPositive ? 'var(--success)' : 'var(--error)'
                    }}>
                        {isPositive ? '+' : ''}{change}
                    </span>
                )}
            </div>
        </div>
    );
};

export default MetricCard;
