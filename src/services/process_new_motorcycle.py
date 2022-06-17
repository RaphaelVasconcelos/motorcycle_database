from src.factories.motorcycle import build_motorcycle
from src.models.data_from_client import DataFromClient


repository = []


def process_new_motorcyle(
    data_from_client: DataFromClient,
):
    motorcycle = build_motorcycle(**data_from_client.dict())
    repository.append(motorcycle)
    return repository
