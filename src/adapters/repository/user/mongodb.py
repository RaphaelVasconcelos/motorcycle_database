from pymongo import MongoClient
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.adapters.repository.user.port import UserRepository
from src.models.user import User


class MongoDbUserRepository(UserRepository):
    def __init__(self, config: MongoDbRepositoryConfig = MongoDbRepositoryConfig()):
        self._client = MongoClient(config.connection_string)
        self.motorcycle_db = self._client[config.database]

    def add(self, user: User):
        collection_name = self.motorcycle_db['users']
        result = collection_name.insert_one(user.dict())
        return result.acknowledged
