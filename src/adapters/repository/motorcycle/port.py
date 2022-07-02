import abc

from src.models.motorcycle import Motorcycle


class MotorcycleRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data: dict) -> Motorcycle:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: dict) -> Motorcycle:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, data: dict) -> Motorcycle:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, data: dict) -> Motorcycle:
        raise NotImplementedError

    @abc.abstractmethod
    def motorcycle_list(self, data: dict) -> Motorcycle:
        raise NotImplementedError
