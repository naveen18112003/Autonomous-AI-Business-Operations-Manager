from pydantic import BaseModel
from typing import List, Dict, Optional, Any

class AnalysisRequest(BaseModel):
    data: str
    context: Optional[str] = ""

class AnalysisResponse(BaseModel):
    key_trends: List[str]
    anomalies: List[str]
    root_causes: List[str]
    metric_summary: Dict[str, Any]

class RiskRequest(BaseModel):
    analysis_output: Dict[str, Any]

class RiskResponse(BaseModel):
    risks: List[Dict[str, Any]]
    overall_risk_score: int

class DecisionRequest(BaseModel):
    analysis_output: Dict[str, Any]
    risk_output: Dict[str, Any]
    goals: str

class DecisionResponse(BaseModel):
    decisions: List[Dict[str, Any]]
    strategic_direction: str

class ExecutionRequest(BaseModel):
    decision_output: Dict[str, Any]

class ExecutionResponse(BaseModel):
    roadmap: List[Dict[str, Any]]

class ReportRequest(BaseModel):
    analysis_output: Dict[str, Any]
    risk_output: Dict[str, Any]
    decision_output: Dict[str, Any]
    execution_output: Dict[str, Any]
