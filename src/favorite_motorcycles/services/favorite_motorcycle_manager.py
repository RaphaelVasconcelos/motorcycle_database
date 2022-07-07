from src.favorite_motorcycles.adapters.repository.mongodb import MongoDbFavoriteMotorcycleRepository
from src.favorite_motorcycles.factories.favorite_motorcycle import build_favorite_motorcycle
from src.models.motorcycle.data_from_client import DataFromClient


def process_new_favorite_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbFavoriteMotorcycleRepository = MongoDbFavoriteMotorcycleRepository()
):
    favorite_motorcycle = build_favorite_motorcycle(**data_from_client.dict())

    actual_favorite_motorcycles = repository.get_favorite_motorcycle_list(favorite_motorcycle)

    if favorite_motorcycle.motorycle_name in actual_favorite_motorcycles:
        return False

    return repository.add_favorite_motorcycle(favorite_motorcycle)
