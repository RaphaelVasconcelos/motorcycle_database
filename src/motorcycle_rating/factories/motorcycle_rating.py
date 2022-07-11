from src.motorcycle_rating.domain.models.motorcycle_rating import MotorcycleRating


def build_motorcycle_rating(**kwargs):
    return MotorcycleRating.parse_obj(kwargs)
