from pymongo import MongoClient
import pytest
from src.adapters.repository.configs import MongoDbRepositoryConfig


@pytest.fixture(autouse=True)
def clean_mongo_motorcycle_collection():
    mongodb_repository_config = MongoDbRepositoryConfig()
    client = MongoClient(mongodb_repository_config.connection_string)
    motorcycle_db = client[mongodb_repository_config.database]
    collection_name = motorcycle_db['users']
    collection_name.delete_many({})
