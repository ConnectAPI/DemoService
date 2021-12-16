from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 6432

    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
