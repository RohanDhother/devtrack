import pytest


@pytest.mark.asyncio
async def test_auth_flow(client):
    register = await client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "supersecret"},
    )
    assert register.status_code == 201

    login = await client.post(
        "/auth/login",
        data={"username": "test@example.com", "password": "supersecret"},
    )
    assert login.status_code == 200
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = await client.post(
        "/applications/",
        json={"company": "Acme", "role": "Backend Engineer"},
        headers=headers,
    )
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_protected_route_rejects_no_auth(client):
    response = await client.post(
        "/applications/",
        json={"company": "Acme", "role": "Backend Engineer"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_register_duplicate_email(client):
    await client.post("/auth/register", json={"email": "dupe@example.com", "password": "supersecret"})
    response = await client.post("/auth/register", json={"email": "dupe@example.com", "password": "supersecret"})
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_login_wrong_password(client):
    await client.post("/auth/register", json={"email": "user@example.com", "password": "correctpass"})
    response = await client.post(
        "/auth/login",
        data={"username": "user@example.com", "password": "wrongpass"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_login_nonexistent_user(client):
    response = await client.post(
        "/auth/login",
        data={"username": "ghost@example.com", "password": "whatever"},
    )
    assert response.status_code == 401
