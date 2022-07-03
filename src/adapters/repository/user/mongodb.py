from pymongo import MongoClient
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.adapters.repository.user.port import UserRepository
from src.models.user.user import User


class MongoDbUserRepository(UserRepository):
    def __init__(self, config: MongoDbRepositoryConfig = MongoDbRepositoryConfig()):
        self._client = MongoClient(config.connection_string)
        self.user_db = self._client[config.database]

    def add(self, user: User):
        collection_name = self.user_db['users']
        result = collection_name.insert_one(user.dict())
        return result.acknowledged

    def update(self, user: User):
        collection_name = self.user_db['users']
        result = collection_name.replace_one({"mail": user.mail}, user.dict())
        return result.modified_count > 0

    def remove(self, user: User):
        collection_name = self.user_db['users']
        result = collection_name.delete_one({"mail": user.mail})
        return result.deleted_count > 0

    def get(self, user: User):
        collection_name = self.user_db['users']
        return collection_name.find_one({"mail": user.mail})

    def user_list(self):
        collection_name = self.user_db['users']
        cursor = collection_name.find({})
        return list(cursor)
