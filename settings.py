import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class SettingsBase(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
