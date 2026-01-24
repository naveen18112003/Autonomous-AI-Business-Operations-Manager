import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Overview from './pages/Overview';
import AIInsights from './pages/AIInsights';
import RiskAssessment from './pages/RiskAssessment';
import ExecutionPlan from './pages/ExecutionPlan';
import Reports from './pages/Reports';

function App() {
    return (
        <Router>
            <div className="dashboard-layout">
                <Sidebar />
                <main className="main-content">
                    <Routes>
                        <Route path="/" element={<Navigate to="/overview" replace />} />
                        <Route path="/overview" element={<Overview />} />
                        <Route path="/insights" element={<AIInsights />} />
                        <Route path="/risk" element={<RiskAssessment />} />
                        <Route path="/execution" element={<ExecutionPlan />} />
                        <Route path="/reports" element={<Reports />} />
                    </Routes>
                </main>
            </div>
        </Router>
    );
}

export default App;
