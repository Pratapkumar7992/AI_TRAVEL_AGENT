from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

    APP_NAME:str
    DEBUG:bool
    HOST:str
    PORT:int
    GOOGLE_API_KEY:str
    LANGCHAIN_API_KEY:str=""
    LANGCHAIN_TRACING_V2:bool=False
    LANGCHAIN_PROJECT:str="AI-Travel-Planner"

    @field_validator("DEBUG", mode="before")
    @classmethod
    def parse_debug(cls, value):
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in ("debug", "true", "1", "yes"):
                return True

            if normalized in ("release", "false", "0", "no"):
                return False
        return value
        
settings = Settings()
