from pydantic_settings import BaseSettings


# Pydantic class
class TTSModelConfig(BaseSettings):
    api_key: str
    model_id: str
    voice: str
    speed: float
    response_format: str = "mp3"

    class Config:
        protected_namespaces = ()
