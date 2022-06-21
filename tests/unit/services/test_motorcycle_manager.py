from src.adapters.repository.list_repository import MotorcycleListRepository
from src.models.data_from_client import DataFromClient
from src.services.motorcycle_manager import process_new_motorcyle, remove_motorcyle, update_motorcyle


def test_it_should_persist_new_motorcycle(data_from_client):
    motorcycle_added = process_new_motorcyle(data_from_client)

    assert motorcycle_added.name == data_from_client.name
    assert motorcycle_added.manufacturer == data_from_client.manufacturer
    assert motorcycle_added.release_year == data_from_client.release_year


def test_it_should_remove_motorcycle(data_from_client):
    list_repository = MotorcycleListRepository()
    motorcycle = process_new_motorcyle(data_from_client, list_repository)

    remove_motorcyle(motorcycle, list_repository)

    assert len(list_repository._collection) == 0


def test_it_should_update_motorcycle(data_from_client):
    process_new_motorcyle(data_from_client)
    motorcycle_to_update = DataFromClient.parse_obj(data_from_client.dict())
    motorcycle_to_update.release_year = "2022"

    updated_motorcycle = update_motorcyle(motorcycle_to_update)

    assert updated_motorcycle.name == motorcycle_to_update.name
    assert updated_motorcycle.manufacturer == motorcycle_to_update.manufacturer
    assert updated_motorcycle.release_year == motorcycle_to_update.release_year
