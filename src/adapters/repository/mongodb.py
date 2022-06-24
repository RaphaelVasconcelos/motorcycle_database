from pymongo import MongoClient
from src.adapters.repository.configs import MongoDbConfig
from src.adapters.repository.port import MotorcycleRepository
from src.models.motorcycle import Motorcycle


class MongoDbRepository(MotorcycleRepository):
    def __init__(self, config: MongoDbConfig = MongoDbConfig()):
        self._client = MongoClient(config.connection_string)
        self.motorcycle_db = self._client[config.database]

    def add(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        collection_name.insert_one(motorcycle.dict())

    def update(self, motorcycle: Motorcycle):
        pass

    def remove(self, motorcycle: Motorcycle):
        pass

    def get(self, motorcycle: Motorcycle):
        collection_name = self.motorcycle_db['motorcycles']
        return collection_name.find_one({"name": motorcycle.name})

    def list(self):
        pass
