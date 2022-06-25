from unittest import mock
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


@pytest.fixture
def fake_get_motorcycle_from_mongo_repository(motorcycle):
    method_path = (
        'src.adapters.repository.mongodb.MongoDbMotorcycleRepository.get'
    )
    with mock.patch(method_path, return_value=motorcycle) as mocked_method:
        yield mocked_method


@pytest.fixture
async def mock_list_repository(motorcycle):
    motorcycle_list = []
    motorcycle_list.append(motorcycle)

    method_path = (
        'src.adapters.repository.list_repository.MotorcycleListRepository.list'
    )
    with mock.patch(method_path, return_value=motorcycle_list) as mocked_method:
        yield mocked_method
