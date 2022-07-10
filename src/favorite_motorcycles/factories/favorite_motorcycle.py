from src.favorite_motorcycles.domain.models.favorite_motorcycle import FavoriteMotorcycle


def build_favorite_motorcycle(**kwargs):
    return FavoriteMotorcycle.parse_obj(kwargs)
