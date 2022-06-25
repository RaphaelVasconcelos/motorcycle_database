import json
from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
@pytest.mark.usefixtures('mongodb_repository')
async def test_handle_list_motorcycle(
    http_client: AsyncClient,
    client_payload,
    motorcycle,
):
    response = await http_client.post(
        '/v1/motorcycle/list/',
        json=json.loads(client_payload.json())
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == motorcycle.dict()["name"]
