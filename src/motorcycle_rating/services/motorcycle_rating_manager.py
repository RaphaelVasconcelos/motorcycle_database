from src.motorcycle_rating.adapters.repository.mongodb import MongoDbMotorcycleRatingRepository
from src.motorcycle_rating.domain.models.motorcycle_rating_data_from_client import MotorcycleRatingDataFromClient
from src.motorcycle_rating.domain.models.motorcyle_rating_result import MotorcycleRatingResult
from src.motorcycle_rating.domain.services import action_for_rating_motorcycle
from src.motorcycle_rating.factories.motorcycle_rating import build_motorcycle_rating


def handle_motorcyle_rating(
    data_from_client: MotorcycleRatingDataFromClient,
    repository: MongoDbMotorcycleRatingRepository = MongoDbMotorcycleRatingRepository()
):
    motorcycle_rating = build_motorcycle_rating(**data_from_client.dict())
    action_required = action_for_rating_motorcycle(motorcycle_rating, repository)

    match action_required:
        case action_required.ADD:
            result = repository.add_motorcycle_rating(motorcycle_rating)
            return MotorcycleRatingResult(action=action_required, is_succeed=result)
        case action_required.UPDATE:
            result = repository.update_motorcycle_rating(motorcycle_rating)
            return MotorcycleRatingResult(action=action_required, is_succeed=result)
        case _:
            return MotorcycleRatingResult(action="invalid", is_succeed=False)
