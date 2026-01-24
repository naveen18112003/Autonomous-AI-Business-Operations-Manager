import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, BrainCircuit, ShieldAlert, KanbanSquare, FileText } from 'lucide-react';

const Sidebar = () => {
    const navItems = [
        { to: "/overview", icon: <LayoutDashboard size={20} />, label: "Overview" },
        { to: "/insights", icon: <BrainCircuit size={20} />, label: "AI Insights" },
        { to: "/risk", icon: <ShieldAlert size={20} />, label: "Risk Assessment" },
        { to: "/execution", icon: <KanbanSquare size={20} />, label: "Execution Plan" },
        { to: "/reports", icon: <FileText size={20} />, label: "Reports" },
    ];

    return (
        <aside className="sidebar">
            <div style={{ marginBottom: '2rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <div style={{ width: '32px', height: '32px', background: 'var(--accent-primary)', borderRadius: '8px' }}></div>
                <h2 style={{ fontSize: '1.25rem', fontWeight: 'bold', lineHeight: '1.2' }}>Autonomous AI<br />Business Ops Manager</h2>
            </div>

            <nav style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                {navItems.map((item) => (
                    <NavLink
                        key={item.to}
                        to={item.to}
                        className={({ isActive }) =>
                            `btn ${isActive ? 'btn-primary' : ''}`
                        }
                        style={({ isActive }) => ({
                            justifyContent: 'flex-start',
                            gap: '0.75rem',
                        })}
                    >
                        {item.icon}
                        {item.label}
                    </NavLink>
                ))}
            </nav>
        </aside>
    );
};

export default Sidebar;
