import abc

from src.models.motorcycle import Motorcycle


class MotorcycleRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data: dict) -> Motorcycle:
        pass

    @abc.abstractmethod
    def update(self, data: dict) -> Motorcycle:
        pass
