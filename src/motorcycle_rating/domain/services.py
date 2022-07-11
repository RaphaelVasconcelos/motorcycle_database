from enum import Enum
from src.motorcycle_rating.adapters.repository.mongodb import MongoDbMotorcycleRatingRepository
from src.motorcycle_rating.domain.models.motorcycle_rating import MotorcycleRating


class RatingActions(str, Enum):
    ADD = "add"
    UPDATE = "update"


def action_for_rating_motorcycle(
    motorcycle_rating: MotorcycleRating,
    repository: MongoDbMotorcycleRatingRepository
):
    user_already_rate = repository.get_motorcycle_rating_by_user(motorcycle_rating)
    if user_already_rate:
        return RatingActions.UPDATE
    return RatingActions.ADD
