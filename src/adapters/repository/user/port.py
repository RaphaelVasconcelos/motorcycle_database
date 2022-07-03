import abc

from src.models.user.user import User


class UserRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data: dict) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: dict) -> User:
        raise NotImplementedError
