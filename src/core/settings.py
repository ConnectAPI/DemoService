from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 80

    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
