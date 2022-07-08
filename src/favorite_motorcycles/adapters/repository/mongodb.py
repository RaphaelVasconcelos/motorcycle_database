from bson.json_util import dumps, loads
from pymongo import MongoClient
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.favorite_motorcycles.adapters.repository.port import FavoriteMotorcycleRepository
from src.favorite_motorcycles.models.favorite_motorcycle import FavoriteMotorcycle


class MongoDbFavoriteMotorcycleRepository(FavoriteMotorcycleRepository):
    def __init__(self, config: MongoDbRepositoryConfig = MongoDbRepositoryConfig()):
        self._client = MongoClient(config.connection_string)
        self.motorcycle_db = self._client[config.database]

    def add_favorite_motorcycle(self, favorite_motorcycle: FavoriteMotorcycle):
        collection_name = self.motorcycle_db['users']
        result = collection_name.update_one(
            {'mail': favorite_motorcycle.mail_user},
            {'$addToSet': {'favorite_motorcycles': favorite_motorcycle.motorycle_name}}
        )
        return result.modified_count > 0

    def get_favorite_motorcycle_list(self, favorite_motorcycle: FavoriteMotorcycle):
        collection_name = self.motorcycle_db['users']
        cursor = collection_name.find_one(
            {'mail': favorite_motorcycle.mail_user},
            {'favorite_motorcycles': 1, '_id': 0}
        )
        list_favorite_motorcycles = loads(dumps(cursor))
        return list_favorite_motorcycles["favorite_motorcycles"] if list_favorite_motorcycles else []

    def remove_favorite_motorcycle(self, favorite_motorcycle: FavoriteMotorcycle):
        collection_name = self.motorcycle_db['users']
        result = collection_name.update_one(
            {'mail': favorite_motorcycle.mail_user},
            {'$pull': {'favorite_motorcycles': favorite_motorcycle.motorycle_name}}
        )
        return result.modified_count > 0
