import pytest


@pytest.mark.asyncio
async def test_create_application(auth_client):
    response = await auth_client.post(
        "/applications/",
        json={"company": "Acme", "role": "Backend Engineer"},
    )
    assert response.status_code == 201
    assert response.json()["company"] == "Acme"


@pytest.mark.asyncio
async def test_get_missing_application(client):
    response = await client.get("/applications/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_then_list(auth_client):
    await auth_client.post("/applications/", json={"company": "Acme", "role": "Backend"})
    await auth_client.post("/applications/", json={"company": "Globex", "role": "Fullstack"})

    response = await auth_client.get("/applications/")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.asyncio
async def test_delete_application(auth_client):
    create = await auth_client.post("/applications/", json={"company": "Acme", "role": "Backend"})
    application_id = create.json()["id"]

    response = await auth_client.delete(f"/applications/{application_id}")
    assert response.status_code == 204

    check = await auth_client.get(f"/applications/{application_id}")
    assert check.status_code == 404


@pytest.mark.asyncio
async def test_update_application(auth_client):
    create = await auth_client.post("/applications/", json={"company": "Acme", "role": "Backend"})
    application_id = create.json()["id"]

    response = await auth_client.patch(f"/applications/{application_id}", json={"status": "interviewing"})
    assert response.status_code == 200
    assert response.json()["status"] == "interviewing"


@pytest.mark.asyncio
async def test_update_missing_application(auth_client):
    response = await auth_client.patch("/applications/999", json={"status": "interviewing"})
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_missing_application(auth_client):
    response = await auth_client.delete("/applications/999")
    assert response.status_code == 404
