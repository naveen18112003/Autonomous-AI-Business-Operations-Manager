import json
from app.services.llm_service import llm_service
from app.models.agent_models import ExecutionRequest
import logging

logger = logging.getLogger(__name__)

class ExecutionAgent:
    def __init__(self):
        with open("app/prompts/execution_prompt.txt", "r") as f:
            self.prompt_template = f.read()

    def run(self, request: ExecutionRequest) -> dict:
        prompt = self.prompt_template.format(decision_output=json.dumps(request.decision_output))
        response_text = llm_service.get_response(prompt, system_message="You are a JSON-speaking COO.")

        try:
            cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON from Execution Agent")
            return {"error": "Failed to parse execution plan"}

execution_agent = ExecutionAgent()
