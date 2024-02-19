from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import RedisDsn

class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

class Config(BaseConfig):
    REDIS_URL: RedisDsn = "redis://localhost:6379"
    CELERY_BROKER_URL: str = "amqp://rabbit:password@localhost:5672"
    CELERY_BACKEND_URL: str = "redis://localhost:6379"


config: Config = Config()