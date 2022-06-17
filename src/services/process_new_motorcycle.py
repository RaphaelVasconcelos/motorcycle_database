from src.models.data_from_client import DataFromClient


repository = set()


def process_new_motorcyle(
    data_from_client: DataFromClient,
):
    repository.add(tuple(data_from_client))
    return repository
