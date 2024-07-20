import secrets
from dataclasses import dataclass


@dataclass
class Config:
    DEBUG: bool = True
    TESTING: bool = False
    SECRET_KEY: str = secrets.token_urlsafe(32)