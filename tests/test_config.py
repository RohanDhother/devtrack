from app.config import get_settings


def test_settings_can_read_database_url_from_environment(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost:5432/testdb")

    settings = get_settings()

    assert settings.database_url == "postgresql+asyncpg://user:pass@localhost:5432/testdb"
