import abc


class FavoriteMotorcycleRepository(abc.ABC):

    @abc.abstractmethod
    def add_favorite_motorcycle(self, data: dict):
        raise NotImplementedError
