import json
from httpx import AsyncClient


async def test_handle_remove_motorcycle(
    http_client: AsyncClient,
    client_payload,
):
    response = await http_client.post(
        '/v1/motorcycle/remove/',
        json=json.loads(client_payload.json())
    )
    assert response.status_code == 200
    assert response.json() is True
