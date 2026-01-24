import json
from app.services.llm_service import llm_service
from app.models.agent_models import DecisionRequest
import logging

logger = logging.getLogger(__name__)

class DecisionAgent:
    def __init__(self):
        with open("app/prompts/decision_prompt.txt", "r") as f:
            self.prompt_template = f.read()

    def run(self, request: DecisionRequest) -> dict:
        prompt = self.prompt_template.format(
            analysis_output=json.dumps(request.analysis_output),
            risk_output=json.dumps(request.risk_output),
            goals=request.goals
        )
        response_text = llm_service.get_response(prompt, system_message="You are a JSON-speaking CEO.")

        try:
            cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON from Decision Agent")
            return {"error": "Failed to parse strategic decisions"}

decision_agent = DecisionAgent()
