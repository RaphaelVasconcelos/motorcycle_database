import abc

from src.models.user import User


class UserRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data: dict) -> User:
        raise NotImplementedError
