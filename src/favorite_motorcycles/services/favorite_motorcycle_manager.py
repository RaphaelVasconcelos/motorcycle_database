from src.favorite_motorcycles.adapters.repository.mongodb import MongoDbFavoriteMotorcycleRepository
from src.favorite_motorcycles.domain.models.favorite_motorcyle_result import FavoriteMotorcycleResult
from src.favorite_motorcycles.domain.services import action_for_this_favorite_motorcycle
from src.favorite_motorcycles.factories.favorite_motorcycle import build_favorite_motorcycle
from src.models.motorcycle.data_from_client import DataFromClient


def toggle_favorite_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbFavoriteMotorcycleRepository = MongoDbFavoriteMotorcycleRepository()
):
    favorite_motorcycle = build_favorite_motorcycle(**data_from_client.dict())
    action_required = action_for_this_favorite_motorcycle(favorite_motorcycle, repository)

    match action_required:
        case action_required.ADD:
            result = repository.add_favorite_motorcycle(favorite_motorcycle)
            return FavoriteMotorcycleResult(action=action_required, is_succeed=result)
        case action_required.REMOVE:
            result = repository.remove_favorite_motorcycle(favorite_motorcycle)
            return FavoriteMotorcycleResult(action=action_required, is_succeed=result)
        case _:
            return FavoriteMotorcycleResult(action="invalid", is_succeed=False)
