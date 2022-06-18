from src.adapters.repository.port import MotorcycleRepository
from src.models.motorcycle import Motorcycle


class MotorcycleListRepository(MotorcycleRepository):

    def __init__(self):
        self._collection = []

    def add(self, motorcycle: Motorcycle):
        self._collection.append(motorcycle)
        return motorcycle
