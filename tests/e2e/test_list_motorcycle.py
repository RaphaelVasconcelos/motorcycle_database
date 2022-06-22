import json
from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
@pytest.mark.usefixtures('mock_list_repository')
async def test_handle_get_motorcycle(
    http_client: AsyncClient,
    client_payload,
    motorcycle,
):
    response = await http_client.post(
        '/v1/motorcycle/list/',
        json=json.loads(client_payload.json())
    )
    assert response.status_code == 200
    assert response.json() == [motorcycle.dict()]
