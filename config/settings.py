from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_TITLE: str = "Axiomind API"
    API_VERSION: str = "0.1.0"
    LOG_LEVEL: str = "INFO"
    
    # Database
    DATABASE_URL: str
    
    # Qdrant
    QDRANT_HOST: str
    QDRANT_PORT: int = 6333
    
    class Config:
        env_file = ".env"

settings = Settings()
