import abc


class FavoriteMotorcycleRepository(abc.ABC):

    @abc.abstractmethod
    def add_favorite_motorcycle(self, data: dict):
        raise NotImplementedError

    def get_favorite_motorcycles(self, data: dict):
        raise NotImplementedError

    def remove_favorite_motorcycle(self, data: dict):
        raise NotImplementedError
