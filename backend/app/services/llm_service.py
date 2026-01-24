from openai import OpenAI
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_BASE_URL
        )
        self.model = settings.OPENAI_MODEL_NAME

    def get_response(self, prompt: str, system_message: str = "You are a helpful AI assistant.") -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Error calling OpenAI API: {error_msg}")
            # Raise a more descriptive error so the UI can show what's wrong
            raise Exception(f"AI Model Response Failed: {error_msg}")

llm_service = LLMService()
