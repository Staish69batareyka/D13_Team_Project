from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field

class Configuration(BaseSettings):
    """
    Конфигурационный класс для загрузки переменных окружения
    """
    login: str = Field(..., description="Логин врача")
    base_folder: str = Field(..., description="Папка с материалами")
    
    class Config:
        env_file = "src/.env"
        env_file_encoding = "utf-8"
        case_sensitive = False  # чтобы не зависеть от регистра
