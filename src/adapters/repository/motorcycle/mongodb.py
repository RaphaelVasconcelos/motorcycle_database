from pymongo import MongoClient
from bson.json_util import dumps, loads
from src.adapters.repository.configs import MongoDbRepositoryConfig
from src.adapters.repository.motorcycle.port import MotorcycleRepository
from src.models.motorcycle.motorcycle import Motorcycle


class MongoDbMotorcycleRepository(MotorcycleRepository):
    def __init__(self, config: MongoDbRepositoryConfig = MongoDbRepositoryConfig()):
        self._client = MongoClient(config.connection_string)
        self.motorcycle_db = self._client[config.database]

    def add(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        result = collection_name.insert_one(motorcycle.dict())
        return result.acknowledged

    def update(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        result = collection_name.replace_one({"name": motorcycle.name}, motorcycle.dict())
        return result.modified_count > 0

    def remove(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        result = collection_name.delete_one({"name": motorcycle.name})
        return result.deleted_count > 0

    def get(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        list_cur = collection_name.find_one({"name": motorcycle.name})
        json_data = dumps(list_cur)
        motorcycle = Motorcycle.parse_obj(loads(json_data))
        return motorcycle

    def motorcycle_list(self):
        collection_name = self.motorcycle_db['motorcycles']
        cursor = collection_name.find({})
        return list(cursor)
