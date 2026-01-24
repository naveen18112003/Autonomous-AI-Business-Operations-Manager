from fastapi import APIRouter, HTTPException
from app.agents.risk_agent import risk_agent
from app.models.agent_models import RiskRequest, RiskResponse

router = APIRouter()

@router.post("/", response_model=RiskResponse)
async def run_risk_assessment(request: RiskRequest):
    result = risk_agent.run(request)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result
