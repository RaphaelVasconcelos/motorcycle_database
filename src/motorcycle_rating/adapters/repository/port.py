import abc


class MotorcycleRatingRepository(abc.ABC):

    @abc.abstractmethod
    def add_motorcycle_rating(self, data: dict):
        raise NotImplementedError

    def update_motorcycle_rating(self, data: dict):
        raise NotImplementedError
