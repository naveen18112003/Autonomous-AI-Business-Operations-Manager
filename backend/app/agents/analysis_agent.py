import json
from app.services.llm_service import llm_service
from app.models.agent_models import AnalysisRequest, AnalysisResponse
import logging

logger = logging.getLogger(__name__)

class AnalysisAgent:
    def __init__(self):
        import os
        current_dir = os.path.dirname(__file__)
        prompt_path = os.path.join(current_dir, "../../app/prompts/analysis_prompt.txt")
        # Fallback if structure is slightly different or ensure absolute resolution
        prompt_path = os.path.abspath(prompt_path)
        
        try:
            with open(prompt_path, "r") as f:
                self.prompt_template = f.read()
        except FileNotFoundError:
             # Try alternative path for safety (e.g. if run from different root)
             base_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) # root/backend/app/agents -> root
             # Actually, best is to rely on package structure relative to THIS file.
             # This file: .../backend/app/agents/analysis_agent.py
             # Prompt: .../backend/app/prompts/analysis_prompt.txt
             # Relative: ../prompts/analysis_prompt.txt
             prompt_path = os.path.join(current_dir, "../prompts/analysis_prompt.txt")
             with open(prompt_path, "r") as f:
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
