from enum import Enum
from src.favorite_motorcycles.adapters.repository.mongodb import MongoDbFavoriteMotorcycleRepository

from src.favorite_motorcycles.domain.models.favorite_motorcycle import FavoriteMotorcycle


class ToggleFavorite(str, Enum):
    ADD = "add"
    REMOVE = "remove"


def action_for_this_favorite_motorcycle(
    favorite_motorcycle: FavoriteMotorcycle,
    repository: MongoDbFavoriteMotorcycleRepository
):
    actual_favorite_motorcycles = repository.get_favorite_motorcycle_list(favorite_motorcycle)
    if favorite_motorcycle.motorycle_name in actual_favorite_motorcycles:
        return ToggleFavorite.REMOVE
    return ToggleFavorite.ADD
