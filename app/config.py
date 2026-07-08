import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    database_url: str
    test_database_url: str
    secret_key: str
    algorithm: str
    access_token_ttl_hours: int


def get_settings() -> Settings:
    return Settings(
        database_url=os.getenv(
            "DATABASE_URL",
            "postgresql+asyncpg://rohan:dev_password@localhost:5432/devtrack",
        ),
        test_database_url=os.getenv(
            "TEST_DATABASE_URL",
            "postgresql+asyncpg://rohan:dev_password@localhost:5432/devtrack_test",
        ),
        secret_key=os.getenv("SECRET_KEY", "dev-secret-change-me"),
        algorithm=os.getenv("JWT_ALGORITHM", "HS256"),
        access_token_ttl_hours=int(os.getenv("ACCESS_TOKEN_TTL_HOURS", "1")),
    )
