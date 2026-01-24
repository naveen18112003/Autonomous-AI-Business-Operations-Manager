import json
from app.services.llm_service import llm_service
from app.models.agent_models import ReportRequest
import logging

logger = logging.getLogger(__name__)

class ReportingAgent:
    def __init__(self):
        import os
        current_dir = os.path.dirname(__file__)
        prompt_path = os.path.join(current_dir, "../prompts/reporting_prompt.txt")
        with open(prompt_path, "r") as f:
            self.prompt_template = f.read()

    def run(self, request: ReportRequest) -> dict:
        prompt = self.prompt_template.format(
            analysis_output=json.dumps(request.analysis_output),
            risk_output=json.dumps(request.risk_output),
            decision_output=json.dumps(request.decision_output),
            execution_output=json.dumps(request.execution_output)
        )
        response_text = llm_service.get_response(prompt, system_message="You are a JSON-speaking Executive Assistant.")

        try:
            cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON from Reporting Agent")
            return {"error": "Failed to parse report content"}

reporting_agent = ReportingAgent()
