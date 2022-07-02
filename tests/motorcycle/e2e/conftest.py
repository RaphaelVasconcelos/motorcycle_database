from fastapi import FastAPI
from httpx import AsyncClient
import pytest
import pytest_asyncio

from src.entrypoints.server import create_app


@pytest.fixture
def test_app() -> FastAPI:
    return create_app()


@pytest_asyncio.fixture
async def http_client(test_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=test_app,
        base_url='http://test'
    ) as async_client:
        yield async_client
