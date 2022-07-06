from pymongo import MongoClient
import pytest
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.entrypoints.payload_models import ClientPayload

from src.models.motorcycle.data_from_client import DataFromClient
from src.models.motorcycle.motorcycle import Motorcycle


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
def mongodb_repository(motorcycle):
    config = MongoDbRepositoryConfig()
    client = MongoClient(config.connection_string)
    motorcycle_db = client[config.database]
    collection_name = motorcycle_db['motorcycles']
    collection_name.insert_one(motorcycle.dict())


@pytest.fixture(autouse=True)
def clean_mongo_motorcycle_collection():
    mongodb_repository_config = MongoDbRepositoryConfig()
    client = MongoClient(mongodb_repository_config.connection_string)
    motorcycle_db = client[mongodb_repository_config.database]
    collection_name = motorcycle_db['motorcycles']
    collection_name.delete_many({})
