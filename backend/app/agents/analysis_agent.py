import json
from app.services.llm_service import llm_service
from app.models.agent_models import AnalysisRequest, AnalysisResponse
import logging

logger = logging.getLogger(__name__)

class AnalysisAgent:
    def __init__(self):
        with open("app/prompts/analysis_prompt.txt", "r") as f:
            self.prompt_template = f.read()

    def run(self, request: AnalysisRequest) -> dict:
        try:
            prompt = self.prompt_template.format(
                data_context=request.data,
                operational_notes=request.context or "No operational notes provided."
            )
            response_text = llm_service.get_response(prompt, system_message="You are a JSON-speaking Data Analyst.")

            try:
                import re
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    cleaned_response = json_match.group(0)
                else:
                    cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
                
                parsed_json = json.loads(cleaned_response)

                try:
                    AnalysisResponse(**parsed_json)
                except Exception as e:
                    return {"error": f"Model output validation failed: {str(e)}"}

                return parsed_json
            except json.JSONDecodeError:
                logger.error(f"Failed to decode JSON from Analysis Agent. Raw response: {response_text}")
                return {"error": "Failed to parse analysis results from AI Response"}
        except Exception as e:
            logger.error(f"Analysis Agent failed: {e}")
            print(f"CRITICAL ERROR IN ANALYSIS AGENT: {e}") 
            return {"error": f"Agent Execution Failed: {str(e)}"}

analysis_agent = AnalysisAgent()
