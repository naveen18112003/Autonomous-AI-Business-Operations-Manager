from fastapi import APIRouter, HTTPException
from app.agents.execution_agent import execution_agent
from app.models.agent_models import ExecutionRequest, ExecutionResponse

router = APIRouter()

@router.post("/", response_model=ExecutionResponse)
async def run_execution_planning(request: ExecutionRequest):
    result = execution_agent.run(request)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result
