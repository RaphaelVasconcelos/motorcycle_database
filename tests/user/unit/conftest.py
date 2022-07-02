from pymongo import MongoClient
import pytest
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.entrypoints.payload_models import ClientUserPayload
from src.models.user.user import User
from src.models.user.user_data_from_client import UserDataFromClient


@pytest.fixture
def user_data_from_client_message():
    return {
        'name': "Foo",
        'mail': "foo@bar.com",
        'age': '30',
    }


@pytest.fixture
def client_payload(user_data_from_client_message):
    return ClientUserPayload(
        name=user_data_from_client_message["name"],
        mail=user_data_from_client_message["mail"],
        age=user_data_from_client_message["age"],
    )


@pytest.fixture
def user_data_from_client(user_data_from_client_message):
    return UserDataFromClient.parse_obj(user_data_from_client_message)


@pytest.fixture
def user(user_data_from_client_message):
    return User.parse_obj(user_data_from_client_message)


@pytest.fixture
def mongodb_user_repository(user):
    config = MongoDbRepositoryConfig()
    client = MongoClient(config.connection_string)
    motorcycle_db = client[config.database]
    collection_name = motorcycle_db['users']
    collection_name.insert_one(user.dict())
