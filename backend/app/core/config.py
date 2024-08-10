import secrets

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = True
    TESTING: bool = False
    WIN_HOST: str = '0.0.0.0'
    LINUX_HOST: str = '127.0.0.1'
    PORT: int = 8532
    SECRET_KEY: str = secrets.token_urlsafe(32)
