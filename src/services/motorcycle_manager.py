from src.adapters.repository.list_repository import MotorcycleListRepository
from src.factories.motorcycle import build_motorcycle
from src.models.data_from_client import DataFromClient


def process_new_motorcyle(
    data_from_client: DataFromClient,
    repository: MotorcycleListRepository = MotorcycleListRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    motorcycle_added = repository.add(motorcycle)
    return motorcycle_added


def remove_motorcyle(
    data_from_client: DataFromClient,
    repository: MotorcycleListRepository = MotorcycleListRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    repository.remove(motorcycle)


def update_motorcyle(
    data_from_client: DataFromClient,
    repository: MotorcycleListRepository = MotorcycleListRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    motorcycle_updated = repository.update(motorcycle)
    return motorcycle_updated
