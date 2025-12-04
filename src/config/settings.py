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
    OPENAI_API_KEY: str
    
    # LangSmith
    ENABLE_LANGSMITH: bool = False
    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str
    LANGCHAIN_ENDPOINT: str
