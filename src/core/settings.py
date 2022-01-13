from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8082

    debug: bool = False

    class Config:
        case_sensitive = False
        fields = {
            "host": {"env": "host"},
            "port": {"env": "port"},
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()
