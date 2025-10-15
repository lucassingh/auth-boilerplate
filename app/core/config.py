from pydantic_settings import BaseSettings
from typing import List, Optional
from pydantic import field_validator
import json


class Settings(BaseSettings):
    # ========== API CONFIG ==========
    PROJECT_NAME: str
    VERSION: str
    DESCRIPTION: str
    API_V1_STR: str = "/api/v1"
    
    # ========== SECURITY AND JWT ==========
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # ========== DATABASE ==========
    DATABASE_URL: str
    
    # ========== EMAIL CONFIG ==========
    SMTP_HOST: Optional[str] = "localhost"
    SMTP_PORT: Optional[int] = 1025
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = None
    
    # ========== CORS ==========
    BACKEND_CORS_ORIGINS: List[str] = []
    
    # ========== ENVIRONMENT ==========
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # ========== USER FIELDS CONFIG==========
    # DEFAULT VALUES - OPTIONS IN .env
    USER_FIELDS_REQUIRED: List[str] = ["email", "password", "first_name", "last_name"]
    USER_FIELDS_OPTIONAL: List[str] = ["phone", "country", "city", "address", "date_of_birth"]
    
    # ========== VALIDATORS ==========
    @field_validator("BACKEND_CORS_ORIGINS", mode='before')
    @classmethod
    def assemble_cors_origins(cls, v):
        """Convierte string de CORS a lista"""
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [origin.strip() for origin in v.split(",") if origin.strip()]
        elif isinstance(v, list):
            return v
        return []
    
    @field_validator("USER_FIELDS_REQUIRED", "USER_FIELDS_OPTIONAL", mode='before')
    @classmethod
    def assemble_user_fields(cls, v):
        """Convierte string de campos a lista"""
        if isinstance(v, str):
            return [field.strip() for field in v.split(",") if field.strip()]
        elif isinstance(v, list):
            return v
        return None

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()