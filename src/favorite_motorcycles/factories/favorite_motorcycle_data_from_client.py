from src.favorite_motorcycles.domain.models.favorite_motorcycle_data_from_client import FavoriteMotorcycleDataFromClient


def build_favorite_motorcycle_data_from_client(**kwargs):
    return FavoriteMotorcycleDataFromClient.parse_obj(kwargs)
