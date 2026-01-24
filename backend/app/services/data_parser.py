import pandas as pd
import io
import logging

logger = logging.getLogger(__name__)

class DataParser:
    @staticmethod
    def parse_csv(file_content: bytes) -> str:
        try:
            df = pd.read_csv(io.BytesIO(file_content))
            return df.head(50).to_string()
        except Exception as e:
            logger.error(f"Error parsing CSV: {e}")
            raise Exception("Failed to parse CSV file")

    @staticmethod
    def parse_text(text: str) -> str:
        return text.strip()

data_parser = DataParser()
