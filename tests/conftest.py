import pytest

from src.models.data_from_client import DataFromClient


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
