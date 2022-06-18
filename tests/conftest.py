import pytest

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
def data_from_client(data_from_client_message):
    return DataFromClient.parse_obj(data_from_client_message)


@pytest.fixture
def motorcycle(data_from_client_message):
    return Motorcycle.parse_obj(data_from_client_message)
