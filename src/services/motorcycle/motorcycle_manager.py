from src.adapters.repository.motorcycle.mongodb import MongoDbMotorcycleRepository
from src.factories.motorcycle.motorcycle import build_motorcycle
from src.models.motorcycle.data_from_client import DataFromClient


def process_new_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    return repository.add(motorcycle)


def remove_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    return repository.remove(motorcycle)


def update_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    return repository.update(motorcycle)


def get_motorcyle(
    data_from_client: DataFromClient,
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    returned_motorcycle = repository.get(motorcycle)
    return returned_motorcycle


def motorcyle_list(
    repository: MongoDbMotorcycleRepository = MongoDbMotorcycleRepository()
):
    motorcycle_list = repository.motorcycle_list()
    return motorcycle_list
