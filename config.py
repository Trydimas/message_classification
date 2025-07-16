from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    LAYER_API_KEY: str

    AZURE_API_VERSION: str
    AZURE_ENDPOINT: str
    AZURE_DEPLOYMENT_NAME: str
    AZURE_API_KEY: str
    AZURE_MODEL_NAME: str = 'gpt-4o'
    AZURE_TOKEN_LIMIT: int = 35000

    LOG_LEVEL: str = "INFO"
    LOG_FOLDER: str = "../log"

    @property
    def DB_URL(self):
        return f'sqlite+aiosqlite:///test.db'


settings = Settings()
