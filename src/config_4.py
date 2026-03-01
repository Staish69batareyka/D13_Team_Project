# from typing import Optional
from pydantic_settings import BaseSettings
import os
# from pydantic import Field

class Configuration(BaseSettings):
    """
    Конфигурационный класс для загрузки переменных окружения
    """
    login: str
    base_folder: str

    class Config:
        env_file = 'src/.env'
        env_file_encoding = "utf-8"
        case_sensitive = False

