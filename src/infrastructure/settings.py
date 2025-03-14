from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    APP_PORT: int

    ASYNC_POSTGRES_POOL_SIZE: int

    TELEGRAM_TOKEN: str

    CHANNEL_ID: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def ASYNC_DB_URL(self) -> str:
        """ASYNC CONNECTION IN POSTGRES DB"""
        return (f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")

    @property
    def SYNC_DB_URL(self) -> str:
        """SYNC CONNECTION IN POSTGRES DB"""
        return (f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")


@lru_cache
def get_settings() -> Settings:
    return Settings()
