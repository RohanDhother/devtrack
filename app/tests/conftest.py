import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.config import get_settings
from app.database import Base, get_db
from app.main import app

settings = get_settings()
test_engine = create_async_engine(settings.test_database_url, poolclass=NullPool)
TestSessionLocal = async_sessionmaker(test_engine, expire_on_commit=False)


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest_asyncio.fixture
async def client():
    async def override_get_db():
        async with TestSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def auth_client(client):
    await client.post(
        "/auth/register",
        json={"email": "tester@example.com", "password": "supersecret"},
    )
    login = await client.post(
        "/auth/login",
        data={"username": "tester@example.com", "password": "supersecret"},
    )
    token = login.json()["access_token"]
    client.headers["Authorization"] = f"Bearer {token}"
    return client
