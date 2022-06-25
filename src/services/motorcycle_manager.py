from src.adapters.repository.list_repository import MotorcycleListRepository
from src.adapters.repository.mongodb import MongoDbMotorcycleRepository
from src.factories.motorcycle import build_motorcycle
from src.models.data_from_client import DataFromClient


def process_new_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    result = repository.add(motorcycle)
    return result


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


def get_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    returned_motorcycle = repository.get(motorcycle)
    return returned_motorcycle


def motorcyle_list(
    repository: MotorcycleListRepository = MotorcycleListRepository()
):
    motorcycle_list = repository.list()
    return motorcycle_list
