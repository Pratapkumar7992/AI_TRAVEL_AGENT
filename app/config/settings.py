from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME:str
    DEBUG:bool
    HOST:str
    PORT:int
    
    class Config:
        env_file = ".env"
        
settings = Settings()