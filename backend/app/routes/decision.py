from fastapi import APIRouter, HTTPException
from app.agents.decision_agent import decision_agent
from app.models.agent_models import DecisionRequest, DecisionResponse

router = APIRouter()

@router.post("/", response_model=DecisionResponse)
async def run_decision_making(request: DecisionRequest):
    result = decision_agent.run(request)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result
