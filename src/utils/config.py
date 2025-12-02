from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables
load_dotenv()


# Pydantic class
class TTSModelConfig(BaseSettings):
    api_key: str
    model_id: str
    voice: str
    speed: float
    response_format: str = "mp3"
