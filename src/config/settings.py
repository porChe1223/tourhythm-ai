from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    """
    Application Settings
    --------------------
    - All Settings are defined here
    - Can Load variables from .env
    """
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    # OpenAI
    OPENAI_API_KEY: SecretStr
    
    # LangSmith
    ENABLE_LANGSMITH: bool = False
    LANGCHAIN_TRACING_V2: SecretStr
    LANGCHAIN_ENDPOINT: SecretStr
    LANGCHAIN_PROJECT: SecretStr
    LANGCHAIN_API_KEY: SecretStr

    # Database
    POSTGRES_HOST: SecretStr
    POSTGRES_DB: SecretStr
    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr

    # Redis
    REDIS_HOST: SecretStr
    REDIS_PORT: SecretStr
    REDIS_DB: SecretStr
