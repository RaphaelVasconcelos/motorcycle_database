from pymongo import MongoClient
from src.adapters.repository.configs import MotorcycleMongoDbRepositoryConfig
from src.adapters.repository.port import MotorcycleRepository
from src.models.motorcycle import Motorcycle


class MongoDbMotorcycleRepository(MotorcycleRepository):
    def __init__(self, config: MotorcycleMongoDbRepositoryConfig = MotorcycleMongoDbRepositoryConfig()):
        self._client = MongoClient(config.connection_string)
        self.motorcycle_db = self._client[config.database]

    def add(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        result = collection_name.insert_one(motorcycle.dict())
        return result.acknowledged

    def update(self, motorcycle: Motorcycle):
        pass

    def remove(self, motorcycle: Motorcycle):
        pass

    def get(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        return collection_name.find_one({"name": motorcycle.name})

    def list(self):
        pass