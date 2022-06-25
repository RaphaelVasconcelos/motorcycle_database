from src.adapters.repository.port import MotorcycleRepository
from src.models.motorcycle import Motorcycle


class MotorcycleListRepository(MotorcycleRepository):

    def __init__(self):
        self._collection = []

    def add(self, motorcycle: Motorcycle):
        self._collection.append(motorcycle)
        return motorcycle

    def update(self, motorcycle: Motorcycle):
        filtered_list = [m for m in self._collection if m.name != motorcycle.name]
        filtered_list.append(motorcycle)
        self._collection = filtered_list
        return motorcycle

    def remove(self, motorcycle: Motorcycle):
        filtered_list = [m for m in self._collection if m.name != motorcycle.name]
        self._collection = filtered_list

    def get(self, motorcycle: Motorcycle):
        filtered_list = [m for m in self._collection if m.name == motorcycle.name]
        return filtered_list[0]

    def motorcycle_list(self):
        list = [m for m in self._collection]
        return list
