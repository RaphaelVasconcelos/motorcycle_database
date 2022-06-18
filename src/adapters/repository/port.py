import abc

from src.models.motorcycle import Motorcycle


class MotorcycleRepository(abc.ABC):

    @abc.abstractmethod
    async def add(self, data: dict) -> Motorcycle:
        pass
