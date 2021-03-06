import abc

from src.models.user.user import User


class UserRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data: dict) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: dict) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, data: dict) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, data: dict) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def user_list(self, data: dict) -> User:
        raise NotImplementedError
