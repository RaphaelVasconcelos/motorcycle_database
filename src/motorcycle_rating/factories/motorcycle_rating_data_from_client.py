from src.motorcycle_rating.domain.models.motorcycle_rating_data_from_client import MotorcycleRatingDataFromClient


def build_motorcycle_rating_data_from_client(**kwargs):
    return MotorcycleRatingDataFromClient.parse_obj(kwargs)
