from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME:str
    DEBUG:bool
    HOST:str
    PORT:int

    @field_validator("DEBUG", mode="before")
    @classmethod
    def parse_debug(cls, value):
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized == "release":
                return False
            if normalized == "debug":
                return True
        return value
        
settings = Settings()
