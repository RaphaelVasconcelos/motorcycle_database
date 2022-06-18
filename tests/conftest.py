import pytest
from src.entrypoints.payload_models import ClientPayload

from src.models.data_from_client import DataFromClient
from src.models.motorcycle import Motorcycle


@pytest.fixture
def data_from_client_message():
    return {
        'name': "CB",
        'manufacturer': "HONDA",
        'release_year': '2021',
    }


@pytest.fixture
def client_payload(data_from_client_message):
    return ClientPayload(
        name=data_from_client_message["name"],
        manufacturer=data_from_client_message["manufacturer"],
        release_year=data_from_client_message["release_year"],
    )


@pytest.fixture
def data_from_client(data_from_client_message):
    return DataFromClient.parse_obj(data_from_client_message)


@pytest.fixture
def motorcycle(data_from_client_message):
    return Motorcycle.parse_obj(data_from_client_message)
