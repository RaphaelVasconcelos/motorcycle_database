from src.adapters.repository.list_repository import MotorcycleListRepository
from src.services.process_new_motorcycle import process_new_motorcyle
from src.services.remove_motorcycle import remove_motorcyle


def test_it_should_remove_motorcycle(data_from_client):
    list_repository = MotorcycleListRepository()
    motorcycle = process_new_motorcyle(data_from_client, list_repository)

    remove_motorcyle(motorcycle, list_repository)

    assert len(list_repository._collection) == 0
